# Module containing view functions

from flask import render_template, flash, redirect, url_for, session
from application import app
from forms import LoginForm, FeedPostForm


@app.route('/')
@app.route('/index')
def index():
	# |go to home page;		|response-status-code:200 by default
	return render_template('index.html', username = session.get('username'))


# a custom user-page
@app.route('/user/<name>')
def profile(name=''):
	name = session.get('username')
	# go to custom user page
	return render_template('user.html', username = name)


@app.route('/login', methods=['GET', 'POST'])
def auth():
	form = LoginForm()

	if form.validate_on_submit():

		if form.password_fld.data == 'entry':									# Validate correctness of password; dumb procedure though, but should suffice
			session['username'] = form.username_fld.data
			form.username_fld.data = ''											# clear username data
			form.password_fld.data = ''											# clear password data

			flash("User '%s' has req login;    Remember_me=%s" %(session['username'], str(form.remember_me_chkbx.data)))


			return redirect(url_for('profile', name = session['username']))
		
		else:
			flash('You may have entered the wrong password! Try again')
	#end: if form.validate_on_submit()

	else:	# clear credentials
		session.pop('username', '')


	return render_template('auth.html', username = session.get('username'), form = form)


@app.route('/feeds', methods=['GET', 'POST'])
def feeds():
	form = FeedPostForm()
	items = {0: ("Default Post", "This is a default feed post that appears on every page. Nothing interesting.")}																	#list of feed items from db


	if form.validate_on_submit():
		flash('Posting new feed')
		#add content to db

		return redirect(url_for('feeds'), feeds_dict = items, username = session.get('username'), post_form = form)

	return render_template('feeds.html', feeds_dict = items, username = session.get('username'), post_form = form)