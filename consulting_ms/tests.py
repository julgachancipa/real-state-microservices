import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# Test Case 1: Valid Request with City Parameter
def test_get_properties_city_cali():
    response = client.get("/properties?city=cali")

    assert response.status_code == 207 or response.status_code == 200
    json_response = response.json()

    if response.status_code == 207:
        assert isinstance(json_response["detail"], list)
        assert isinstance(json_response["body"], list)

        json_response = json_response["body"]

    assert isinstance(json_response, list)

    for property in json_response:
        assert isinstance(property["address"], (str, type(None)))
        assert property["city"] == "cali"
        assert isinstance(property["status_name"], str)
        assert isinstance(property["price"], int)
        assert isinstance(property["description"], (str, type(None)))


# Test Case 2: Valid Request with Multiple Parameters
def test_get_properties_city_year():
    response = client.get("/properties?year=2011&city=bogota")

    assert response.status_code == 207 or response.status_code == 200
    json_response = response.json()

    if response.status_code == 207:
        assert isinstance(json_response["detail"], list)
        assert isinstance(json_response["body"], list)

        json_response = json_response["body"]

    assert isinstance(json_response, list)

    for property in json_response:

        assert isinstance(property["address"], str)
        assert property["city"] == "bogota"
        assert isinstance(property["status_name"], str)
        assert isinstance(property["price"], int)
        assert isinstance(property["description"], str)


# Test Case 3: Filter by Status List
def test_get_properties_city_status_list():
    response = client.get(
        "/properties?city=pereira&status_list=en_venta&status_list=vendido"
    )

    assert response.status_code == 207 or response.status_code == 200

    json_response = response.json()

    if response.status_code == 207:
        assert isinstance(json_response["detail"], list)
        assert isinstance(json_response["body"], list)

        json_response = json_response["body"]

    assert isinstance(json_response, list)

    for property in json_response:
        assert property["city"] == "pereira"
        assert property["status_name"] in ["en_venta", "vendido"]


# Test Case 4: Filter by Single Status
def test_get_properties_city_single_status():
    response = client.get("/properties?city=pereira&status_list=vendido")

    assert response.status_code == 207 or response.status_code == 200

    json_response = response.json()

    if response.status_code == 207:
        assert isinstance(json_response["detail"], list)
        assert isinstance(json_response["body"], list)

        json_response = json_response["body"]

    assert isinstance(json_response, list)

    for property in json_response:
        assert property["city"] == "pereira"
        assert property["status_name"] == "vendido"


# Test Case 5: Handling Invalid Data Types
def test_get_properties_invalid_description():
    response = client.get("/properties?city=cali")
    assert response.status_code == 207 or response.status_code == 200

    json_response = response.json()

    if response.status_code == 207:
        assert isinstance(json_response["detail"], list)
        assert isinstance(json_response["body"], list)

        json_response = json_response["body"]

    assert isinstance(json_response, list)

    for property in json_response:
        assert property["city"] == "cali"


# Test Case 6: Empty Response for Non-Existent Data
def test_get_properties_no_existent_status():
    response = client.get("/properties?city=medellin&status_list=no_existent_status")
    assert response.status_code == 400
    json_response = response.json()
    assert json_response == {
        "detail": "Invalid status value. Valid options are: ['pre_venta', 'en_venta', 'vendido']"
    }


if __name__ == "__main__":
    pytest.main()
