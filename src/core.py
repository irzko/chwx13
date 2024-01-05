
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
            "X-Firebase-Appcheck": "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQzMzU3MCwiaWF0IjoxNzA0NDMxNzcwLCJqdGkiOiJlVGNqQVZMSFFxRUlTaXBuR0ZfVEFfZVF6aVJpY1BUVUNRN0tGVXVweENRIn0.QPzIgqL2WFgidBISJx_RUH4AjGOvf4RO0S5XZfTsHX9J53wldlRMLl53FSCM-tqfKkNMoWysFF3iSoEtDfAql-SvA0PgyOu85sTyHVClzVXpRnFZjarU3vuM7J1DjDjbh9b1r6ppgZ6mMN0_PvMfEQ8HAIxoF1YrrDD4T_YjjTRWYuttpRXeUtN8LDfpxxGni7I8oe6QZNMbKOTevfNhUfthZ43a4B_3it-SqJLCC-rpBAqeW9b9i3oSiHVPPnCTWhjkbWDcwRyCMx5m_QVkAWVRfwUvdPWPC1VkGZVRGtC0v5kVt3kdiAPk80sMZ9LNxi1zdetM4GLxB8IT9Yojp5YPbp-QGak2gYP61LVJ2-YVIycUJBpU0_Na7bXgGm_ORmfFvMpbSpS0fAR8zPNj20B9kwPjSCdm1FUw3HbwSVklblF3XOQ3-QBeX8lLtsXkEVjHepSBDkreRLVqsj7BI9ZPMNgTKTNI6_oE7GgR-_z3PJJpr-61xmbTMl9_ZKzH",
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
