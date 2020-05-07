import os

from brain.brain_base import random_id

from body.base_btn import KBB__BASE__EXIT
from body.admin.keyboards.base.admin_k_base_btns import *

from body.body_base import send_transitional_msg

from body.user.modules.menu.s_keyboard.user_m_m_s_keyboard import standard_keyboard

from data.ww_json.work_with_json import JSONFile


def send__add_del__msg(vk, event, command):
    vk.messages.send(
        user_id=event.user_id,
        message='Хорошо, пришли мне сообщение в таком формате:\n\n'
                f'{command} user_id',
        random_id=random_id()
    )


def add_user(vk, event, path, user, w):
    file = JSONFile(path, d_or_l='load')
    if user not in file['users']:
        file['users'].append(user)
        JSONFile(path, file)
        vk.messages.send(
            user_id=event.user_id,
            message='Добавил. Этот пользователь теперь имеет'
                    f' права {w}',
            random_id=random_id()
        )

    else:
        vk.messages.send(
            user_id=event.user_id,
            message='Пользователь уже имеет '
                    f'права {w}',
            random_id=random_id()
        )


def del_user(vk, event, path, user, w):
    file = JSONFile(path, d_or_l='load')
    try:
        file['users'].remove(user)
        JSONFile(path, file)
        vk.messages.send(
            user_id=event.user_id,
            message='Удалил. Этот пользователь больше не имеет'
                    f' прав {w}',
            random_id=random_id()
        )
    except ValueError:
        vk.messages.send(
            user_id=event.user_id,
            message=f'Пользователь не имеет прав {w}',
            random_id=random_id()
        )


def main_admin_handler(vk, event):
    """ Функция обработчик всех
        входящих событий и сообщений в режиме АДМИНА """

    if event.text == KBB__BASE__EXIT:
        admin_file = JSONFile(f'./brain/admin/admin.json', d_or_l='load')
        admin_file['status'] = "OFF"
        JSONFile(f'./brain/admin/admin.json', admin_file)
        send_transitional_msg(vk, event, standard_keyboard)

    elif event.text == KBB__ADMIN_B__USER_LIST:
        logs = os.listdir('./data/logs/')

        user_list = []
        user_str = ''

        for file in logs:
            user_file = JSONFile(f'./data/logs/{file}', d_or_l='load')
            user_list.append([user_file['id'], f'{user_file["first_name"]} {user_file["last_name"]}'])

        for i, u in enumerate(user_list, 1):
            user_str += f'{i}. @id{u[0]}({u[1]})\n'

        vk.messages.send(
            user_id=event.user_id,
            message='Список пользователей\n\n'
                    f'{user_str}',
            random_id=random_id()
        )

    elif event.text == KBB__ADMIN_B__ADMIN_LIST:
        user_str = ''
        admin_file = JSONFile(f'./brain/admin/admin.json', d_or_l='load')
        for u in admin_file['users']:
            user_str += f'https://vk.com/id{u}\n'

        vk.messages.send(
            user_id=event.user_id,
            message='Список админов\n\n'
                    f'{user_str}',
            random_id=random_id()
        )

    elif event.text == KBB__ADMIN_B__ADD_ADMIN:
        send__add_del__msg(vk, event, '$admin')
    elif event.text == KBB__ADMIN_B__DEL_ADMIN:
        send__add_del__msg(vk, event, '$deladmin')

    elif event.text == KBB__ADMIN_B__ADD_MAILING_USER:
        send__add_del__msg(vk, event, '$manager')
    elif event.text == KBB__ADMIN_B__DEL_MAILING_USER:
        send__add_del__msg(vk, event, '$delmanager')

    elif event.text[0] == "$":
        msg = event.text.split()

        if len(msg) > 1:
            if msg[0][1:] == 'admin':
                add_user(vk, event, './brain/admin/admin.json', msg[1], 'администратора')
            if msg[0][1:] == 'manager':
                add_user(vk, event, './brain/mailing/mailing.json', msg[1], 'менеджера')

            if msg[0][1:] == 'delmanager':
                del_user(vk, event, './brain/mailing/mailing.json', msg[1], 'менеджера')
            if msg[0][1:] == 'deladmin':
                del_user(vk, event, './brain/admin/admin.json', msg[1], 'администратора')









