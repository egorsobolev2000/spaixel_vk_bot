from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from .user_m_s_btns import *


def service_keyboard():
    """ Функция создает стандарную
        клавиатуру бота """

    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button(KBB__USER_M_SERVICE__SITE_DEVELOPMENT, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_SERVICE__CHATBOT_DEVELOPMENT, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_SERVICE__LOGO, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_SERVICE__DESIGN_VK_GROUPS, color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button(KBB__USER_M_SERVICE__MAIN_MENU, color=VkKeyboardColor.DEFAULT)

    return keyboard.get_keyboard()

