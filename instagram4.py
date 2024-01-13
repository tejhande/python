import requests

url = "https://www.instagram.com/accounts/login/ajax/"

payload = {
    "username": "dt1dt2d",
    "enc_password": "Love@#Emiway",
    "queryParams": {},
    "optIntoOneTap": False
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "x-csrftoken": "XcYbTIOzB1FMEZpnyJq3CjD1SOHJOE2f",
    "x-instagram-ajax": "9ce3d24be58d",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.post(url, data=payload, headers=headers)

print(f"Response content: {response.content}")
print(f"Response status code: {response.status_code}")
print(f"Response headers: {response.headers}")
print(f"Response cookies: {response.cookies}")

try:
    response_json = response.json()
    authenticated = response_json.get("authenticated")
    if authenticated == True:
        print("Login successful!")
    else:
        print("Login failed.")
except Exception as e:
    print(f"Error decoding JSON response: {e}")
