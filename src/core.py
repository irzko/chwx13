
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
            "X-Firebase-Appcheck": "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQyOTkwNiwiaWF0IjoxNzA0NDI4MTA2LCJqdGkiOiJ5UWw5bkQ4MWNsTlprV3JsR1ZfcFhMbGhXcFpNdmhaMVhKRDAyT3BiTUd3In0.HD477ffgQyU1vztK0z1YouMiq4CghKWPvdzkRF3Xez2fvBgkaIZ32oC8Nnmb6vBJHfeNR-m6ORZjBgpJP-v6qfneMaYptELAekmCO5Y6cDymOQqL7LcEF7yJW7imwsoPEubucu6_ceoLDvbLbDI3tCps0rSzeTpgOX9sncvBLwjenqLVwFymafRjvoJ6qA90danwx9kpfoQJezYsYBxv13ID_T0jLZ1cveUAUUyJIwd6gPYb98hvoMeO8oqfv0yL7oqzRdymNb3oPTheDsPV9G_4VZxoZwGIBwzELT1gS9nnGg2s5p2Q-o4CNRIV4kONnws3Bx6xkZzyDDytGLKu6FY7IAisjJ6FER69CzL5r_WsCTBG4b30AioVkokeVHvke8cY3nnayJS1BS7JnfB6YnACpziKz4dj63o-3X7HFsdI2gqCJpLD0WQ9y3J3CqiXRTiqw5Aek8-bUZLuult3bonyU3Z4eVXuEavahPTHVHd335Oguwf8XVdjFIZL2Q7r",
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
            "X-Firebase-Appcheck": "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQyOTkwNiwiaWF0IjoxNzA0NDI4MTA2LCJqdGkiOiJ5UWw5bkQ4MWNsTlprV3JsR1ZfcFhMbGhXcFpNdmhaMVhKRDAyT3BiTUd3In0.HD477ffgQyU1vztK0z1YouMiq4CghKWPvdzkRF3Xez2fvBgkaIZ32oC8Nnmb6vBJHfeNR-m6ORZjBgpJP-v6qfneMaYptELAekmCO5Y6cDymOQqL7LcEF7yJW7imwsoPEubucu6_ceoLDvbLbDI3tCps0rSzeTpgOX9sncvBLwjenqLVwFymafRjvoJ6qA90danwx9kpfoQJezYsYBxv13ID_T0jLZ1cveUAUUyJIwd6gPYb98hvoMeO8oqfv0yL7oqzRdymNb3oPTheDsPV9G_4VZxoZwGIBwzELT1gS9nnGg2s5p2Q-o4CNRIV4kONnws3Bx6xkZzyDDytGLKu6FY7IAisjJ6FER69CzL5r_WsCTBG4b30AioVkokeVHvke8cY3nnayJS1BS7JnfB6YnACpziKz4dj63o-3X7HFsdI2gqCJpLD0WQ9y3J3CqiXRTiqw5Aek8-bUZLuult3bonyU3Z4eVXuEavahPTHVHd335Oguwf8XVdjFIZL2Q7r",
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
