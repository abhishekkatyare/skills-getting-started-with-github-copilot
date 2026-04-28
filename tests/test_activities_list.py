def test_get_activities_returns_activity_catalog(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert payload

    for activity_name, details in payload.items():
        assert activity_name
        assert expected_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)
