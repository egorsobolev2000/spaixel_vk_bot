import os
import datetime

from brain.brain_base import random_id, check_email
from debug.debug import log_error
from data.collect_data.vk_user import VkUser as User
from data.ww_json.work_with_json import JSONFile
from body.user.modules.menu.s_keyboard.user_m_m_s_keyboard import standard_keyboard

from debug.debug import timeit


def create_user_log(user_info, user_name, msg, date):
    user_info.update({'message': []})
    user_info.update({'mail_count': []})
    user_info['message'] = msg
    JSONFile(f'./data/logs/{user_name}${date}.json', user_info)


def ww_logs(lst, filename, users=False, file=False):
    """ Внутренняя функция для работы со списком лог файлов
        Может вернуть:
        -> либо списков всех пользователей для
                которых был создан лог файл
        -> либо 1 конкрентый файл
    """
    users_list = []
    if users:
        for log in lst:
            users_list.append(log.split('$')[0])
        return users_list
    if file:
        for log in lst:
            if log.split('$')[0] == filename:
                return log


@log_error
def data_collector(f):
    """ Функция ДЕКОРАТОР-ПРОСЛУШАВАТЕЛЬ - собирает
        данные от пользователя"""

    def wrapper(vk, event):
        user_info = User(vk).get_user_info(event, return_user=True)
        user_name = f"{user_info['first_name']}_{user_info['last_name']}_{event.user_id}"
        date = datetime.datetime.today()
        msg = {f'{date.hour}:{date.minute}:{date.second}': event.text}
        if user_name not in ww_logs(os.listdir('./data/logs/'), user_name, users=True):
            create_user_log(user_info, user_name, msg, date)
            vk.messages.send(
                user_id=event.user_id,
                message=f'Привет, {user_info["first_name"]} 🖐🏿',
                random_id=random_id(),
                keyboard=standard_keyboard()
            )

            check_email(vk, event, 0, '')

        else:
            file = ww_logs(os.listdir('./data/logs/'), user_name, file=True)
            user_info = JSONFile(f'./data/logs/{file}', d_or_l='load')
            user_info['message'].update(msg)
            JSONFile(f'./data/logs/{file}', user_info)
        return f(vk, event)

    return wrapper
