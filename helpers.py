import uuid


BASE_URL = "https://qa-desk.education-services.ru/"

class EmailGenerator:
    def __get__(self, obj, objtype=None):
        _uid = uuid.uuid4().hex
        return _uid[:7] + '@' + _uid[-7:] + '.' + 'com'


class Helpers():
    password = "Password$123"
    invalid_email = "invalid_email.com"
    random_email = EmailGenerator()
    new_advert_name = "Прекрасное объявление"
    new_advert_description = "Описание Прекрасного объявления"
    new_advert_price = 123
