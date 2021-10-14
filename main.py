from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired, Email
import datetime
import smtplib


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Length(min=2)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    message = TextAreaField(label='Message', render_kw={"rows": 8}, validators=[DataRequired()])
    submit = SubmitField('Send ↲')


year = datetime.datetime.today().year
app = Flask(__name__)
bootstrap = Bootstrap(app)


# TODO 1. Move this to sys/os before deploying
app.secret_key = "pG^9KsXeg!LS9l*7s%Y8v90@N7wbIKoh"
EMAIL = "joseph.table.k@outlook.com"
MY_EMAIL = "zohrlaffz@gmail.com"
PASSWORD = "c|10WKtCx"
#############


def send_email(name, email, message):
    with smtplib.SMTP("smtp.live.com:587") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Contact Message!\n\nFrom: {name}\nEmail: {email}\n \n{message}"
        )
    return True


@app.route('/')
def main():
    return render_template("index.html", year=year)


@app.route('/projects')
def projects():
    return render_template("projects.html", year=year)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    alert = None
    form = ContactForm()
    if form.validate_on_submit():
        if send_email(name=form.name.data, email=form.email.data, message=form.message.data):
            flash("Your message was sent successfully!")
            return redirect(url_for('contact'))
    else:
        alert = "Please fill out the entire form!"
    return render_template("contact.html", year=year, form=form, alert=alert)


if __name__ == "__main__":
    app.run(debug=True)
