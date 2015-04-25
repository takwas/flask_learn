

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    #openid = StringField('openid', validators=[DataRequired()])
    username_fld = StringField('Username:  ', validators=[DataRequired()])
    password_fld = PasswordField('Password:  ', validators=[DataRequired()])
    remember_me_chkbx = BooleanField('Remember me', default=False)
    login_btn = SubmitField('Sign in!')



from wtforms import TextAreaField
class FeedPostForm(Form):
	title_fld = StringField('Post Title:   ', validators=[DataRequired()])
	content_fld = TextAreaField('Type your post here:   ', validators=[DataRequired()])
	post_btn = SubmitField('Post content!')