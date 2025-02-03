# Feito por t.me/Samuca_007
import requests

BASE_URL: str = "https://groovecpm-api.onrender.com"

class GrooveCPM:
    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
        
    def login(self, email: str, password: str):
        payload = { "email": email, "password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/login", json=payload, params=params)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
        
    def get_player_data(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/get_player_data", json=payload, params=params)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            return response_decoded
        return response_decoded.get("error")
    
    def get_key_data(self):
        params = { "key": self.access_key }
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            return response_decoded
        return response_decoded.get("error")
        
    def delete(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/delete", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
    
    def set_player_rank(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_player_rank", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def set_coin(self, amount: int):
        payload = { "auth": self.auth_token, "amount": amount}
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_coin", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def set_money(self, amount: int):
        payload = { "auth": self.auth_token, "amount": amount}
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_money", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def set_name(self, new_name: str):
        payload = { "auth": self.auth_token, "new_name": new_name}
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_name", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def set_name_rainbow(self, new_name: str):
        payload = { "auth": self.auth_token, "new_name": new_name}
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_name_rainbow", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
        
    def set_id(self, new_id: str):
        payload = { "auth": self.auth_token, "new_id": new_id}
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_id", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def unlock_all_cosmetics(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_all_cosmetics", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def unlock_all_animations(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_all_animations", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
         
    def delete_friends(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/delete_friends", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def unlock_w16(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_w16", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
    
    def unlock_wheels(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_wheels", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
        
    def unlock_horns(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_horns", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def disable_engine_damage(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/disable_engine_damage", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def unlimited_fuel(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlimited_fuel", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def delete_friends(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/delete_friends", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def set_race_win(self, amount: int):
        payload = { "auth": self.auth_token, "amount": amount }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_race_win", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
         
    def set_race_lose(self, amount: int):
        payload = { "auth": self.auth_token, "amount": amount }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_race_lose", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
         
    def unlock_house(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_house", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def unlock_smoke(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_smoke", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def unlock_all_cars(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_all_cars", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
    
    def unlock_all_paid_cars(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_all_paid_cars", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
        
    def unlock_all_cars_sirens(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_all_cars_sirens", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def unlock_all_levels(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_all_levels", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
     
    def reset_all_levels(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/reset_all_levels", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
         
    def clone_cars(self, email: str, password: str):
        payload = { "auth": self.auth_token, "email": email, "password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/clone_cars", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
    
    def remove_front_parts(self, car_id: str):
        payload = { "auth": self.auth_token, "id": car_id }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/remove_front_parts", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
    
    def remove_back_parts(self, car_id: str):
        payload = { "auth": self.auth_token, "id": car_id }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/remove_back_parts", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
    
    def all_cars_max_mileage(self):
        payload = { "auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/all_cars_max_milleage", json=payload, params=params)
        response_decoded = response.json()
        return response_decoded.get("message")
        