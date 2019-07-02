# Generated by Django 2.2.3 on 2019-07-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=254)),
                ('organization', models.CharField(db_index=True, max_length=254)),
                ('start_date', models.DateField(db_index=True)),
                ('cost', models.PositiveSmallIntegerField(db_index=True)),
                ('event_original_id', models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]
