from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from .user_m_m_s_btns import *


def standard_keyboard():
    """ Функция создает стандарную
        клавиатуру бота """

    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(KBB__USER_M_M__S_K__SERVICE, color=VkKeyboardColor.DEFAULT)
    # keyboard.add_button(KBB__USER_M_M__S_K__FILL_BRIF, color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(KBB__USER_M_M__S_K__FAQ, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_openlink_button(KBB__USER_M_M__S_K__OPEN_WEBSAIT, 'https://spaixel.com/')

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_M__S_K__REVIEWS, color=VkKeyboardColor.PRIMARY)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_M__S_K__REQUEST, color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()

