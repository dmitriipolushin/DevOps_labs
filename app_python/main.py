from datetime import datetime
import pytz
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    time_now = datetime.now(pytz.timezone('Europe/Moscow'))
    return time_now.strftime("%d/%m/%Y %H:%M:%S")
