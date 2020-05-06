import random
import datetime
from debug.debug import log_error
from brain.post.ww_post import send
from data.collect_data.vk_user import VkUser as User
from data.ww_json.work_with_json import JSONFile

from debug.debug import timeit

@log_error
def random_id() -> object:
    """ Функция генерирует случайный id
        для отправки сообщения человеку """

    rand = 0
    rand += random.randint(0, 10000000000)
    return rand


@log_error
@timeit
def check_email(vk, event, subject, body):
    first_name = User(vk).get_user_info(event, "first_name")
    last_name = User(vk).get_user_info(event, "last_name")
    username: str = f'{first_name} {last_name}'
    user_id: int = User(vk).get_user_info(event, "id")
    date = datetime.datetime.today()
    ids = JSONFile(f'./brain/post/mail_check.json', d_or_l='load')

    if subject == 0:
        send(subject, username, user_id, body)

    elif subject == 1:
        if str(user_id) not in ids.keys():
            vk.messages.send(
                user_id=event.user_id,
                message='Отправляю заявку ... 💬',
                random_id=random_id()
            )
            send(subject, username, user_id, body)
            ids.update({user_id: [f'{date.day}', 1]})
            JSONFile(f'./brain/post/mail_check.json', ids)

            vk.messages.send(
                user_id=event.user_id,
                message='Заявка успешно отправленна ✅',
                random_id=random_id()
            )

        elif ids[str(user_id)][0] != str(date.day):
            vk.messages.send(
                user_id=event.user_id,
                message='Отправляю заявку ... 💬',
                random_id=random_id()
            )
            send(subject, username, user_id, body)
            ids[str(user_id)][0] = str(date.day)
            JSONFile(f'./brain/post/mail_check.json', ids)

            vk.messages.send(
                user_id=event.user_id,
                message='Заявка успешно отправленна ✅',
                random_id=random_id()
            )

        else:
            vk.messages.send(
                user_id=event.user_id,
                message='ТЫ уже оставлял заявку сегодня',
                random_id=random_id()
            )
