import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('phones.csv', type=str)

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for phone in phones:
                Phone(id=int(phone['id']),
                      name=phone['name'],
                      price=phone['price'],
                      image=phone['image'],
                      release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                      lte_exists=phone['lte_exists'].lower() == 'true').save()
        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))