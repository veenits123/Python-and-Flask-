from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

	name= StringField('Name of the Owner')
	id =IntegerField('id of the puppy for owner')
	submit=SubmitField('AddOwner')