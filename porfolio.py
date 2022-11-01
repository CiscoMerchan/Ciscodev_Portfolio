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

class AboutMe(FlaskForm):
    submit = SubmitField("My name is Franciscoelias ...")

"""About me Text"""
about_me = "My name is Franciscoelias, but everyone calls me Cisco. I entered the world of coding in 2021 with an online" \
           "with a Udemy course bla bla. Since then,I have become familiar with programs such as bla bla. I have created" \
           " some projects through my course, as well as individual projects that I have displayed on Github. I have also " \
           "joined a group called bla bla, where I have done a presentation of a step-by-step on how to create a log-in " \
           "bla bla for beginners.  Coding is a fascinating subject(?) for me, that I wish I found sooner. Being fluent " \
           "in english, spanish and french (and conversational in others), I can't help but draw similarites between " \
           "coding and learning a language, something I really enjoy. There is always something new to learn, and constant problem"\
            "solving are other aspects of coding that really appeal to me (just to name a few.\n"\
            "My previous work experience as a Scuba Diving Instructor, and a manager in hospitality have required of me " \
           "a high level of dedication and self-motivation,professional work etiquette, ability to work under pressure " \
           "and meet deadlines and a high level of communcation skill with people from all works of life."\
           "In my spare time you can find me sailing, or scuba diving, reading about history, and of course with my family."\
           "For more detail about my work experience, projects and skills, please follow the link to my Github and resume."\
            "Kind regards, Cisco"

testty= "<h1 class='helloh1'>vfvafvafvafvafvafva</h1>\n<br><h6>pararaeer</h6> "

send = SendEmail()
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY']='fgwfnbg bjiopnegpbniegpbuio npbnwbwbwgbetybnetyne'
@app.route('/', methods=['GET','POST'])
def home():
    about = AboutMe()
    if about.validate_on_submit():
        pass
    return render_template('home.html', about=about)

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
        flash('Thank you for interest, I will contact you ASAP!')
        return redirect(url_for('home'))
    return render_template('contact.html', form=form)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/portafolio')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)