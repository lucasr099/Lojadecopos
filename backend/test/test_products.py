from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_products():
    response = client.get("/products/")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)

    # Se houver produtos, valida campos
    if data:
        product = data[0]
        assert "id" in product
        assert "name" in product
        assert "price" in product
        assert "stock" in product
