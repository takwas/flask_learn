# Module that initialises and runs the app


from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


from application import views


from flask.ext.script import Manager				# enable command-line interaction (cmd arg parsing) using extension
app_mang = Manager(app)								# run prog with this object instead


from flask.ext.bootstrap import Bootstrap			# enable bootstrap templates using extension
bootstrap = Bootstrap(app)
 

# run the program
if __name__ == '__main__':
	app_mang.run()
