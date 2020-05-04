from body.user.modules.faq.user_m_f_keyboard import faq_keyboard
from brain.base import random_id
from debug.debug import log_error

from data.collect_data.vk_user import VkUser as User
from data.collect_data.data_collect import data_collector

from body.base_btn import KBB__BASE__MAIN_MENU
from body.user.modules.faq.user_m_f_btns import *
from body.user.modules.service.user_m_s_btns import *
from body.user.modules.menu.s_keyboard.user_m_m_s_btns import *


from data.modules_data.service.service_data import SERVICE_DATA
from data.modules_data.faq.faq_data import FAQ_DATA

from body.base import get_empty_keyboard
from body.user.modules.service.user_m_s_keyboard import service_keyboard
from body.user.modules.menu.s_keyboard.user_m_m_s_keyboard import standard_keyboard


@log_error
@data_collector
def main_user_handler(vk, event):
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

    # Если человек нажимает на кнопку -> УСЛУГИ
    elif event.text == KBB__USER_M_M__S_K__SERVICE:
        vk.messages.send(
            user_id=event.user_id,
            message='Список наших услуг появился внизу на клавиатуре.',
            random_id=random_id(),
            keyboard=get_empty_keyboard()

        )
        vk.messages.send(
            user_id=event.user_id,
            message='Нажимай на интересующую тебя услугу и я расскажу тебе о ней',
            random_id=random_id(),
            keyboard=service_keyboard()

        )

    # Если запрашивается любая из услуг
    elif event.text == KBB__USER_M_SERVICE__LOGO or \
            event.text == KBB__USER_M_SERVICE__SITE_DEVELOPMENT or \
            event.text == KBB__USER_M_SERVICE__CHATBOT_DEVELOPMENT or \
            event.text == KBB__USER_M_SERVICE__DESIGN_VK_GROUPS:

        vk.messages.send(
            user_id=event.user_id,
            message=SERVICE_DATA[event.text],
            random_id=random_id()
        )

    # Если человек нажимает на кнопку -> FAQ
    elif event.text == KBB__USER_M_M__S_K__FAQ:
        vk.messages.send(
            user_id=event.user_id,
            message='Если ты не сможешь найти здесь ответа на свой вопрос, '
                    'ты всегда можешь оставить нам заявку.',
            random_id=random_id(),
            keyboard=faq_keyboard()

        )

    # Если запрашивается любой из FAQ вопросов
    elif event.text == KBB__USER_M_FAQ__COST or \
            event.text == KBB__USER_M_FAQ__TIME or \
            event.text == KBB__USER_M_FAQ__HAVE_DESIGN or \
            event.text == KBB__USER_M_FAQ__EDITS or \
            event.text == KBB__USER_M_FAQ__PORTFOLIO:

        vk.messages.send(
            user_id=event.user_id,
            message=FAQ_DATA[event.text],
            random_id=random_id()
        )

    # Если человек нажимает на кнопку -> ГЛАВНОЕ МЕНЮ
    elif event.text == KBB__BASE__MAIN_MENU:
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

    # Если человек нажимает на кнопку -> ОТЗЫВЫ
    elif event.text == KBB__USER_M_M__S_K__REVIEWS:
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
