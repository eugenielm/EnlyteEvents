from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=254, db_index=True)
    organization = models.CharField(max_length=254, db_index=True)
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#datefield
    start_date = models.DateField(db_index=True)
    cost = models.PositiveSmallIntegerField(db_index=True)
    event_original_id = models.CharField(max_length=25, unique=True)
