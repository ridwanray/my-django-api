import os

from django.core.management.base import BaseCommand
from accounts.models import CustomUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(email="alabarise@gmail.com").exists():
            CustomUser.objects.create_superuser(email="alabarise@gmail.com", password="WireLee1@")

