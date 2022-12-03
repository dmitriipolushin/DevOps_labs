from datetime import datetime
from .controllers.time_controller import Time_controller
import pytz


def test_dateformat():
    time_now = datetime.now(pytz.timezone('Europe/Moscow'))
    time = time_now.strftime("%d/%m/%Y %H:%M:%S")
    assert Time_controller().moscow_time() == time
