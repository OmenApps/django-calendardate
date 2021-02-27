===================
django-calendardate
===================

*A calendar model with date metadata for querying against.*

Sometimes it is useful to have a range of dates and associated metadata stored in the database, rather than calculating on-the-fly, particularly when creating reports based on quarters, fiscal years, etc. This is where django-calendardate comes in. Also known as a date dimension table or calendar table, the inspiration for this project comes from `this article <https://www.sqlshack.com/designing-a-calendar-table/>`_.

django-calendardate provides:

* a model for storing metadata about a set of dates.
* a management command for generating the metadata


THIS PROJECT IS PRE_RELEASE. It works, but is missing documentation and tests. Be cautious.

Usage
-----

To process a range of dates (ignoring any duplicates):

    ``python manage.py process_dates 2021-01-01 2021-12-31``


To process a range of dates (overwriting any duplicates):

    ``python manage.py process_dates 2021-01-01 2021-12-31 --force``


Optional settings.py settings
-----------------------------

By default, django-calendardate assumes a fiscal year starts in October. If your fiscal year begins on a different month, set ``FISCAL_YEAR_START_MONTH`` to the month number (1-indexed). For instance January would be 1).

    ``FISCAL_YEAR_START_MONTH = 1``


Model Fields
------------

Each of the following are automatically calculated and inserted into the model using the ``process_dates`` management command.

    **calendar_date** (*DateField*)
        The actual date object

    **calendar_day** (*PositiveSmallIntegerField*)
        Number from 1 through 31

    **calendar_month** (*PositiveSmallIntegerField*)
        Month number from 1-12

    **calendar_year** (*PositiveSmallIntegerField*)
        Current year, eg: 2017, 2025, 1984

    **calendar_quarter** (*PositiveSmallIntegerField*)
        1-4, indicates quarter within the current year

    **fiscal_year** (*PositiveSmallIntegerField*)
        Current fiscal year, eg: 2017, 2025, 1984

    **fiscal_quarter** (*PositiveSmallIntegerField*)
        1-4, indicates fiscal quarter within the current fiscal year

    **day_of_week** (*PositiveSmallIntegerField*)
        Monday is 0 and Sunday is 6

    **day_of_isoweek** (*PositiveSmallIntegerField*)
        Monday is 1 and Sunday is 7

    **day_of_quarter** (*PositiveSmallIntegerField*)
        Number from 1-92, indicates the day # in the current quarter

    **day_of_year** (*PositiveSmallIntegerField*)
        Number from 1-366

    **week_of_month** (*PositiveSmallIntegerField*)
        Number from 1-6, indicates the number of week within the current month

    **week_of_year** (*PositiveSmallIntegerField*)
        Number from 1-53, indicates the number of week within the current year

    **isoweek_of_year** (*PositiveSmallIntegerField*)
        Number from 1-53, indicates the number of isoweek within the current year

    **is_weekday** (*BooleanField*)
        True if Monday-->Friday, False for Saturday/Sunday

    **is_leap_year** (*BooleanField*)
        True if current year is a leap year

    **days_in_month** (*PositiveSmallIntegerField*)
        Number of days in the current month

Model Properties
----------------

Each of the following properties are provided for each date.

    **get_day_name** (*property*)
        returns a string with the name of the day for the given date (e.g.: "Monday")

    **get_month_name** (*property*)
        returns a string with the name of the month for the given date (e.g.: "January")

    **get_month_abbreviated** (*property*)
        returns a string with the abbreviated name of the month for the given date (e.g.: "Jan")


Quick Example:
--------------

Say you have an Order model with a `order_date` field, and you want to query all of the orders that were placed in the third fiscal quarter of fiscal year 2021.

.. code-block:: python

    # Return list of  of dates in 3rd Qtr of FY21
    third_fiscal_qtr_dates = CalendarDate.objects.filter(fiscal_year=2021, fiscal_quarter=3).values_list('calendar_date', flat=True)
    
    # Filter on those dates
    third_qtr_orders = Order.objects.filter(order_date__in=third_fiscal_qtr_dates)


To Do
-----

1. Testing

2. Better documentation

3. Translations (strings already marked for translation)
