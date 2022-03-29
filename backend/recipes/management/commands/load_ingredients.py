import json
import os
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from foodgram.settings import BASE_DIR
from recipes.models import Ingredient

FILE_PATCH = os.path.join(BASE_DIR, "data")


class Command(BaseCommand):
    help = 'Load Ingredient'
    
    def add_arguments(self, parser):
        parser.add_argument("filename", default="ingredients.json", nargs="?",
                            type=str)

    def handle(self, *args, **options):
        try:
            with open(os.path.join(FILE_PATCH, options["filename"]),
                      "r", encoding="utf8") as file:
                data = json.load(file)
                for ingredient in data:
                    try:
                        Ingredient.objects.create(
                            name=ingredient["name"],
                            measurement_unit=ingredient["measurement_unit"]
                        )
                    except IntegrityError:
                        print(f'Ingredient {ingredient["name"]} '
                              f'{ingredient["measurement_unit"]}'
                              f'already in database')
        except FileNotFoundError:
            raise CommandError('the file is missing data')
