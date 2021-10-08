from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import datetime


class ContactForm(FlaskForm):
    name = StringField(label='name', validators=[DataRequired()])
    email = StringField(label='email', validators=[DataRequired(), Email()])
    message = StringField(label='message', validators=[DataRequired()])
    submit = SubmitField('Submit')


year = datetime.datetime.today().year
app = Flask(__name__)
# TODO 1. Move key to sys/os before deploying
app.secret_key = "pG^9KsXeg!LS9l*7s%Y8v90@N7wbIKoh"


@app.route('/')
def main():
    return render_template("index.html", year=year)


@app.route('/projects')
def projects():
    return render_template("projects.html", year=year)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    # TODO 2. Fix contact form submission
    if form.validate_on_submit():
        print(form.name.data, form.email.data, form.message.data)
    return render_template("contact.html", year=year, form=form)


if __name__ == "__main__":
    app.run(debug=True)
