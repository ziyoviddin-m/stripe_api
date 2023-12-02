Тестовое задание: https://docs.google.com/document/d/1X8yV7jAZWZWhy3NG3m_Yi8lW4Bfa6ZNGDx95pHkE_qc/edit#heading=h.qn8kbnfz56hc

Проект доступен на удаленном сервере:

Для получения session.id - https://stripeapitest.pythonanywhere.com/buy/1 

Информация о выбранном Item и кнопка Buy - https://stripeapitest.pythonanywhere.com/item/1

Модель Order - https://stripeapitest.pythonanywhere.com/order-create/

Установка:
1) git clone https://github.com/ziyoviddin-m/stripe_api.git

2) python -m venv venv

3) .\venv\Scripts\activate

4) cd stripe_api

5) pip install -r requirements.txt

6) cd store

7) python manage.py runserver

9) Админ панель

логин: admin

пароль: 1234

Сделанные бонусные задачи:
· 	Использование environment variables
· 	Просмотр Django Моделей в Django Admin панели
· 	Запуск приложения на удаленном сервере, доступном для тестирования
· 	Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
