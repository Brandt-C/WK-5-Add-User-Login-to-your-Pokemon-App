from flask import render_template, flash, redirect, url_for, request
from app.auth import auth
from app.auth.forms import SignUpForm, LoginForm
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User
from app import db

@auth.route('/')
def home():
    return render_template('base.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data),
                first_name=form.first_name.data,
                last_name=form.last_name.data)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You can now log in.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('signup.html', title='Sign Up', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.home')) 
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('auth.home')) 
        else:
            flash('Login failed. Please check your email and password.', 'danger')
    return render_template('login.html', title='Log In', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))