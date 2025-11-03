import json
import pytest


def test1(playwright):
    request = playwright.request.new_context()
    response = request.get("https://reqres.in/api/users/2")
    responseBody = response.json()
    assert response.status == 200
    # assert responseBody["data"][1]["id"] == 2
    request.dispose()


@pytest.fixture(scope="session")
def input_data():
    with open("./data/test_data.json", "r") as data1:
        return json.load(data1)


def test2(playwright, input_data):
    request = playwright.request.new_context()
    response = request.post(
        "https://jsonplaceholder.typicode.com/posts", data=input_data
    )

    responseBody = response.json()
    assert response.status == 201
    print("output", responseBody)
    request.dispose()
