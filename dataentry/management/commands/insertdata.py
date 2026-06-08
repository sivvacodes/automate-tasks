from django.core.management.base import BaseCommand
from dataentry.models import Student



class Command(BaseCommand):
    help="Insert data to Database"

    def handle(self, *args, **options):
        dataset=[
            {"roll_no":1,"name":"name1","age":20},
            {"roll_no":2,"name":"name2","age":21},
            {"roll_no":3,"name":"name3","age":22}


        ]

        for data in dataset:
            Student.objects.create(roll_no=data["roll_no"],name=data["name"],age=data["age"])
        self.stdout.write("data inserted",self.style.SUCCESS)
        
