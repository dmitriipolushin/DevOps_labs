from datetime import datetime
import pytz


class Time_controller():

    def moscow_time(self):
        time_now = datetime.now(pytz.timezone('Europe/Moscow'))
        return time_now.strftime("%d/%m/%Y %H:%M:%S")
