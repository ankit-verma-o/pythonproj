from django.core.management.base import BaseCommand, CommandError
from sightings.models import sightings
import csv
import datetime as dt

class Command(BaseCommand):
    help = 'Import Squirrel Census Data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs = '+', type = str)

    def handle(self, *args, **options):
        path=str(options['csv_file'][0])
        with open(path) as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                for i in ('Running','Chasing','Climbing','Eating','Foraging','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent', 'Runs from'):
                        if row[i]=='false':
                            row[i]= False
                        else:
                            row[i]= True
                s = sightings( 
                            X = row['X'],
                            Y = row['Y'],
                            Unique_Squirrel_ID = row['Unique Squirrel ID'],
                            Shift = row['Shift'],
                            Date = dt.datetime.strptime(row['Date'],'%m%d%Y'),
                            Age = row['Age'],
                            Primary_Fur_Color = row['Primary Fur Color'],
                            Location = row['Location'],
                            Specific_Location = row['Specific Location'],
                            Running = row['Running'],
                            Chasing = row['Chasing'],
                            Climbing = row['Climbing'],
                            Eating = row['Eating'],
                            Foraging = row['Foraging'],
                            Other_Activities = row['Other Activities'],
                            Kuks = row['Kuks'],
                            Quaas = row['Quaas'],
                            Moans = row['Moans'],
                            Tail_flags = row['Tail flags'],
                            Tail_twitches = row['Tail twitches'],
                            Approaches = row['Approaches'],
                            Indifferent = row['Indifferent'],
                            Runs_from = row['Runs from'],
                           )
                 
                s.save()
