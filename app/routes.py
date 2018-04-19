from flask import Flask, request, render_template, session, flash, redirect, url_for, jsonify
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from app import db
from app.forms import RegistrationForm
from flask_login import login_required
import os
from flask.ext.mail import Mail, Message
from celery import Celery

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page')

@app.route('/todo')
def todo():
	import sqlite3
	conn = sqlite3.connect('todo.db')
	cur = conn.cursor()
	cur.execute("SELECT * from todolist")
	data = cur.fetchall()
	return render_template('todo.html',data=data, title = "To Do")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('todo'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('todo')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


'''
CREATE TABLE `todolist` (
`id` int(11) NOT NULL,
`restaurant_name` varchar(128) DEFAULT NULL,
`location` varchar(128) DEFAULT NULL,
`zomato_rating` float(12) DEFAULT NULL,
`average_cost` double(10000) DEFAULT NULL,
PRIMARY KEY (`id`));

INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (1, 'Skky Ramada', 'Powai', 4.1, 3000 );
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (2, 'Bayview Cafe', 'Coloba', 3.7, 1200 );
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (3, 'Light House Cafe', 'Worli', 4.2, 1200 );
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (4, 'Imperial China', 'Chakala', 4.5, 3500 );
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (5, 'Tamasha', 'Lower Parel', 4.2, 1800 );
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (6, 'Ark - Deck Bar', 'Bandra', 4.0, 6000 );
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (7, 'Marina', 'Colaba', 3.5, 1600 );
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (8, 'SpiceKlub', 'Lower Parel', 4.5, 2100 );
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES(9,'Dome-InterContinental','Churgegate',4.1,3500);
INSERT INTO todolist(id,restaurant_name,location,zomato_rating,average_cost) VALUES (10, 'Aer - 4 seasons', 'Worli',4.3,4000);
'''
