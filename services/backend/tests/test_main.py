def test_root(client):
    response = client.get(url='/')
    assert response.status_code == 200
