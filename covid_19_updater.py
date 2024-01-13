import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r=requests.get('http://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    text=f'Confirmed cases : {data["cases"]} \ndeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast=ToastNotifier()
        toast.show_toast("Covid-19-Updates",text,duration=20)
        time.sleep(5)

update()
