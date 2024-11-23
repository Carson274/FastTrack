from typing import Union

from fastapi import FastAPI

app = FastAPI()

# user-read-currently-playing
# /me/player/currently-playing

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

