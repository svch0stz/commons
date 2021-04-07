import datetime as dt
import logging

import pytz


def lookup_abbreviated_timezone(datetime, abbreviation):
    for tz in pytz.all_timezones:
        if abbreviation == pytz.timezone(tz).tzname(datetime):
            return pytz.timezone(tz)


def convert_date_time_zscaler(datetime_str):
    try:
        timezone = datetime_str.split(' ')[-1].strip()
        datetime_str = datetime_str[:len(datetime_str) - len(timezone)].strip()
        datetime = dt.datetime.strptime(datetime_str, '%B %d, %Y %I:%M:%S %p')
        timezone = lookup_abbreviated_timezone(datetime, timezone)
        return timezone.localize(datetime)
    except Exception as ex:
        logging.error("Error processing date: {} - {}".format(datetime_str, ex))
        raise ex


def convert_to_utc(datetime):
    return datetime.astimezone(pytz.UTC)


def convert_to_epoch_mills(datetime):
    return int(round(datetime.timestamp() * 1000))


def utc_epoch_mills_now():
    return convert_to_epoch_mills(convert_to_utc(dt.datetime.now()))
