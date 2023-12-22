def test_home_page_post_with_fixture(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask User Management Example!" not in response.data


def test_view_hotel_with_fixture(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted to (GET)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = client.get("/viewPackageDetail/Capella Singapore")
    assert response.status_code == 200
    assert b"Capella Singapore" in response.data
