from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from .user_m_f_btns import *
from debug.debug import log_error


@log_error
def faq_keyboard():
    """ Функция создает клавиатуру
        для модуля FAQ """

    keyboard = VkKeyboard(one_time=False, inline=True)

    keyboard.add_button(KBB__USER_M_FAQ__TIME, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_FAQ__COST, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_FAQ__HAVE_DESIGN, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_FAQ__EDITS, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_FAQ__PORTFOLIO, color=VkKeyboardColor.DEFAULT)

    return keyboard.get_keyboard()

