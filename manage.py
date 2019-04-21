#!/usr/bin/env python
import os
import sys

# print("어떤 환경에서 구축할래?\n")
# print("1.development(localhost)\n")
# print("2.deployment(실제서버)\n")
# print("1 or 2")
# env_var = input()

if __name__ == '__main__':
    # if env_var == '1':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
    # else:
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.deployment')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )(exc)
    execute_from_command_line(sys.argv)
