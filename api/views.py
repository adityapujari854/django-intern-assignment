from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .tasks import send_welcome_email

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message': 'This is a public endpoint.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    user = request.user

    # Trigger welcome email in background via Celery
    send_welcome_email.delay(user.username, user.email)

    return Response({
        'message': f'Hello {user.username}, you are authenticated!',
        'note': 'A welcome email has been sent in the background.'
    })
