def test1(playwright):
    request = playwright.request.new_context()
    response = request.get("https://reqres.in/api/users/2")
    responseBody = response.json()
    assert response.status == 200
    # assert responseBody["data"][1]["id"] == 2
    request.dispose()


def test2(playwright):
    request = playwright.request.new_context()
    response = request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={"userId": 20, "id": 20, "title": "sdsf", "body": "sdfsd"},
    )

    responseBody = response.json()
    assert response.status == 201
    request.dispose()
