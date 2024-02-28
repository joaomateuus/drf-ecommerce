import requests

class LoginScript:
    def __init__(self) -> None:
        self.base_url = 'http://localhost:8000'
        self.token_url = f'{self.base_url}/o/token/'
        self.username = ''
        self.password = ''
        self.client_id = ''
        self.client_secret = ''
        self.acess_token = None
        self.refresh_token = None
        
    def login(self):
        try:
            token_data = {
                "grant_type": "password",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "username": self.username,
                "password": self.password,
            }
            response = requests.post(self.token_url, token_data)

            if response.status_code == 200:
                response_json = response.json()
                self.acess_token = response_json.get('access_token')
                self.refresh_token = response_json.get('refresh_token')
                print('User logged sucessfully \n')
            else:
                raise Exception('Was not posible to log in into the api')
            
        except Exception as e:
            print(str(e))

instance = LoginScript()
instance.login()
print(f'Acess Token: {instance.acess_token}')
print(f'Refresh Token: {instance.refresh_token}')