import requests
import json
import string
import random
import threading
import concurrent.futures



ID_1 = "fanez"
ID_2 = "irzko"

def get_x_firebase_appcheck():
    spread_sheet_id = "1RCgSI_iUxB_u4zQBrvYL8w0AE2WzhiBmyHVATUCNtB0"
    sheet_id = "0"
    res = requests.get(f"https://docs.google.com/spreadsheets/d/{spread_sheet_id}/export?format=csv&id={spread_sheet_id}&gid={sheet_id}")
    return res.text
X_FIREBASE_APPCHECK = get_x_firebase_appcheck()

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
  if len(token_list) > 0:
    print(f"Đã tạo thành công {len(token_list)} tài khoản!")
    print("Tiến hành ref...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(
        token_list)) as executor:
      executor.map(ref_cross, range(len(token_list)))
  else:
    print("Không thể tạo tài khoản!")
