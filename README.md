# Тестовое задание для TeamUp
Используя Python 3.10 написть приложение на версии Django 3.2 и Django DRF (любой версии), в качестве пакетного менеджера использовать poetry.
Бизнес требования:
Для тестируемых существуют специальные секретные ключи по которым можно пройти 2 теста. Один из них это IQ второй EQ. В конце тестирования можно посмотреть свои результаты.
Нужно реализовать следующие ручки
Создание теста При вызове этой ручки создается тест с уникальным логином (набор букв в 10 знаков) который будет возвращен в ответе и его можно будет использовать для прохождения теста.
Сохранить результаты теста IQ и время когда он был пройден Передаются набранные баллы от 0 до 50 и логин теста к которому нужно это прикрепить
Сохранить результаты теста EQ и время когда был пройден Передается упорядоченный список букв (размером в 5 элемента) из набора set(а, б, в, г, д)
Можно посмотреть текущий результат прохождения по заданному тесту Передается логин, в ответе получаю результаты 2 тестов (кол-во баллов, упорядоченный список букв которые ввел пользователь, время прохождения каждого теста и логин)


Install dependencies with poetry:
```
poetry init
poetry install
```
and activate venv:
```
poetry shell
```


Rename .env.sample to .env:
```
DEBUG=True
SECRET_KEY=your_secret_key
DJANGO_SETTINGS_MODULE=config.settings.local
```