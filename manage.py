python
"""Django's command-line utility for administrative tasks."""
import os
import sys


if __name__ == '__main__':
    main()

def main():
check=[(chech_reboot)]
    os.environ.sd('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
