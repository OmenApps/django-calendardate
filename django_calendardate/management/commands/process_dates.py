"""
Based on the date range provided, this command adds CalendarDate
objects for any non-yet-existing dates in that range.
"""
import logging

from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
from ...models import CalendarDate
from ...date_utilities import process_date

logger = logging.getLogger("django_calendardate")


class Command(BaseCommand):
    help = """Processes (and creates) dates for the CalendarDate model.
        Use: `manage.py process_dates 2000-01-01 2005-12-31`

        Optionally, the --force argument will overwrite existing dates.
        """

    def add_arguments(self, parser):
        parser.add_argument("start_date", type=str, help="Start of the date period, formatted as: YYYY-MM-DD")
        parser.add_argument("end_date", type=str, help="End of the date period, formatted as: YYYY-MM-DD")

        parser.add_argument(
            "--force",
            action="store_true",
            help="Force overwrite of existing dates",
        )

    def handle(self, *args, **options):
        start_date = datetime.strptime(options["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(options["end_date"], "%Y-%m-%d").date()
        delta = timedelta(days=1)

        logger.debug(f"Processing dates from {start_date} to {end_date}")

        while start_date <= end_date:

            date_metadata = process_date(start_date)

            obj, created = CalendarDate.objects.update_or_create(**date_metadata)

            start_date += delta

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created/verified CalendarDate for {obj.calendar_date}.")
                )
            else:
                if options["force"]:
                    self.stdout.write(self.style.SUCCESS(f"CalendarDate for {obj.calendar_date} updated."))
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f"CalendarDate for {obj.calendar_date} already exists. Skipping.")
                    )
