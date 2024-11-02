import random
from faker import Faker
from  django.core.management.base import BaseCommand
from  tracker.models import User, Transaction, Category

class Command(BaseCommand):
    help = 'Generates fake transactions'
    def handle(self, *arg, **options):
        faker = Faker()
        categories = ["Bills", "Food", "Medical", "Clothes", "Housing", "Salary", "Social"]

