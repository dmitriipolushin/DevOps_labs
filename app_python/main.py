from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from controllers.time_controller import Time_controller
from controllers.visits import Visits

app = FastAPI()


@app.get('/')
def moscow_time():
    time = Time_controller().moscow_time()
    Visits().add_visits(time)
    return time


@app.get('/visits', response_class=PlainTextResponse)
def get_visits():
    return Visits().get_visits()
