import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="session")
def auth_token(playwright):
    request = playwright.request.new_context(base_url="https://fakestoreapi.com")
    response = request.post(
        "/auth/login",
        data={"username": "mor_2314", "password": "83r5^_"},
    )
    assert response.status == 201
    assert "token" in response.json()
    auth_toke = response.json()["token"]

    request.dispose()
    return auth_toke


@pytest.fixture(scope="session")
def api_context(playwright, auth_token):
    request = playwright.request.new_context(
        base_url="https://fakestoreapi.com",
        extra_http_headers={"Authorization": f"Bearer {auth_token}"},
    )
    yield request
    request.dispose()


def test_get(api_context):
    response = api_context.get("users/2")
    assert response.status == 200
    print(response.json())


def test_put(api_context):
    response = api_context.put(
        "users/2",
        data={
            "id": 2,
            "username": "vani",
            "email": "vani@gmail.com",
            "password": "dfs",
        },
    )
    assert response.status == 200
    assert response.json()["username"] == "vani"
    print(response.json())
