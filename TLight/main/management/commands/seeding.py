from django.core.management.base import BaseCommand, CommandError
from main.models import *
from django_seed import Seed
import random

seeder = Seed.seeder()

class Command(BaseCommand):

    def id_range(self, type):
        range_list = []
        if type == 'legal':
            for i in range(101, 603, 100):
                range_list.append(str(i)[:-2] + '02')
            return range_list
        elif type == 'dept':
            for i in range(103, 604, 100):
                range_list.append(str(i)[:-2] + '03')
            return range_list
        else:
            for i in range(101, 602, 100):
                range_list.append(str(i)[:-2] + '01')
            return range_list


    def handle(self, *args, **options):
        print('Starting to fill up database...')
        seeder.add_entity(TMail, 8)
        seeder.add_entity(DStatus, 2, {
            'status_name': lambda x: random.randint(0, 1),
        })
        seeder.add_entity(DType, 3)
        seeder.add_entity(DGender, 3)
        seeder.add_entity(TPhone, 5)
        seeder.add_entity(TClient, 9)
        seeder.add_entity(TSocial, 10)
        seeder.add_entity(TLegalEntity, 10)
        seeder.add_entity(TDepartment, 10)
        seeder.add_entity(TLegalEntityDepartment, 7, {
            'id_legal_entity': lambda x: TLegalEntity.objects.filter(id=random.choice(self.id_range('legal')))[0] if
            TLegalEntity.objects.filter(id=random.choice(self.id_range('legal'))).exists() else TLegalEntity.objects.first(),
            'id_department': lambda x: TDepartment.objects.filter(id=random.choice(self.id_range('dept')))[0] if
            TDepartment.objects.filter(id=random.choice(self.id_range('dept'))).exists() else TDepartment.objects.first()
        })
        seeder.add_entity(TClientDepartment, 6, {
            'id_client': lambda x: TClient.objects.filter(id=random.choice(self.id_range('client')))[0] if
            TClient.objects.filter(id=random.choice(self.id_range('client'))).exists() else TClient.objects.first(),
            'id_department': lambda x: TDepartment.objects.filter(id=random.choice(self.id_range('dept')))[0] if
            TDepartment.objects.filter(id=random.choice(self.id_range('dept'))).exists() else TDepartment.objects.first()
        })
        inserted_pks = seeder.execute()
        print("Database successfully filled up with fake datas!")
