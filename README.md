1. create dir and clone git repo


2. Issues with virtualenv:
> pip install virtualenv
> 
> virtualenv venv
> 
> source venv/bin/activate
> 
> pip install -r requirements.txt

3. First Install and Test Redis:
> sudo apt-get update
> 
> sudo apt-get upgrade
> 
> sudo apt-get install redis-server
> 
> sudo service redis-server restart
> 
> redis-cli

4. Then srt runserver, celery beat and celery worker:
> python3 manage.py runserver
> 
> celery -A jokes_project beat -l INFO
> 
> celery -A jokes_project worker -l INFO