from datetime import datetime
import pytz
from .controllers.time_controller import moscow_time
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_moscow_time():
    return moscow_time()
