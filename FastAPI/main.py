from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, name: Optional[str] = None):
    return {"item_id": item_id, "name": name}


# def create_redis(...):
#     // 템플릿에서 테라폼 파일 카피해오기
#     //