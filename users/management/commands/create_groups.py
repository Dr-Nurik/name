from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Creates default user groups'

    def handle(self, *args, **kwargs):
        Group.objects.get_or_create(name='Patient')
        Group.objects.get_or_create(name='Doctor')
        Group.objects.get_or_create(name='Administrator')
        self.stdout.write(self.style.SUCCESS('Successfully created user groups'))
