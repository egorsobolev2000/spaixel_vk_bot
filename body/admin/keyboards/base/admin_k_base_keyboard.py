from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from .admin_k_base_btns import *
from body.base_btn import KBB__BASE__EXIT

from debug.debug import log_error


@log_error
def admin_base_keyboard():
    """ Функция создает клавиатуру
        для модуля ADMIN """

    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(KBB__ADMIN_B__USER_LIST, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__ADMIN_B__ADMIN_LIST, color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(KBB__ADMIN_B__ADD_ADMIN, color=VkKeyboardColor.POSITIVE)
    keyboard.add_button(KBB__ADMIN_B__DEL_ADMIN, color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button(KBB__ADMIN_B__MAILING_USER_LIST, color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(KBB__ADMIN_B__ADD_MAILING_USER, color=VkKeyboardColor.POSITIVE)
    keyboard.add_button(KBB__ADMIN_B__DEL_MAILING_USER, color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button(KBB__BASE__EXIT, color=VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()

