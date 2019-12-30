from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    mylist=[1,2,3,4,5]
    # Pass in a puppy name
    # We insert it to the html with jinja2 templates!
    return render_template('home.html',mylist=mylist)

@app.route('/puppy/<name>')
def puppy_name(name):
    # Pass in a puppy name
    # We insert it to the html with jinja2 templates!
    return render_template('puppy.html',name=name)

@app.route('/advpuppy/<name>')
def adv_puppy_name(name):
    letters = list(name)
    pup_dict = {'pup_name':name}
    return render_template('temp0.html',
                           name=name,mylist=letters,mydict=pup_dict)


if __name__ == '__main__':
    app.run(debug=True)