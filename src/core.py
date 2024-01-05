
import requests
import json
import string
import random
import threading
import concurrent.futures

X_FIREBASE_APPCHECK = "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQ2MzY2NSwiaWF0IjoxNzA0NDYxODY1LCJqdGkiOiJrTmpWQTR6eXJxeGpqWVY0cFF2emFvdmJONmJuNVBRU0FKX1Izcmh0MzVjIn0.dpkwv7I_EuC5gZxxBvWzyPHOWXpG7VGZe5t2Hj3ohvgwnFaOqDnommq7h_5Bo9PdOEWtA2K4epKQLjNMmEovRfgAIH-UYUXmZAqs24nDMSdVFnbv6NK7VS_vCXJYw3fq4GTy_gm5abritGMc6L7-8omFnpBqFSlgbAIEiG7P4PGyOUSQFfD9Q71gbikrSLwM1dFvYI9fg_WW1-TAeAaRbm2tWMm5tvXIIb7x1THSMSEAUJifcgxTRA17667tJ7wlc3cOTiV_XGJ7FuQqnlzC7eEunUXVAkTun9zNyvTIBq6C02HH_53N8xiL5AgS810oJdyvV26gbmP4PKo3sp5s5O9Foyc9pWf3kVaztW_o0aPBCRrQg7gL-zVQGucLkZxBmemBtWgsDAvtAI0rKMOOhkS0il8-l0erdEAAslC0U9WvVI7Q2OlSHjHBa2k0r8-PP2rk3CS4CULGqxjNqSc55k6ksgi85UzyAxQdirgvWDyYRYfg3KZZcwjzZU0chQ5h"

def generate_random_string(length):
  return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def sign_up(email: str, password: str):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyBCZ5M2ukumMvtvwtOGkBw0Tk8ttAbP4Is"
    payload = json.dumps(
        {
            "returnSecureToken": True,
            "email": email,
            "password": password,
            "clientType": "CLIENT_TYPE_WEB"
        }
    )

    headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "X-Firebase-Appcheck": X_FIREBASE_APPCHECK,
            "Origin": "https://app.brcapp.com"
        }
    res = requests.post(
        url=url,
        data=payload,
        headers=headers,
    )
    return res


def set_referred(id_token: str, referred_by: str):
    url = "https://users-3tzf7aaa5a-ew.a.run.app/set-referred-by"
    payload = json.dumps(
        {"referredBy": referred_by}
    )

    headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Origin": "https://app.brcapp.com",
            "Referer": "https://app.brcapp.com/",
            "Authorization": id_token
        }
    res = requests.post(
        url=url,
        data=payload,
        headers=headers
    )
    return res


stop_flag = threading.Event()

def make_request(i):
    if not stop_flag.is_set():
        email = generate_random_string(20) + "@gmail.com"
        res = sign_up(email, generate_random_string(15))

        if res.status_code == 200:
            id_token = res.json().get("idToken")
            with open("token.txt", "a") as file:
                file.write(id_token + "\n")
            refRes = set_referred(id_token, "irzko")
            if refRes.status_code == 200:
                print(f"[{i}] OK")
            else:
                print(f"[{i}] Error:", refRes.json().get("error").get("message"))
                stop_flag.set()
        else:
            print(f"[{i}] Error:", res.json().get("error").get("message"))
            stop_flag.set()

def handle_exception(fut):
    try:
        fut.result()
    except Exception as exc:
        print("Request failed")

def run():
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(make_request, i) for i in range(300)]
        for fut in concurrent.futures.as_completed(futures):
            handle_exception(fut)
