source venv/bin/actvate
python3 -m pip install -r requirements.txt
django-admin startproject etale .
python3 ./manage.py makemigrations blog
python3 ./manage.py migrate
