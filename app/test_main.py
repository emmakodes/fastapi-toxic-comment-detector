from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_check_toxicity():
    response = client.post("/comments/")
    response = client.post(
        "/comments/",
        json={"comments": "string"},
    )
    assert response.status_code == 200


def test_check_toxicity_wrong_datatype():
    response = client.post(
        "/comments/",
        json={"comments": 20},
    )
    assert response.status_code == 422
    assert response.json() == {
                                "detail": [
                                    {
                                        "type": "string_type",
                                        "loc": [
                                            "body",
                                            "comments"
                                        ],
                                        "msg": "Input should be a valid string",
                                        "input": 20,
                                        "url": "https://errors.pydantic.dev/2.3/v/string_type"
                                    }
                                ]
                            }