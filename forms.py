from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
from wtforms.validators import Required

class  ContactForm(Form):
  name = TextField("Name" , [validators.Required("please enter your name")])
  email = TextField("Email", [validators.Required("please enter your email address"), validators.Email()])
  subject = TextField("Subject", [validators.Required("please enter your subject")])
  message = TextAreaField("Message", [validators.Required("please enter your message")])
  submit = SubmitField("Send")