from fastapi import FastAPI, Depends, HTTPException, Request, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import Item, SessionLocal

app = FastAPI()


@app.get("/home")
def het_home():
    return {"message": "Hello, World!"}


class ItemSchema(BaseModel):
    name: str
    color: str


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/item", response_model=int, status_code=status.HTTP_201_CREATED)
def add_item(
    item: ItemSchema,
    db_session: Session = Depends(get_db_session),
):
    db_item = Item(name=item.name, color=item.color)
    db_session.add(db_item)
    db_session.commit()
    db_session.refresh(db_item)
    return db_item.id


@app.get("/item/{item_id}", response_model=ItemSchema)
def get_item(
    item_id: int,
    db_session: Session = Depends(get_db_session),
):
    item_db = db_session.get(Item, item_id)
    if not item_db:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")
    return item_db
