import pytest
from api.dog_api import DogApi

@pytest.fixture
def dog_api():
    return DogApi()