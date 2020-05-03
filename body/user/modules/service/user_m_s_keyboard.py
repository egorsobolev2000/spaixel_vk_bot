from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from .user_m_s_btns import *
from body.base_btn import KBB__BASE__MAIN_MENU


def service_keyboard():
    """ Функция создает клавиатуру
        для модуля УСЛУГИ """

    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(KBB__USER_M_SERVICE__SITE_DEVELOPMENT, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_SERVICE__CHATBOT_DEVELOPMENT, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_SERVICE__LOGO, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_SERVICE__DESIGN_VK_GROUPS, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__BASE__MAIN_MENU, color=VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()

