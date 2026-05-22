from app import add 

def test_add():
    client = app.test.client()
    response = client.get('/')
    assert response.status_code == 200