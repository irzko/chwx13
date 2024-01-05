import requests
import json
import string
import random
import threading
import concurrent.futures

X_FIREBASE_APPCHECK = "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQ3OTMwMSwiaWF0IjoxNzA0NDc3NTAxLCJqdGkiOiJ1M0hzdFZVZ3dmOFdIcnBocmlSckRjaDlaX3F3TDlzQ2RhbFlJejR2SUI4In0.pOJ6Dz-27OxsdB2M8nzuIy5AVPMP5VvAHQsejYMi2ty_GEm9miGOb93KcnvmUciUPQL5NqcSVWjpNyYGkR9-vV0hO-te5OppcvWN6bhwzBkA1SlJJjMShr9fU3KEaNui3I8iAIoK3UzsETiGAtL4HJ1co-CLtXdIiSkS-2WVP7nYN2ay2sHCk4hDXXKrQec34maHJS3jdnRzSMZCooVaNZiEzkG_Gf7K_S3RCVVR8yYDYOx5rtyrvPfIH8uVxR_Zk_I4Hmyp8TGtR_ngf2w41N2eQlnUYpxIobKOw8bb6tHTi_60Zaq8pXOzMEGxM28vfW42U7rXt_mktyBMMGaQn6TxDTOgV-ky6WYRWW35r9gDIPXAWUUg6W5Ri9EiEwJcGQYHqlUSpUQC9BOhWxzFR65W9WZKMC1tResRr5jPgZXnal2t6vzhFu6gdV87yf4xki_40Dv098ghQxbzbcp_Q563FKOyVQFW5OK6j7tadCJNppa8Lk19M-ooravb0qlk"
ID_1 = "fanez"
ID_2 = "irzko"

def generate_random_string(length):
  return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def sign_up(email: str, password: str):
  url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyBCZ5M2ukumMvtvwtOGkBw0Tk8ttAbP4Is"
  payload = json.dumps({
      "returnSecureToken": True,
      "email": email,
      "password": password,
      "clientType": "CLIENT_TYPE_WEB"
  })

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
  payload = json.dumps({"referredBy": referred_by})

  headers = {
      "Content-Type": "application/json",
      "Accept": "*/*",
      "Origin": "https://app.brcapp.com",
      "Referer": "https://app.brcapp.com/",
      "Authorization": id_token
  }
  res = requests.post(url=url, data=payload, headers=headers)
  return res


stop_flag = threading.Event()
token_list = []

def get_clone(i):
  if not stop_flag.is_set():
    email = generate_random_string(20) + "@gmail.com"
    res = sign_up(email, generate_random_string(15))

    if res.status_code == 200:
      id_token = res.json().get("idToken")
      token_list.append(id_token)
    else:
      stop_flag.set()


def ref_cross(i):
  while True:
    set_referred(token_list[i], ID_1)
    refRes = set_referred(token_list[i], ID_2)
    if refRes.status_code == 200:
      print(f"[{i}] -> OK")
    else:
      print(f"[{i}] Error:", refRes.text)


def run():
  with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    futures = [executor.submit(get_clone, i) for i in range(300)]
    for _ in concurrent.futures.as_completed(futures):
      pass

  
  with concurrent.futures.ThreadPoolExecutor(max_workers=len(
      token_list)) as executor:
    executor.map(ref_cross, range(len(token_list)))
