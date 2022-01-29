from typing import Optional

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from src import fii_scrapper
app = FastAPI()


@app.get("/")
def helf_check():
    return {"Status": "OK"}


@app.get("/fiis")
def read_item(response_class=UJSONResponse):
    return fii_scrapper.collect()