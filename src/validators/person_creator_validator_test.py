import pytest
from src.validators.person_creator_validator import person_creator_validator

class MockHttpRequest:
    def __init__(self, body: dict) -> None:
        self.body = body

def test_valid_request():
    http_request = MockHttpRequest({
        "first_name": "romy",
        "last_name": "Eduardo",
        "age": 10,
        "pet_id": 1
    })

    person_creator_validator(http_request)

def test_invalid_request():
    http_request = MockHttpRequest({
        "first_name": "1",
        "last_name": "Eduardo",
        "age": 10,
        "pet_id": 1
    })

    with pytest.raises(Exception):
        person_creator_validator(http_request)
