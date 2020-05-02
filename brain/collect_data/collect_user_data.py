import requests, fake_useragent
from bs4 import BeautifulSoup
from debug.debug import log_error, timeit


class VkUser:
    def __init__(self, vk):
        self.vk = vk
        self.user_agent = fake_useragent.UserAgent()
        self.user = str(self.user_agent.random)
        self.headers = {
            'User-Agent': f'{self.user}',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US',
        }

    def get_user_name(self, event):
        """ Функция получает имя пользователя """
        # {'id': 441335448, 'first_name': 'Name', 'last_name': 'Surname', 'is_closed': False, 'can_access_closed':
        # True}
        user = self.vk.users.get(user_ids=event.user_id)[0]
        first_name: object = user["first_name"]
        return first_name
