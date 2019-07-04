import os, datetime
from dateutil import parser

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from events_api.models import Event

from eventbrite import Eventbrite


class Command(BaseCommand):
    help = 'Pull events from Eventbrite and store them in the db as Event instances'

    def add_arguments(self, parser):
        parser.add_argument(
            '--token',
            help='Oauth token to access the Eventbrite API',
        )
        parser.add_argument(
            '--number_of_events',
            '-n',
            type=int,
            default=500,
            help='Number of events to fetch',
        )


    def handle(self, *args, **options):
        "Pull events from Eventbrite and store them in the db as Event instances"
        # https://github.com/eventbrite/eventbrite-sdk-python/blob/master/eventbrite/client.py
        eventbrite = Eventbrite(settings.EVENTBRITE_OAUTH_TOKEN or options.get('token'))
        number_of_events_to_parse = options['number_of_events']
        count = 0
        page = 1
        events = eventbrite.event_search(expand='ticket_availability,organizer', page=page)

        while count < number_of_events_to_parse:
            for event in events.get('events'):
                cost = int(
                    (float(event['ticket_availability']['minimum_ticket_price']['major_value']) \
                    + float(event['ticket_availability']['maximum_ticket_price']['major_value'])
                    )/2
                )
                try:
                    # only unique events with values for all fields will be saved
                    Event.objects.create(
                        name=event['name']['text'],
                        organization=event['organizer']['name'],
                        event_original_id=event['id'],
                        start_date=parser.parse(event['start']['local']),
                        cost=cost
                    )
                    count += 1
                except: pass

                if count >= number_of_events_to_parse:
                    break

            if events.get('pagination').get('has_more_items') and count < number_of_events_to_parse:
                page += 1
                events = eventbrite.event_search(expand='ticket_availability,organizer', page=page)
            else: break
        
        print("\nSaved {} events in the database!\n".format(count))