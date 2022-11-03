from flask import Flask, redirect,render_template, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,TelField,EmailField
from wtforms.validators import DataRequired, length
from sendemail import SendEmail
class Contactform(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email Address',validators=[DataRequired()])
    phone = TelField('Phone Number')
    message = TextAreaField('Message', validators=[DataRequired(), length(max=400)])
    submit = SubmitField('Send')

send = SendEmail()
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY']='fgwfnbg bjiopnegpbniegpbuio npbnwbwbwgbetybnetyne'
@app.route('/', methods=['GET','POST'])
def home():

    return render_template('home.html')

@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')
@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = Contactform()

    if form.validate_on_submit():
        send.send(form.name.data, form.email.data, form.phone.data ,form.message.data)
        if form.submit.data:
            flash('Thank you for interest, I will contact you ASAP!')
            return redirect(url_for('home'))
    return render_template('contact.html', form=form)

@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug=True)