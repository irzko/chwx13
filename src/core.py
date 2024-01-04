
import requests
import json
import string
import random
from concurrent.futures import ThreadPoolExecutor

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
            "X-Firebase-Appcheck": "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQyOTQwMSwiaWF0IjoxNzA0MzQzMDAxLCJqdGkiOiJvSEwzNHE3NWFVYm44MlRxdlM4dE04R0t2LVJLanZkaTlMbU1uTWIzcm1rIn0.B37o9mX52_ICjjp4e58MTrkP7EuPG5x-IG-BmawebZQs4SBEjH45aDkHT99OnRKNBccF_TT9ZjRkYJgglR7tk-_gNQXaZbhHfZyRFg59ytCn24Ke7AyDKgiNLTnoyP3EpAySpLsw3KFxGePlOKnHtoeykPdMea7rGb41jPZNi2tCFQzllyJapsvZ0cdSwxLkFzXEE2GcpbkzfbWhy2MAIh_btOxhIF0NglMXoxOVbZaTRQx7aKplSNl7U02bxKivSXzhqjV060ZFJr4hJonS225nGrm9Ns0vlkebPZPMMeAihc6pzbpyzcs9xpmhYiGZrv0uwa4MRe953YuSJEs6NoxWsRde10UtJAkkoBd5Qjbj_LPKIAzJVEgsdAXWfnZ1RE7RivGdxsiSW0zDgio5AnQZfXHDKYAH6wqGCd5OPO2UtJ6l3P39RSWFsBxD5LcgwOGSCFRH-3cSCMjJ53rH1ycZvQj_WXbS8RpYGmuOBY8UBbhhHBhwRhyP7pLOIMTl",
            "Origin": "https://app.brcapp.com"
        }

    res = requests.post(
        url=url,
        data=payload,
        headers=headers,
    );


    return res


def set_referred(id_token: str, referred_by: str):
    url = "https://users-3tzf7aaa5a-ew.a.run.app/set-referred-by"
    payload = json.dumps(
        {"referredBy": referred_by}
    )

    headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "X-Firebase-Appcheck": "eyJraWQiOiJYcEhKU0EiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjMxNjkxMzg3NzkxNzp3ZWI6Y2VlOTJhMmQ1N2I2MDZjNTc5MjU3NCIsImF1ZCI6WyJwcm9qZWN0c1wvMzE2OTEzODc3OTE3IiwicHJvamVjdHNcL3ZlbG9jaXR5LWEzNTYwIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6XC9cL2ZpcmViYXNlYXBwY2hlY2suZ29vZ2xlYXBpcy5jb21cLzMxNjkxMzg3NzkxNyIsImV4cCI6MTcwNDQyOTQwMSwiaWF0IjoxNzA0MzQzMDAxLCJqdGkiOiJvSEwzNHE3NWFVYm44MlRxdlM4dE04R0t2LVJLanZkaTlMbU1uTWIzcm1rIn0.B37o9mX52_ICjjp4e58MTrkP7EuPG5x-IG-BmawebZQs4SBEjH45aDkHT99OnRKNBccF_TT9ZjRkYJgglR7tk-_gNQXaZbhHfZyRFg59ytCn24Ke7AyDKgiNLTnoyP3EpAySpLsw3KFxGePlOKnHtoeykPdMea7rGb41jPZNi2tCFQzllyJapsvZ0cdSwxLkFzXEE2GcpbkzfbWhy2MAIh_btOxhIF0NglMXoxOVbZaTRQx7aKplSNl7U02bxKivSXzhqjV060ZFJr4hJonS225nGrm9Ns0vlkebPZPMMeAihc6pzbpyzcs9xpmhYiGZrv0uwa4MRe953YuSJEs6NoxWsRde10UtJAkkoBd5Qjbj_LPKIAzJVEgsdAXWfnZ1RE7RivGdxsiSW0zDgio5AnQZfXHDKYAH6wqGCd5OPO2UtJ6l3P39RSWFsBxD5LcgwOGSCFRH-3cSCMjJ53rH1ycZvQj_WXbS8RpYGmuOBY8UBbhhHBhwRhyP7pLOIMTl",
            "Origin": "https://app.brcapp.com",
            "Referer": "https://app.brcapp.com/",
            "Authorization": id_token
        }
    res = requests.post(
        url=url,
        data=payload,
        headers=headers
    );
    return res

def make_request(i):
    email = generate_random_string(20) + "@gmail.com"
    res = sign_up(email, generate_random_string(15))

    if res.status_code == 200:
        id_token = res.json().get("idToken")
        refRes = set_referred(id_token, "tmkha")
        if (refRes.status_code == 200):
            print(f"[{i}] OK", )
            return True
        else:
            print(f"[{i}] Error: ", refRes.json().get("error").get("message"))
            return False
    else:
        print(f"[{i}] Error: ", res.json().get("error").get("message"))
        return False


def run():
    with ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(make_request, range(18))