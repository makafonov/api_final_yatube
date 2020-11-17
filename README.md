# api_final

REST API для социальной сети [yatube](https://github.com/makafonov/hw05_final).

## Running this project

Install the project dependencies with
```
pip install -r requirements.txt
```

Synchronize the database state with the current set of models and migrations. 
```
python manage.py migrate
```

Now you can run the project with this command
```
python manage.py runserver
```
