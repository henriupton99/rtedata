import pytest
from rtedata.client import Client
import os

@pytest.fixture(scope="session")
def client():
    return Client(
        client_id=os.getenv("RTE_CLIENT_ID"),
        client_secret=os.getenv("RTE_CLIENT_SECRET")
    )
