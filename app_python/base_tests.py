from datetime import datetime
from .controllers.time_controller import moscow_time
import pytz


def test_get_moscow_time_dateformat():
    """ Unit test to check that overall dateformat is correct
    """
    time_now = datetime.now(pytz.timezone('Europe/Moscow'))
    assert moscow_time() == time_now.strftime("%d/%m/%Y %H:%M:%S")


def test_get_moscow_time_correct_time():
    """ Check that all particular parts of the time
        (year, month, day, hour, minute) is correct
    """
    result = moscow_time()
    parsed_result_date = datetime.strptime(result, "%d/%m/%Y %H:%M:%S")

    time_now = datetime.now(pytz.timezone('Europe/Moscow'))

    assert parsed_result_date.year == time_now.year
    assert parsed_result_date.month == time_now.month
    assert parsed_result_date.day == time_now.day
    assert parsed_result_date.hour == time_now.hour
    assert parsed_result_date.minute == time_now.minute
