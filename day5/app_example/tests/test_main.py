import pytest
from httpx import AsyncClient, ASGITransport
from app.database import Item
from app.main import app


@pytest.mark.asyncio
async def test_read_main():
    client = AsyncClient(
        transport=ASGITransport(app),
        base_url="http://localhost",
    )
    response = await client.get("/home")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

    await client.aclose()


def test_read_main_client(test_client):
    response = test_client.get("/home")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_client_can_add_read_item(test_client, test_db_session):
    response = test_client.get("/item/1")
    assert response.status_code == 404

    response = test_client.post("/item", json={"name": "ball", "color": "red"})
    assert response.status_code == 201

    item_id = response.json()
    item = test_db_session.get(Item, item_id)

    assert item is not None

    response = test_client.get("/item/1")
    assert response.status_code == 200
    assert response.json() == {"name": "ball", "color": "red"}
