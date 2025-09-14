from app import create_app

app = create_app()
client = app.test_client()

def test_exemple_1_returns_two():
    payload = {"dimensao":{"altura": 102, "largura": 40}, "peso": 400}
    r = client.post("/shipping/quotes", json = payload)
    assert r.status_code == 200
    data = r.get_json()
    assert len(data) == 2
    assert data[0]["nome"] == "Entrega Ninja"
    assert abs(data[0]["valor_frete"] - 12.00) < 1e-9
    assert data[0]["prazo_dias"] == 6
    assert data[1]["nome"] == "Entrega Kabum"
    assert abs(data[1]["valor_frete"] - 8.00) < 1e-9
    assert data[1]["prazo_dias"] == 4

def test_exemple_2_returns_one():
    payload = {"dimensao":{"altura": 152, "largura": 50}, "peso": 850}
    r = client.post("/shipping/quotes", json = payload)
    assert r.status_code == 200
    data = r.get_json()
    assert len(data) == 1
    assert data[0]["nome"] == "Entrega Ninja"
    assert abs(data[0]["valor_frete"] - 25.50) < 1e-9
    assert data[0]["prazo_dias"] == 6

def test_exemple_3_returns_empty():
    payload = {"dimensao":{"altura": 230, "largura": 162}, "peso": 5600}
    r = client.post("/shipping/quotes", json = payload)
    assert r.status_code == 200
    data = r.get_json() == []

def test_weigths_must_be_positive_422():
    payload = {"dimensao":{"altura": 20, "largura": 20}, "peso": 0}
    r = client.post("/shipping/quotes", json = payload)
    assert r.status_code == 422
