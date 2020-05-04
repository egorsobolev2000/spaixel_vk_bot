class VkUser:
    """ Класс для работы с объектом Пользователь"""

    def __init__(self, vk):
        self.vk = vk

    def get_user_info(self, event, field=False, return_user=False):
        """ Функция получает информацию о пользователе и возвращает
            либо конкретное поле, либо весь словарь пользователя """

        user = self.vk.users.get(user_ids=event.user_id,
                                 fields='verified, sex, bdate, city, country,'
                                        'domain, contacts, site,'
                                        'counters, relation, connections')[0]

        if field:
            need_field: object = user[field]
            return need_field
        if return_user:
            return user

