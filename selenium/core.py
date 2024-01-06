
import requests
import json
import string
import random
import threading
import concurrent.futures


def get_data_gsheet(spread_sheet_id: str, sheet_id: str):
    res = requests.get(f"https://docs.google.com/spreadsheets/d/{spread_sheet_id}/export?format=csv&id={spread_sheet_id}&gid={sheet_id}")
    return res.text

def csv_to_object(csv: str):
  lines: list[str] = csv.split("\n")
  headers: list[str] = lines[0].split(",")
  for line in lines:
    if line == lines[0]:
      continue
    obj = {}
    currentline = line.split(",")
    for j in range(len(headers)):
      obj[headers[j].strip()] = currentline[j].strip()
  return obj

data = get_data_gsheet("1RCgSI_iUxB_u4zQBrvYL8w0AE2WzhiBmyHVATUCNtB0", "564557539")
config = csv_to_object(data)

X_FIREBASE_APPCHECK = config["x_firebase_appcheck"]
USERNAME = config["username"]

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
            refRes = set_referred(id_token, USERNAME)
            if refRes.status_code == 200:
                print(f"[{i}] OK")
            else:
                print(f"[{i}] Error:", refRes.json().get("error").get("message"))
                stop_flag.set()
        else:
            print(f"[{i}] Error:", res.json().get("error").get("message"))
            stop_flag.set()

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(make_request, i) for i in range(300)]
        for _ in concurrent.futures.as_completed(futures):
            pass
