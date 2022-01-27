from django.core.management.base import BaseCommand, CommandError
from main.models import *
from django_seed import Seed
import random

seeder = Seed.seeder()

class Command(BaseCommand):

    def id_range(self, type):
        range_list = []
        if type == 'legal':
            for i in range(102, 903, 100):
                range_list.append(str(i)[:-2] + '02')
            return range_list
        elif type == 'dept':
            for i in range(103, 1304, 100):
                range_list.append(str(i)[:-2] + '03')
            return range_list
        else:
            for i in range(101, 2902, 100):
                range_list.append(str(i)[:-2] + '01')
            return range_list


    def handle(self, *args, **options):
        print('Starting to fill up database...')
        seeder.add_entity(TMail, 31000)
        seeder.add_entity(DStatus, 2, {
            'status_name': lambda x: random.randint(0, 1),
        })
        seeder.add_entity(DType, 3)
        seeder.add_entity(DGender, 3)
        seeder.add_entity(TPhone, 50000)
        seeder.add_entity(TClient, 43000)
        seeder.add_entity(TSocial, 45000)
        seeder.add_entity(TLegalEntity, 2000)
        seeder.add_entity(TDepartment, 5000)
        seeder.add_entity(TLegalEntityDepartment, 20, {
            'id_legal_entity': lambda x: TLegalEntity.objects.get(id=random.choice(self.id_range('legal'))),
            'id_department': lambda x: TDepartment.objects.get(id=random.choice(self.id_range('dept')))
        })
        seeder.add_entity(TClientDepartment, 500, {
            'id_client': lambda x: TClient.objects.get(id=random.choice(self.id_range('client'))),
            'id_department': lambda x: TDepartment.objects.get(id=random.choice(self.id_range('dept')))
        })
        inserted_pks = seeder.execute()
        print("Database successfully filled up with fake datas!")
