import requests
from urls import API_URL



class OrderApi:
    def get_ingredients(self):
        try:
            response = requests.get(f'{API_URL}/api/ingredients')
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/ingredients: {e}')

    def create_order(self, access_token, ingredients):
        try:
            headers = {
                'Authorization': f'{access_token}'
            }
            ingredients_json = {
                'ingredients': ingredients
            }
            response = requests.post(f'{API_URL}/api/orders', headers=headers, json=ingredients_json)
            return response
        except Exception as e:
            print(f'Ошибка при запросе /api/orders: {e}')