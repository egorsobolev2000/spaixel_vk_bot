from vk_api.keyboard import VkKeyboard
from brain.brain_base import random_id


def get_empty_keyboard():
    """ Функция удаляет текущую клавиатуру """
    keyboard = VkKeyboard(one_time=False)
    return keyboard.get_empty_keyboard()


def send_data_message(vk, event, data_set):
    """ Функция отправляет пользователю нужный ответ
        из набора относительно его запроса """
    vk.messages.send(
        user_id=event.user_id,
        message=data_set[event.text],
        random_id=random_id()
    )

