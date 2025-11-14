import json
from models import User


def test_add_user(test_client, user_payload, mocker):
    mock_session_add = mocker.patch("app.db.session.add", autospec=True)
    mock_session_commit = mocker.patch("app.db.session.commit", autospec=True)

    # Simulate POST request
    response = test_client.post(
        "/users",
        data=json.dumps(user_payload),
        content_type="application/json",
    )

    assert response.status_code == 201
    create_response_json = json.loads(response.data)
    assert create_response_json.keys() == {"message": "User created"}.keys()
    assert "User created with id" in create_response_json.get("message")

    # Ensure the session operations were called correctly
    mock_session_add.assert_called_once()
    mock_session_commit.assert_called_once()

    # Mock User.query returns a list with new User instance
    mock_user_query = mocker.patch("app.User.query")
    expected_user_object = User(
        username=user_payload["username"],
        email=user_payload["email"],
    )
    mock_user_query.all.return_value = [expected_user_object]

    # Simulate GET request
    response = test_client.get("/users")
    assert response.status_code == 200
    read_response_json = json.loads(response.data)

    mock_user_query.all.assert_called_once()
    assert read_response_json == [
        {
            "id": None,
            "username": user_payload["username"],
            "email": user_payload["email"],
        }
    ]
