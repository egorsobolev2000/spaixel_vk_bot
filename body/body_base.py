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


def send_transitional_msg(vk, event, keyboard):
    """ Функция автоматизирует переход между
        режимами и смену клавиатуры """

    vk.messages.send(
        user_id=event.user_id,
        message='Возврат в главное меню',
        random_id=random_id(),
        keyboard=get_empty_keyboard()
    )

    vk.messages.send(
        user_id=event.user_id,
        message='Что будем делать?',
        random_id=random_id(),
        keyboard=keyboard()

    )

