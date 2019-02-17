import datetime as dt


def get_todays_date():
    today = dt.datetime.now()
    return today.date()
