# Flask practice application


############################################################################################################
# Do imports

from flask import Flask, request, make_response, redirect, render_template, flash, session, url_for


############################################################################################################
# app instance
app = Flask(__name__)

#Cross Site Request Forgery - CSRF ... key for encryption of requests
app.config['SECRET_KEY'] = 'ac3takwas'				# This encryption string should be hard-to-guess
app.secret_key = 'ac3takwas'

############################################################################################################
# import and activate extensions

from flask.ext.script import Manager				# enable command-line interaction (cmd arg parsing) using extension
app_mang = Manager(app)								# run prog with this object instead

from flask.ext.bootstrap import Bootstrap			# enable bootstrap templates using extension
bootstrap = Bootstrap(app)



############################################################################################################
# general attribs...

# generate an HTML page using the template
# and passing in the given string
def gen_html(content=";) :) ;-D"):

	# basic HTML template
	base_html = "<html> <!--\
		--><head> <!--\
		--><title>Ac3 Flask App</title><!--\
		--><!--\
		--></head><!--\
		--><body><!--\
		--><div id='content'><!--BEGIN--> <!--END--></div><!--\
		--></body><!--\
		--><!--\
		--></html>"

	# partition base html for insertion
	part = base_html.rpartition("<!--BEGIN--> <!--END-->")
	
	# return newly formed string of html doc
	return "".join((part[0], content, part[2]))


############################################################################################################
# View functions...

# to default page
@app.route('/')
def index():
	# |go to home page;		|response-status-code:200 by default
	return render_template('index.html')


# a custom user-page
@app.route('/user/<name>')
def profile(name='Anonymous'):
	# go to custom user page
	return render_template('user.html', username=name)


# a login page
@app.route('/login')
def auth():
	# go to login page
	return render_template('login.html')



# a redirect view function
@app.route('/page_2')
def page_2():
	# The redirect function takes a redirect URL and response-status-code:302
	return redirect('redir', 302)


# a redirect-page
@app.route('/redir')
def redir():
	response = make_response(gen_html('<h2>oOh-0oh!!!</h2> <br/></h3>You have been redirected here.</h3>'), 200)
	return response


# an abort view function
@app.route('/user/<username>')
def error(username):
	user = load_user(username)		### need to confirm where to get load_user function
	if not user:
		# abort takes error-code:404
		abort(404)
	# else
	return profile(user)


############################################################################################################
# Form view funtions

@app.route('/form_test', methods=['GET', 'POST'])
def form_test():
	print 'in form_test page'									#DEBUG
	flash('This is a flash message!')
	form = LoginForm(csrf_enabled=False)
	print 'got here!'									#DEBUG
	print form.errors

	#if form.validate_on_submit():
	if request == 'POST':
		print form.errors
		print 'form submitted'									#DEBUG
		flash('Clicked Login!')
		if form.password.data == 'entry':						# validate password; wrong way, but would suffice for now
			flash('Now logging you in...')
			print 'pwd valid'									#DEBUG
			session['username'] = form.username.data
			#return redirect(url_for('profile'), name=session['username'])
			return redirect(url_for('index'))
		else:
			flash('It appears you have entered an incorrect password. Try again')
			print 'It appears you have entered an incorrect password. Try again'

	return render_template('form_test.html', form=form)



############################################################################################################
# Error page handling

# handles invalid url entries;		| status code for invalid/unknown URL error: 404
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


# handles unhandled exceptions (#noPunIntended)		| status code for unhandled excetion error: 500
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500



############################################################################################################
# Form data handling
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required


# This class is named LoginForm
class LoginForm(Form):		# create a form that extends the imported 'Form' class

	# class attributes...
	username = StringField('Username:     ', validators=[Required()])				#The 'Required' validator endures that this field is not left empty
	password = PasswordField('Password:     ', validators=[Required()])
	login = SubmitField('Login')



# run the program
if __name__ == '__main__':
	app_mang.run()