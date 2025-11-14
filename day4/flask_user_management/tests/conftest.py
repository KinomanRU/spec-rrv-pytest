import pytest
import random
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.exc import OperationalError as SQLAlchemyOperationalError
from app import create_app
from models import db


def pytest_addoption(parser):
    parser.addoption(
        "--dburl",
        action="store",
        default="sqlite:///:memory:",
        help="Database URL used for tests",
    )


@pytest.fixture(scope="session")
def db_url(request):
    return request.config.getoption("--dburl")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    db_url = session.config.getoption("--dburl")
    try:
        engine = create_engine(db_url, poolclass=StaticPool)
        connection = engine.connect()
        connection.close()
        print("Using Database URL", db_url)
        print("Database connection successful")
    except SQLAlchemyOperationalError as e:
        print(f"Failed connecting to database {db_url!r}: {e}")
        pytest.exit(reason="Stopping tests because of database connection failure")


@pytest.fixture(scope="session")
def app(db_url):
    """Session-wide test 'app' fixture"""
    test_config = {
        "SQLALCHEMY_DATABASE_URI": db_url,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(app_config=test_config)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def test_client(app):
    """Test client for the app"""
    return app.test_client()


@pytest.fixture
def user_payload():
    suffix = random.randint(1, 100)
    return {
        "username": f"user_{suffix}",
        "email": f"user_{suffix}@mail.com",
    }
