from django.core.management.base import BaseCommand,CommandError
import csv
from dataentry.models import Student_data
from django.apps import apps

class Command(BaseCommand):
    help="Import data from CSV file"

    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str,help="path of csv file")
        parser.add_argument('model',type=str,help="model name")

   
    def handle(self, *args, **kwargs):
        model=None
        file_path=kwargs['file_path']
        model_name=kwargs['model']

        
        for app_config in apps.get_app_configs():
            try:
                model=apps.get_model(app_config.label,model_name)
                break
            except LookupError:
                continue
        if not model:
            raise CommandError

        with open(file_path,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
            self.stdout.write("Data inserted from CSV",style_func=self.style.SUCCESS)

    


        