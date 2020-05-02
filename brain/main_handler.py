import random

from vk_api.longpoll import VkEventType

from debug.color import ColorsPrint
from debug.debug import log_error

from .collect_data.collect_user_data import VkUser as User


@log_error
def random_id():
    """ Функция генерирует случайный id
        для отправки сообщения человеку """

    rand = 0
    rand += random.randint(0, 10000000000)
    return rand


@log_error
def main_handler(vk, longpoll):
    """ ГЛАВНАЯ Функция обработчик всех
        входящих событий и сообщений """

    print(f'\nСоединение с Дред — ', ColorsPrint('OK', 'suc').do_colored())

    for event in longpoll.listen():
        # event.text == 'hi
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            vk.messages.send(
                user_id=event.user_id,
                message=f'Привет {User(vk).get_user_name(event)} 👋\n'
                        f'Я есть Дред. Чем я могу тебе помочь?',
                random_id=random_id()
            )
