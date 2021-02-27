import bisect
import calendar
import datetime
import logging
import math

from django.conf import settings

logger = logging.getLogger("django_calendardate")


fy_start_month = getattr(settings, "FISCAL_YEAR_START_MONTH", 10)


def process_date(date):
    """
    Returns a dictionary with all of the below processes completed,
    which can then be imported directly to CalendarDate model.
    """

    metadata = {}
    metadata["calendar_date"] = date
    metadata["calendar_day"] = get_calendar_day(date)
    metadata["calendar_month"] = get_calendar_month(date)
    metadata["calendar_year"] = get_calendar_year(date)
    metadata["calendar_quarter"] = get_calendar_quarter(date)
    metadata["fiscal_year"] = get_fiscal_year(date)
    metadata["fiscal_quarter"] = get_fiscal_quarter(date)
    metadata["day_of_week"] = get_day_of_week(date)
    metadata["day_of_isoweek"] = get_day_of_isoweek(date)
    metadata["day_of_quarter"] = get_day_of_quarter(date)
    metadata["day_of_year"] = get_day_of_year(date)
    metadata["week_of_month"] = get_week_of_month(date)
    metadata["week_of_year"] = get_week_of_year(date)
    metadata["isoweek_of_year"] = get_isoweek_of_year(date)
    metadata["is_weekday"] = get_is_weekday(date)
    metadata["is_leap_year"] = get_is_leap_year(date)
    metadata["days_in_month"] = get_days_in_month(date)

    logger.debug(f"process_date metadata: {metadata}")

    return metadata


def get_quarter_begin(date):
    quarter_begins = [datetime.date(date.year, month, 1) for month in (1, 4, 7, 10)]
    idx = bisect.bisect(quarter_begins, date)
    return quarter_begins[idx - 1]


def get_calendar_day(date):
    return date.day


def get_calendar_month(date):
    return date.month


def get_calendar_year(date):
    return date.year


def get_calendar_quarter(date):
    return int(math.ceil(date.month / 3))


def get_fiscal_year(date):
    return date.year if date.month < fy_start_month or fy_start_month == 1 else date.year + 1


def get_fiscal_quarter(date):

    if fy_start_month in [1, 4, 7, 10]:
        quarter_starts = [1, 4, 7, 10]
        quarter_idx = quarter_starts.index(fy_start_month)
    elif fy_start_month in [2, 5, 8, 11]:
        quarter_starts = [2, 5, 8, 11]
        quarter_idx = quarter_starts.index(fy_start_month)
    else:
        quarter_starts = [3, 6, 9, 12]
        quarter_idx = quarter_starts.index(fy_start_month)

    quarter_start_dates = [datetime.date(date.year, month, 1) for month in quarter_starts]

    quarter = bisect.bisect(quarter_start_dates, date) - quarter_idx
    return quarter if quarter > 0 else quarter + 4


def get_day_of_week(date):
    return date.weekday()


def get_day_of_isoweek(date):
    return date.isoweekday()


def get_day_of_quarter(date):
    delta = date - get_quarter_begin(date) + datetime.timedelta(days=1)
    return delta.days


def get_day_of_year(date):
    return int(date.strftime("%j"))


def get_week_of_month(date):
    def week_of_month(date_object):
        """Returns the week of the month for the specified date."""
        first_day = date_object.replace(day=1)
        dom = date_object.day
        adjusted_dom = dom + first_day.weekday()
        return int(math.ceil(adjusted_dom / 7.0))

    return week_of_month(date)


def get_week_of_year(date):
    return int(date.strftime("%U")) + 1


def get_isoweek_of_year(date):
    return int(date.strftime("%W")) + 1


def get_is_weekday(date):
    return True if date.weekday() < 5 else False


def get_is_leap_year(date):
    year = date.year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_days_in_month(date):
    _, days = calendar.monthrange(date.year, date.month)
    return days
