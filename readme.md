Тестовое для "ООО АйТи Мегастар"
==================

Запуск:
------------------
1. Запустить сервер с PostgreSQL 
2. Склонировать данный репозиторий
3. Указать в файле .env необходимые настройки для подключения к БД:
```
Сервер
Логин
Пароль
Порт
Название БД
``` 
4. Дать права файлу на исполнение:
```
chmod 777 ./start.sh  
``` 
5. Запустить:
```
./start.sh init
``` 

Данный скрипт может выполняться с флагами
------------------
* init - накатить миграции и добавить данные в БД
* start - запустить сервис (если миграции уже были сделаны и данные есть в БД)
* stop - остановить сервис

Примеры команд:
------------------
```
 ./start.sh init    
 ./start.sh start  
 ./start.sh stop
 ``` 

Информация для get запроса находится по url:
------------------
```
http://127.0.0.1:8000/writers/<id_author>/
``` 

***Тестовое было выполнено за два часа***
