from django.db import models
from datetime import date
from django.utils.translation import gettext as _


class sightings(models.Model):

    X=models.FloatField(help_text=_('Latitude'))
   
    Y=models.FloatField(help_text=_('Longitude'))

    Unique_Squirrel_ID=models.CharField(
        help_text=_('Enter the unique squirrel id'),
        max_length=50,
        primary_key = True,
        default = None,
    )

    AM='AM'
    PM='PM'
    shift_choice=((AM,'AM'),(PM,'PM'),)
    Shift = models.CharField(
        help_text=_('shift of sighting'),
        max_length=2,
        choices=shift_choice,
        blank=True,
    )
    
    Date = models.DateField(help_text=_('Date'),null=True,blank=True)

    adult='Adult'
    juvenile='juvenile'
    age_choice=((adult,'Adult'),(juvenile,'Juvenile'))
    Age = models.CharField(choices=age_choice, max_length=50, blank=True,null=True)

    grey='Grey'
    cinnamon='Cinnamon'
    black='Black'
    furcolor_choice=((grey,'Grey'),(cinnamon,'Cinnamon'),(black,'Black'))
    Primary_Fur_Color = models.CharField(help_text=_('Enter the fur color of squirrel'),max_length=50,choices=furcolor_choice, blank=True,null=True)

    ground_plane='Ground Plane'
    above_ground='Above Ground'
    location_choice=((ground_plane,'Ground Plane'),(above_ground,'Above Ground'))
    Location = models.CharField(help_text=_('Enter location of squirrel'),max_length=50,choices=location_choice,blank=True,null=True)

    Specific_Location=models.CharField(help_text=_('Enter the specific location of squirrel'),max_length=250,blank=True,null=True)

    Running = models.BooleanField(help_text=_('Is it running?'),default=True)

    Chasing = models.BooleanField(help_text=_('Is it chasing?'),default=True)

    Climbing = models.BooleanField(help_text=_('Is it climbing?'),default=True)
    
    Eating = models.BooleanField(help_text=_('Is it eating?'),default=True)

    Foraging = models.BooleanField(help_text=_('Is it foraging?'),default=True)

    Other_Activities = models.CharField(help_text=_('Enter the activity of squirrel'),max_length=100,blank=True,null=True)

    Kuks = models.BooleanField(help_text=_('Is it kuking?'),default=True)

    Quaas = models.BooleanField(help_text=_('Is it quaaing?'),default=True)

    Moans = models.BooleanField(help_text=_('Is it moaning?'),default=True)

    Tail_flags = models.BooleanField(help_text=_('Is it having tailflags?'),default=True)

    Tail_twitches = models.BooleanField(help_text=_('Is it having tail twitches?'),default=True)

    Approaches = models.BooleanField(help_text=_('Is it approaching?'),default=True)

    Indifferent = models.BooleanField(help_text=_('Is it indifferent?'),default=True)

    Runs_from = models.BooleanField(help_text=_('Is it running from the sighter?'),default=True)

    def __str__(self):
        return self.Unique_Squirrel_ID
    

# eate your models here.
