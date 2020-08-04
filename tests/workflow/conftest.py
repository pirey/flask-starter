import pytest
from faker import Faker
from faker.providers import internet

from app import db

fake = Faker()
fake.add_provider(internet)


@pytest.fixture
def session():
    return db.session


@pytest.fixture
def reset_db():
    def _reset_db():
        db.reset_db()

    # call reset_db here so we don't have to call it in the test
    _reset_db()

    # return reset_db so we can reset db again in the test if needed
    yield _reset_db
