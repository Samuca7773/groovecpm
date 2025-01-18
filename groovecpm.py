import requests

BASE_URL: str = "https://Samuca007.pythonanywhere.com"

class GrooveCPM():
    def __init__(self, access_key: str) -> None:
        self.auth_token = None
        self.access_key = access_key
    
    def login(self, email: str, password: str, ip: str, region: str, country: str) -> int:
        payload = {
            "account_email": email,
            "account_password": password,
            "key": self.access_key,
            "ip": ip,
            "region": region,
            "country": country
        }
        response = requests.post(f"{BASE_URL}/account_login", json=payload)
        response_decoded = response.json()
        if response_decoded.get("success"):
            self.auth_token = response_decoded.get("auth")
            return response_decoded.get("message")
        return response_decoded.get("error")
    
    def get_player_data(self) -> any:
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/get_data", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return {
            "localid": response_decoded.get("localid"),
            "name": response_decoded.get("name"),
            "coin": response_decoded.get("coin"),
            "money": response_decoded.get("money"),
            "smoke": response_decoded.get("smoke"),
            "w16": response_decoded.get("w16"),
            "house": response_decoded.get("house"),
            "race_win": response_decoded.get("race_win"),
            "race_lose": response_decoded.get("race_lose")
        }
    
    def set_coin(self, amount: int):
        payload = { "auth": self.auth_token, "amount": amount, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_coin", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
        
    def set_money(self, amount: int):
        payload = { "auth": self.auth_token, "amount": amount, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_money", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def unlock_cosmetics(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_cosmetics", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def unlock_wheels(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_wheels", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def unlock_animations(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_animations", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def set_id(self, new_id: str):
        payload = { "auth": self.auth_token, "key": self.access_key, "id": new_id }
        response = requests.post(f"{BASE_URL}/set_id", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def set_name(self, new_name: str):
        payload = { "auth": self.auth_token, "key": self.access_key, "name": new_name }
        response = requests.post(f"{BASE_URL}/set_name", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
        
    def unlock_buzines(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_buzines", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def unlock_all_cars(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_all_cars", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def delete_account(self):
        payload = { "auth": self.auth_token, "key": self.access_key } 
        response = requests.post(f"{BASE_URL}/delete_account", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def unlock_smoke(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_smoke", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def unlock_w16(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_w16", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def unlock_house(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_house", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
        
    def delete_friends(self):
        payload = { "auth": self.auth_token, "key": self.access_key }
        response = requests.post(f"{BASE_URL}/delete_friends", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def set_race_win(self, amount: int):
        payload = { "auth": self.auth_token, "key": self.access_key, "amount": amount }
        response = requests.post(f"{BASE_URL}/set_race_win", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
    
    def set_race_lose(self, amount: int):
        payload = { "auth": self.auth_token, "key": self.access_key, "amount": amount }
        response = requests.post(f"{BASE_URL}/set_race_lose", json=payload)
        response_decoded = response.json()
        if response_decoded.get("error"):
            return response_decoded.get("error")
        return response_decoded.get("message")
