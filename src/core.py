
import requests
import json
import string
import random
import threading
import concurrent.futures

X_FIREBASE_APPCHECK = "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQ2MTc5NywiaWF0IjoxNzA0NDU5OTk3LCJqdGkiOiJZaGdnOXpNTWJFZlFVVFZLemdSejB3WDF6bFVGV3ZiMF8tV01tVjBISWd3In0.Kig2xBU_Hso3UzE9Za0Bgpwcq7oB5ERe618yKE_EWrWJyZbThkfZJFiqC6P5HOWVfm7MwX4e1sAxDeCsTzwnNTY-73_wJ7nFq5suS7FX5VoydgsY3y2NqJvlX4ykkrnowdyn_CJvc8dDwEfbqzzUDTwDSkQ_4BDJRWAC2eqNpteGk-pAJoxP3MKvOAuzFLCRY5GyIhTnh_y5pT3kr-0rFTESu5iB-C2YrTkK5HqSlGbzFA0sWadjPVJUrdbpdaVHo2GoSG6znnRXigS5iTQFNECXos4074mB6Us01PS0VAsjsGK9-uZ7bhfuY-lknpNRWUebbGAEMzj0TLDH6bnQ4GB8cc7QN6VBoR0gQzKIqZXH1d75ryfgYaw1Qlqvz8OzxXBpMqqASp52oJVu2euYGx2thLp-w9FF6ieaOTAV_m7BrD0lR5vtQ840G_Hw-iIF69b9ww79wl1uOzFtMT73WGSzjlUriH7JhcrPz7eaN5XodqYGkfZsKsn-6VfGr0sf"

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
