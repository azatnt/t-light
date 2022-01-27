# t-light
1. Clone project
2. Commands:
    1. create virtual environment
    2. pip3 install -r requirements.txt
    3. python3 manage.py runserver
3. If you want to create new fake data in database
    1. Delete db.sqlite3
    2. Commands:
        1. python3 manage.py migrate
        2. python3 manage.py seeding (to fill database with fake datas,  if you want to change amount of data open main/management/seeding.py and set quantity to each model)
        3. python3 manage.py runserver
4. Routes:
    1. clients - list of all clients in database
    2. legal_entity - list of all legal_entity(Юр. лица) with departments
    3. department - list of all departments with clients
