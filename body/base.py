from vk_api.keyboard import VkKeyboard


def get_empty_keyboard():
    keyboard = VkKeyboard(one_time=False)
    return keyboard.get_empty_keyboard()
