import requests
import json
import time
import urllib3

# Desactivar warnings de SSL no verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_create_user():
    url = "https://dummy.restapiexample.com/api/v1/create"
    payload = {
        "name": "Maria",
        "salary": 2000,
        "age": 31
    }

    headers = {
         "Accept": "application/json",
        "User-Agent": "pytest-client" #user agent is mandatory on the server side
    }

    # para los casos de to many requests (429), se ha añadido un retry:
    for attempt in range (3):
        response = requests.post(url, json=payload, headers=headers, verify=False)
        if response.status_code == 429:
            print("Demasiadas solicitudes, esperando 5 segundos...")
            time.sleep(5)

        else:
            break    

    print(f"Status Code: {response.status_code}")
    print(f"Response json: {response.json()}")

    assert response.status_code == 200 or response.status_code == 201

    data = response.json()
    assert data["status"] == "success"

    response_data = data["data"]
    assert response_data["name"] == payload["name"]
    assert response_data["salary"] == payload["salary"]
    assert response_data["age"] == payload["age"]
    assert "id" in response_data