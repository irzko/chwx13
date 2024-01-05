
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
            "X-Firebase-Appcheck": "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQzMTc1MiwiaWF0IjoxNzA0NDI5OTUyLCJqdGkiOiJnRmszSnBkUGxKTzhrNjJSaXVmdk1LRHQ0eXZjLTljU2swRXZOekpLNDYwIn0.gcImnp5mectJaDnavT9i7PjjQ_iBEN9t8dTtmlirJnLdTn-W5FE4mPfnE2WXb0_aWzw6qYOJdupFvnifKXUKrzQbbEdUQrb81KWjXlIqP27ws6PU5s_im4f8OBzcpD40C6-_95v3ttYb7sDyghuPM7jX9rCtyd0e0_n9Rxf_bsjkHLLvk1N6PK642BeeFW75cJb3QV1AP0C9Pczgb9pTmF5xCWJMZEOnWF5MMm5FTwj7xHqDQfun-6NOgs1Yhb9Oc5pQW-tuUEKWFOmZFhgxNjyrrmQnyD7UbOZB5Zadnzo6CxJFLixIv9zNIUTZUJz8CpgCBZWLsELyi8loiZag85dbyeMXBgmVXQClaSU5RuuoDtphCgUXOUaLLQo0eNTHCT7M3xqrVi5EVh_Ajmzpww11MF3BSErox6NejOlMizZ9afUpjorLQNV16C1CRVA7moDr-Bqv_LKN5JmCyri37VI9E1o5DMgJ_471_g0aac_b40uqYim1mK-6ODhGcFVo",
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
            "X-Firebase-Appcheck": "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQzMTc1MiwiaWF0IjoxNzA0NDI5OTUyLCJqdGkiOiJnRmszSnBkUGxKTzhrNjJSaXVmdk1LRHQ0eXZjLTljU2swRXZOekpLNDYwIn0.gcImnp5mectJaDnavT9i7PjjQ_iBEN9t8dTtmlirJnLdTn-W5FE4mPfnE2WXb0_aWzw6qYOJdupFvnifKXUKrzQbbEdUQrb81KWjXlIqP27ws6PU5s_im4f8OBzcpD40C6-_95v3ttYb7sDyghuPM7jX9rCtyd0e0_n9Rxf_bsjkHLLvk1N6PK642BeeFW75cJb3QV1AP0C9Pczgb9pTmF5xCWJMZEOnWF5MMm5FTwj7xHqDQfun-6NOgs1Yhb9Oc5pQW-tuUEKWFOmZFhgxNjyrrmQnyD7UbOZB5Zadnzo6CxJFLixIv9zNIUTZUJz8CpgCBZWLsELyi8loiZag85dbyeMXBgmVXQClaSU5RuuoDtphCgUXOUaLLQo0eNTHCT7M3xqrVi5EVh_Ajmzpww11MF3BSErox6NejOlMizZ9afUpjorLQNV16C1CRVA7moDr-Bqv_LKN5JmCyri37VI9E1o5DMgJ_471_g0aac_b40uqYim1mK-6ODhGcFVo",
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
