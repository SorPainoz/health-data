import datetime
import calendar

DAY_NANOSECONDS_LENGTH = 24 * 60 * 60 * 1000000000


def get_yearly_interval(year):
    """
    Produces the datasets interval string for a year

    >>> get_yearly_interval(2019)
    '1546297200000000000-1577833200000000000'

    :param year:
    :return formatted string for datasets query as 'start-end' in nanoseconds from epoch:
    """
    start_date = datetime.datetime(year, 1, 1)
    end_date = datetime.datetime(year, 12, 31)

    range_interval = get_range_interval(start_date, end_date)
    return range_interval


def get_monthly_interval(month, year):
    """
    Produces the datasets interval string for a month

    >>> get_monthly_interval(1,2019)
    '1546297200000000000-1548975600000000000'

    :param month:
    :param year:
    :return formatted string for datasets query as 'start-end' in nanoseconds from epoch:
    """
    start_date = datetime.datetime(year, month, 1)
    last_day_of_the_month = calendar.monthrange(year, month)[1]
    end_date = datetime.datetime(year, month, last_day_of_the_month)

    range_interval = get_range_interval(start_date, end_date)
    return range_interval


def get_daily_interval(day):
    """
    Produces the datasets interval string for a day

    >>> a_day = datetime.datetime(2019, 1, 17)
    >>> get_daily_interval(a_day)
    '1547679600000000000-1547766000000000000'

    :return:
    :param day:
    :return formatted string for datasets query as 'start-end' in nanoseconds from epoch:
    """

    start = int(datetime.datetime.timestamp(day) * 1000000000)
    end = int(start + DAY_NANOSECONDS_LENGTH)

    return f'{start}-{end}'


def get_range_interval(start_date, end_date):
    """
    Produces the datasets interval string for an interval between two dates

    >>> _start_date = datetime.datetime(2019,1,1)
    >>> _end_date = datetime.datetime(2019,1,31)
    >>> get_range_interval(_start_date, _end_date)
    '1546297200000000000-1548975600000000000'

    :param start_date:
    :param end_date:
    :return formatted string for datasets query as 'start-end' in nanoseconds from epoch:
    """

    start = int(datetime.datetime.timestamp(start_date) * 1000000000)
    delta_days = (end_date - start_date).days + 1
    end = int(start + DAY_NANOSECONDS_LENGTH * delta_days)

    return f'{start}-{end}'
