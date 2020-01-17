from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField('Add Puppy')


class AddOwner(FlaskForm):

	name= StringField('Name of the Owner')
	id =IntegerField('id of the puppy for owner')
	submit=SubmitField('AddOwner')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')
