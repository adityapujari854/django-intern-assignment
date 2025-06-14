#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""

import os
import sys


def main():
    """Run administrative tasks like runserver, migrate, shell, etc."""
    # Set the default Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "that the virtual environment is activated."
        ) from exc

    # Execute the command-line utility
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
