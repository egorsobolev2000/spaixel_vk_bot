import random
from debug.debug import log_error


@log_error
def random_id() -> object:
    """ Функция генерирует случайный id
        для отправки сообщения человеку """

    rand = 0
    rand += random.randint(0, 10000000000)
    return rand
