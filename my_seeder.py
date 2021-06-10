import os
import django
from django_seed import Seed

from about.models import FAQ

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


seeder = Seed.seeder()
seeder.add_entity(FAQ, 5)
inserted_pks = seeder.execute()
