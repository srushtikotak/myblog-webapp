## Web application developed using Python, Flask and Celery

### Screenshots of website:
1) index.html
![index](https://github.com/srushtikotak/myblog-webapp/blob/master/screenshots/index.png)

2) register.html
![register](https://github.com/srushtikotak/myblog-webapp/blob/master/screenshots/register.png)

3) login.html
![login](https://github.com/srushtikotak/myblog-webapp/blob/master/screenshots/log%20in.png)

4) todo.html
![todolist](https://github.com/srushtikotak/myblog-webapp/blob/master/screenshots/todo.png)

5) send_mail.html
![mail](https://github.com/srushtikotak/myblog-webapp/blob/master/screenshots/email.png)

6) gmail
![received mail](https://github.com/srushtikotak/myblog-webapp/blob/master/screenshots/received_mail.png)

7) Home.html
![home](https://github.com/srushtikotak/myblog-webapp/blob/master/screenshots/home.png)

### Steps:
1. Create a virtal environment using python3 : 
    
    $ virtualenv -p python3 myenv
2. Activate it:
    
    $ source myenv/bin/activate
3. Install all the required libraries using :
    
    (myenv)$ pip install <file-name>
4. Open Terminal 1: 
    
    (myenv)$ redis-server
5. Open Terminal 2 : 
    
    $ export MAIL_USERNAME=<your-gmail-username>
    
    $ export MAIL_PASSWORD=<your-gmail-password>
    
    $ source bin/activate
    
    (venv) $ celery worker -A app.celery --loglevel=info
6. Open Terminal 3:   
    
    $ source myenv/bin/activate
    
    (myenv) $ export FLASK_APP=myblog.py
    
    (myenv) $ flask run
7. Now navigate to http://localhost:5000/ in your web browser and try !

PS : todo.db was create using sqlite3 and the query is added as comment in routes.py

### References(Follow the refernces for a detailed tutorial):
1. [Using Celery With Flask](https://blog.miguelgrinberg.com/post/using-celery-with-flask)
2. [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
