def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy", "version": "0.2.0"}


def test_lists_seeded_destinations(client):
    response = client.get("/api/destinations")
    assert response.status_code == 200
    assert len(response.get_json()["data"]) == 3


def test_filters_destinations_case_insensitively(client):
    response = client.get("/api/destinations?q=sYDneY")
    results = response.get_json()["data"]
    assert len(results) == 1
    assert results[0]["country"] == "Australia"


def test_rejects_invalid_contact_message(client):
    response = client.post("/api/contact", json={"name": "Robert", "email": "bad"})
    assert response.status_code == 400
    assert response.get_json()["error"] == "validation_error"


def test_accepts_valid_contact_message(client):
    response = client.post(
        "/api/contact",
        json={
            "name": "Robert Mears",
            "email": "robert@example.com",
            "subject": "Trip question",
            "message": "I would like more information about Berlin.",
        },
    )
    assert response.status_code == 201
    assert response.get_json()["id"] == 1

