import requests
import json

def test_get_employees():
    url = "https://dummy.restapiexample.com/api/v1/employees"
    headers = {
        "Accept": "application/json",
        "User-Agent": "pytest-client" #user agent is mandatory on the server side
    }

    r = requests.get(url, headers=headers)
    print("Status:", r.status_code)

    data = r.json()
    print(json.dumps(data, indent=2))
