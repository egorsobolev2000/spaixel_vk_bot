import random

from body.base import get_empty_keyboard
from body.user.modules.service.user_m_s_keyboard import service_keyboard
from debug.debug import log_error
from data.collect_data.vk_user import VkUser as User
from data.collect_data.data_collect import data_collector

from body.user.modules.menu.s_keyboard.user_m_m_s_keyboard import standard_keyboard


@log_error
def random_id() -> object:
    """ Функция генерирует случайный id
        для отправки сообщения человеку """

    rand = 0
    rand += random.randint(0, 10000000000)
    return rand


@log_error
@data_collector
def main_handler(vk, event):
    """ ГЛАВНАЯ Функция обработчик всех
        входящих событий и сообщений """

    if event.text == 'Начать' or event.text.lower() == 'привет':
        vk.messages.send(
            user_id=event.user_id,
            message=f'Привет, {User(vk).get_user_info(event, "first_name")} 🖐🏿\n\n'
                    f'Я есть Дред.\n'
                    f'Чем я могу тебе помочь?',
            random_id=random_id(),
            keyboard=standard_keyboard()
        )

    elif event.text == 'Услуги':
        vk.messages.send(
            user_id=event.user_id,
            message='Список наших услуг появился на клавиатуре',
            random_id=random_id(),
            keyboard=get_empty_keyboard()

        )
        vk.messages.send(
            user_id=event.user_id,
            message='Нажимай на интересующую тебя услугу и я расскажу о ней',
            random_id=random_id(),
            keyboard=service_keyboard()

        )

    elif event.text == 'Главное меню':
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
            keyboard=standard_keyboard()

        )


    elif event.text == 'Отзывы':
        vk.messages.send(
            user_id=event.user_id,
            message='👇🏿 Наши отзывы 👇🏿',
            random_id=random_id()
        )

        vk.messages.send(
            user_id=event.user_id,
            message='https://vk.com/topic-157919190_41216100',
            random_id=random_id()
        )
