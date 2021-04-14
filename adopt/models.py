from django.db import models
from django.utils.translation import gettext


class Sighting(models.Model):
    Longitude  = models.FloatField(
            help_text = gettext('Longitude of the sight'),
            max_length=30,
            null = True,
            blank = True,
            )

    Latitude = models.FloatField(
            help_text = gettext('Latitude of the sight'),
            max_length=30,
            )

    Unique_Squirrel_ID = models.CharField(
            help_text = gettext('The unique ID of the squirrel'),
            max_length = 30,
            )
    
    Shift = models.CharField(
            help_text = gettext('AM or PM'),
            max_length = 2,
            choices = (("AM", "AM"), ("PM", "PM")),
            default = "AM")
    
    Date = models.DateField(
            help_text = gettext('Date sighted. The format is in mmddyyyy'),
            null = True,
            blank = True,
            default = None,
            )
   
    Age = models.CharField(
            help_text = gettext('Adult or Juvenile'),
            choices = (('Adult','Adult'), ('Juvenile', 'Juvenile'), (None, ''), ('?', '?'),),
            blank = True,
            default = '',
            max_length = 30,
            )

    Primary_Fur_Color = models.CharField(
            help_text = gettext('Fur color'),
            max_length = 16,
            choices = (('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), (None, ''),),
            blank = True,
            )
    
    Location = models.CharField(
            help_text = gettext('Location'),
            choices = (('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), (None, ''),),
            blank = True,
            max_length = 100,
            )

    Specific_Location = models.CharField(
            help_text = gettext('Specific location'),
            blank = True,
            max_length = 100,
            )

    Running = models.NullBooleanField(
            help_text = gettext('Running'),
            blank=True,
    )
    
    Chasing = models.NullBooleanField(
            help_text = gettext('Chasing'),
            blank=True,
    )

    Climbing = models.NullBooleanField(
            help_text = gettext('Climbing'),
            blank=True,
    )

    Eating = models.NullBooleanField(
            help_text = gettext('Eating'),
            blank=True,
    )

    Foraging = models.NullBooleanField(
            help_text = gettext('Foraging'),
            blank=True,
    )

    Other_Activities = models.CharField(
        help_text = gettext('Other Activities'),
        null = True,
        blank = True,
        max_length = 1000,
    )

    Kuks = models.NullBooleanField(
            help_text = gettext('Kuks'),
            blank=True,
    )

    Quaas = models.NullBooleanField(
            help_text = gettext('Quaas'),
            blank=True,
    )

    Moans = models.NullBooleanField(
            help_text = gettext('Moans'),
            blank=True,
    )

    Tail_flags = models.NullBooleanField(
            help_text = gettext('Tail flags'),
            blank=True,
    )

    Tail_twitches = models.NullBooleanField(
            help_text = gettext('Tail twitches'),
            blank=True,
    )

    Approaches = models.NullBooleanField(
            help_text = gettext('Approaches'),
            blank=True,
    )

    Indifferent = models.NullBooleanField(
            help_text = gettext('Indifferent'),
            blank=True,
    )
    
    Runs_from = models.NullBooleanField(
            help_text = gettext('Runs_From'),
            blank=True,
    )
