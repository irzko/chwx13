
import requests
import json
import string
import random
import threading
import concurrent.futures

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
            "X-Firebase-Appcheck": "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQzNTQzNSwiaWF0IjoxNzA0NDMzNjM1LCJqdGkiOiJ3R2l1UFozd0hvdlhybE5XOFRBRmFjMDlaREd3bGc4cmZGU1ludFhTWl84In0.R9WZKzoPQ903BCvJaKhjdEyAkR16DwE-vf20uc-H-zWNjzrAuGRL35QsPmV6dxGJm1f1o1ep6EKDKhlLpjZmd2scNtmB8xNHxZPJ1h9khNHifgQL0j78nx-orKltckh0Pk0R0fQRQCJAcOiWFswhHb-xfPoyreoeHLsTT70rCu9oSkYkBoUyNG1U2lWAE7XQemdrbVvcoVr1OKBXvD_X7deI-aRpk2sYug9nPtWccRuk7j1eanwVDMJiUMjzHzJelFVWRhKMrYrGjbP-dZUtxN6RbFGWU9Dqic6Mqy2oHma50lt7eu02k8ElDw4d6BvBd8EppZa5RM4umdsD0k9NIeXzELQ74nllxsMZrTRS6H7pZhWG8Qf-_Ypep4UFCRkpb1P8VHmYmBe8FaDsLgyXXse9xDb-iJ9u4DIxjJHF-798f7VBGNx9Ds5SfF5KeFOwYTtV9xqIDA2PkNdIqhzhl8el_QzT8VokapvEBQH_D6TTvRb_Dv1A4WzHc-9PCONl",
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
