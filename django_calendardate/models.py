from django.db import models
from django.utils.translation import gettext as _


class CalendarDate(models.Model):
    calendar_date = models.DateField(_("Date"), unique=True, help_text=_("The actual date object"))
    calendar_day = models.PositiveSmallIntegerField(_("Calendar Day"), help_text=_("Number from 1 through 31"))
    calendar_month = models.PositiveSmallIntegerField(_("Calendar Month"), help_text=_("Month number from 1-12"))
    calendar_year = models.PositiveSmallIntegerField(
        _("Calendar Year"), help_text=_("Current year, eg: 2017, 2025, 1984")
    )
    calendar_quarter = models.PositiveSmallIntegerField(
        _("Calendar Quarter"), help_text=_("1-4, indicates quarter within the current year")
    )
    fiscal_year = models.PositiveSmallIntegerField(
        _("Fiscal Year"), help_text=_("Current fiscal year, eg: 2017, 2025, 1984")
    )
    fiscal_quarter = models.PositiveSmallIntegerField(
        _("Fiscal Quarter"), help_text=_("1-4, indicates fiscal quarter within the current fiscal year")
    )
    day_of_week = models.PositiveSmallIntegerField(_("Day of Week"), help_text=_("Monday is 0 and Sunday is 6"))
    day_of_isoweek = models.PositiveSmallIntegerField(_("Day of ISO Week"), help_text=_("Monday is 1 and Sunday is 7"))
    day_of_quarter = models.PositiveSmallIntegerField(
        _("Day in Quarter"), help_text=_("Number from 1-92, indicates the day # in the current quarter")
    )
    day_of_year = models.PositiveSmallIntegerField(_("Day in Year"), help_text=_("Number from 1-366"))
    week_of_month = models.PositiveSmallIntegerField(
        _("Week of Month"), help_text=_("Number from 1-6, indicates the number of week within the current month")
    )
    week_of_year = models.PositiveSmallIntegerField(
        _("Week of Year"), help_text=_("Number from 1-53, indicates the number of week within the current year")
    )
    isoweek_of_year = models.PositiveSmallIntegerField(
        _("ISO Week of Year"), help_text=_("Number from 1-53, indicates the number of isoweek within the current year")
    )
    is_weekday = models.BooleanField(
        _("Is Weekday"), default=False, help_text=_("True if Monday-->Friday, False for Saturday/Sunday")
    )
    is_leap_year = models.BooleanField(
        _("Is Leap Year"), default=False, help_text=_("True if current year is a leap year")
    )
    days_in_month = models.PositiveSmallIntegerField(
        _("Days in current month"), help_text=_("Number of days in the current month")
    )

    class Meta:
        verbose_name = _("Calendar Date")
        verbose_name_plural = _("Calendar Dates")

        get_latest_by = ["-calendar_date"]
        ordering = ["-calendar_date"]

        indexes = [
            models.Index(fields=["calendar_date"]),
            models.Index(fields=["calendar_year", "calendar_month"]),
            models.Index(fields=["calendar_year", "calendar_quarter"]),
            models.Index(fields=["calendar_year", "week_of_year"]),
            models.Index(fields=["fiscal_year", "fiscal_quarter"]),
            models.Index(fields=["is_weekday"]),
        ]

    def __str__(self):
        return f"{self.date}"

    @property
    def get_day_name(self):
        day_names = {
            1: _("Monday"),
            2: _("Tuesday"),
            3: _("Wednesday"),
            4: _("Thursday"),
            5: _("Friday"),
            6: _("Saturday"),
            7: _("Sunday"),
        }
        return day_names[self.day_of_isoweek]

    @property
    def get_month_name(self):
        month_names = {
            1: _("January"),
            2: _("February"),
            3: _("March"),
            4: _("April"),
            5: _("May"),
            6: _("June"),
            7: _("July"),
            8: _("August"),
            9: _("September"),
            10: _("October"),
            11: _("November"),
            12: _("December"),
        }
        return month_names[self.calendar_month]

    @property
    def get_month_abbreviated(self):
        month_names = {
            1: _("Jan"),
            2: _("Feb"),
            3: _("Mar"),
            4: _("Apr"),
            5: _("May"),
            6: _("Jun"),
            7: _("Jul"),
            8: _("Aug"),
            9: _("Sep"),
            10: _("Oct"),
            11: _("Nov"),
            12: _("Dec"),
        }
        return month_names[self.calendar_month]
