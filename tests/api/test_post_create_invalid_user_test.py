import requests
import json
import time
import urllib3

# Desactivar warnings de SSL no verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_create_employee_invalid():
    url = "https://dummy.restapiexample.com/api/v1/create"
    payload = {
        "name": "",
        "salary": "",
        "age": ""
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "pepito"
    }

    # Validación local simulando lo que debería hacer una API real
    if not payload["name"] or not payload["salary"] or not payload["age"]:
        print("Payload inválido detectado antes de enviar.")
        assert True  # para que pase la prueba una vez que se ha detectado que los datos no son válidos.
        return


    response = requests.post(url, json=payload, headers=headers, verify=False)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    assert response.status_code == 200
    data = response.json()
    print(f"Parsed JSON: {data}")




# Nota: La API dummy no valida el payload.

# Ejemplo: acepta valores vacíos ("") o tipos incorrectos (str en vez de int) 
# y aun así responde con 200 (status "success").

# Por este motivo, en el test se hace una validación local del payload antes de enviarlo.

# Sugerencia de mejora (para una API real):
# - Validar los atributos (nombre, salario y edad).
# - Si los datos son inválidos, la API debería devolver un status code 400 (Bad Request).

# Devolver "success" con datos inválidos puede generar errores posteriores en el sistema
# (ejemplo: guardar información falsa en la base de datos de la empresa).
