import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minimal_settings')
django.setup()

from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'runserver'])