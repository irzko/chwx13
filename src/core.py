import requests
import json
import string
import random
import threading
import concurrent.futures

X_FIREBASE_APPCHECK = "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQ3NzE1OSwiaWF0IjoxNzA0NDc1MzU5LCJqdGkiOiJ1RktyV2cxWl9yVDlBOHh0bkhyWWZBYS15VzhXLVRoV0VaZ3cwUjR4aVpRIn0.JHauF8y02XeAbcotwhY_9U5NVq6t-99vkf5Qq01m39Db5PicQ5MoAUENbVCTpzszmja21S-tRRymxjg3Fbgmi7JgNmNpy7Zui608Oa_P-3qaDSITxfT7oAv2fz5__p6nkFXOqoMLqgLkGfH6bGfkkwaY3IY8uxgwY5zg8A8t3wRQey8g4K8-Lh0tYlpWqP2qlUhh0m2FTbwTQaZ8hL55CDYRSEbloXk_jWbTHYArSLjXJ2zvXrkAuqzEylPatvO-L6JksncVHR9PETG5Q4azkpeLY5f8LAn1SZrtcmd-XfdK-cdMP4dYxsphYBIsVRdcRskePfRw-tT51W8NRKJOyXtPu-Lsy1sitwXN6-waV2fYmwu0rgFV2Fb0O0hxKuopz_V1IWK9SH5DYadzzQtdV0PGCo8g0NOoNXYIZESTc_dSjKxLyWzFcSltBtF3z_QNYRVvfpX_9K1TFrm3LJ_IiriXsxHfyTv1EFLYZ3M8Td_LrcsDJcrcGsq-vp3s13IU"
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
