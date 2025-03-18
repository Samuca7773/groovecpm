
import requests

BASE_URL: str = "https://groovecpm.squareweb.app"

class GrooveCPM:
    def __init__(self, access_key):
        self.auth_token = None
        self.access_key = access_key
    
    def res(self, endpoint, json):
        try:
            response = requests.post(
                url=f"{BASE_URL}/{endpoint}",
                params={"key": self.access_key},
                json=json
            )
            response_decoded = response.json()
            if response.status_code != 200:
                return {
                    "error": True,
                    "message": f"{response_decoded.get('message', 'INDEFINIDO')}"
                }
            return response_decoded
        except requests.exceptions.RequestException as err:
            return {
                "error": True,
                "message": f"ERRO DE CONEXÃO"
            }
        except ValueError:
            return {
                "error": True,
                "message": "ERRO AO DECODIFICAR JSON"
            }
            
    def auth(self, email, password):
        payload = {
            "email": email,
            "password": password    
        }
        response = self.res(
            endpoint="auth",
            json=payload
        )
        if response.get("auth"):
            self.auth_token = response.get('auth')
        return response
    
    def delete_account(self):
        return self.res("delete_account", {"auth": self.auth_token})
    
    def get_player_data(self):
        return self.res("get_player_data", {"auth": self.auth_token})

    def get_key_data(self):
        return self.res("get_key_data", {"auth": self.auth_token})

    def set_player_rank(self):
        return self.res("set_player_rank", {"auth": self.auth_token})
        
    def set_player_coin(self, amount):
        return self.res("set_player_coin", {"auth": self.auth_token, "amount": amount})
        
    def set_player_money(self, amount):
        return self.res("set_player_money", {"auth": self.auth_token, "amount": amount})
        
    def set_player_id(self, new_id):
        return self.res("set_player_id", {"auth": self.auth_token, "new_id": new_id})
    
    def set_player_name(self, new_name):
        return self.res("set_player_name", {"auth": self.auth_token, "new_name": new_name})
        
    def delete_friends(self):
        return self.res("delete_friends", {"auth": self.auth_token})

    def unlock_w16(self):
        return self.res("unlock_w16", {"auth": self.auth_token})

    def unlock_horns(self):
        return self.res("unlock_horns", {"auth": self.auth_token})

    def unlimited_fuel(self):
        return self.res("unlimited_fuel", {"auth": self.auth_token})
    
    def disable_engine_damage(self):
        return self.res("disable_engine_damage", {"auth": self.auth_token})
    
    def unlock_wheels(self):
        return self.res("unlock_wheels", {"auth": self.auth_token})
   
    def unlock_animations(self):
        return self.res("unlock_animations", {"auth": self.auth_token})
   
    def unlock_cosmetics(self):
        return self.res("unlock_cosmetics", {"auth": self.auth_token})
           
    def set_races_wins(self, amount):
        return self.res("set_races_wins", {"auth": self.auth_token, "amount": amount})
        
    def set_races_loses(self, amount):
        return self.res("set_races_loses", {"auth": self.auth_token, "amount": amount})

    def unlock_house(self):
        return self.res("unlock_house", {"auth": self.auth_token})

    def unlock_smoke(self):
        return self.res("unlock_smoke", {"auth": self.auth_token})

    def unlock_paid_cars(self):
        return self.res("unlock_paid_cars", {"auth": self.auth_token})
    
    def unlock_all_cars(self):
        return self.res("unlock_all_cars", {"auth": self.auth_token})
        
    def unlock_car_id(self, car_id):
        return self.res("unlock_car_id", {"auth": self.auth_token, "car_id": car_id})
        
    def unlock_all_cars_sirens(self):
        return self.res("unlock_all_cars_sirens", {"auth": self.auth_token})
    
    def unlock_siren_id(self, car_id):
        return self.res("unlock_siren_id", {"auth": self.auth_token, "car_id": car_id})
    
    def complete_all_levels(self):
        return self.res("complete_all_levels", {"auth": self.auth_token})
    
    def reset_all_levels(self):
        return self.res("reset_all_levels", {"auth": self.auth_token})
    
    def set_torque(self, car_id, new_torque):
        return self.res("set_torque", {"auth": self.auth_token, "car_id": car_id, "new_torque": new_torque})
    
    def remove_front_part(self, car_id):
        return self.res('remove_front_part', {"auth": self.auth_token, "car_id": car_id})
    
    def remove_back_part(self, car_id):
        return self.res("remove_back_part", {"auth": self.auth_token, "car_id": car_id})
    
    def unlock_all_cars_max_milleage(self):
        return self.res("unlock_all_cars_max_milleage", {"auth": self.auth_token})
    
    def unlock_car_id_max_milleage(self, car_id):
        return self.res("unlock_car_id_max_milleage", {'auth': self.auth_token, "car_id": car_id})
            
    def clone_cars(self, email, password):
        payload = {
            "auth": self.auth_token,
            "email": email,
            "password": password
        }
        return self.res("clone_cars", payload)