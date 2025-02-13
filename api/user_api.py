import requests
from urls import API_URL


class UserApi:
    def registration(self, body):
        try:
            response = requests.post(f'{API_URL}/api/auth/register', data=body)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/auth/register: {e}')

    def delete(self, access_token):
        try:
            headers = {
                'Authorization': f'{access_token}'
            }
            response = requests.delete(f'{API_URL}/api/auth/user', headers=headers)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/auth/user: {e}')