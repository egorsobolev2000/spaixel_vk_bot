import os
import vk_api

from config import TOKEN

from vk_api.longpoll import VkLongPoll, VkEventType

from brain.user.main_user_handler import main_user_handler
from debug.color import ColorsPrint

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


if __name__ == "__main__":
    while True:
        os.system('clear')
        print(ColorsPrint('Запускаем бота...', 'att').do_colored())
        try:
            print(f'\nСоединение с Дред — ', ColorsPrint('OK', 'suc').do_colored())
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    main_user_handler(vk, event)
        except Exception as e:
            print(ColorsPrint('Не удалось запустить бота', 'err').do_colored(), e)
        except KeyboardInterrupt:
            print(ColorsPrint('\n\nЗавершение соединения с ботом...', 'inf').do_colored())
            break



