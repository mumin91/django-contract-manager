from django.core.management.base import BaseCommand, CommandError
from expense.models import *


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        pass
        # self.stdout.write(self.style.SUCCESS('Successfully closed poll'))
        # for _ in range(5):
