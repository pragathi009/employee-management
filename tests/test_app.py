import pytest

from app import app, init_db


@pytest.fixture
def client(tmp_path):

    app.config["TESTING"] = True

    import app as application

    application.DATABASE = str(
        tmp_path / "test.db"
    )

    init_db()

    with app.test_client() as client:
        yield client


def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200


def test_add_employee(client):

    response = client.post(
        "/add",
        data={
            "name": "Pragathi",
            "email": "pragathi@example.com",
            "department": "AI",
            "position": "Developer"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Pragathi" in response.data