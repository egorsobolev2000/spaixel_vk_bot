import os
import vk_api

from config import TOKEN

from vk_api.longpoll import VkLongPoll

from brain.main_handler import main_handler
from debug.color import ColorsPrint

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


if __name__ == "__main__":
    while True:
        os.system('clear')
        print(ColorsPrint('Запускаем бота...', 'att').do_colored())
        try:
            main_handler(vk, longpoll)
        except Exception as e:
            print(ColorsPrint('Не удалось запустить бота', 'err').do_colored(), e)
            raise e
        except KeyboardInterrupt:
            print(ColorsPrint('\n\nЗавершение соединения с ботом...', 'inf').do_colored())
            break



