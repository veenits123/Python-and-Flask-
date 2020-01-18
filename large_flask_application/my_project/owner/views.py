from flask import Blueprint,render_template,redirect,url_for
from my_project import db
from my_project.models import Owner
from my_project.owner.forms import AddForm

owners_blueprint = Blueprint('owner',
                              __name__,
                              template_folder='templates/owner')

@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html',form=form)