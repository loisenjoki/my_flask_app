from flask import Flask, render_template, flash
from forms import ContactForm
from flask import Flask, request
from flask.ext.mail import Message, Mail

mail = Mail()
	
app = Flask(__name__)   

app.secret_key = 'development key1'  

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'your_email@example.com'
app.config["MAIL_PASSWORD"] = 'password'
	
mail.init_app(app)
	
@app.route('/')
def home():
		return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
	form = ContactForm()
	if request.method =='POST':
		if form.validate() == False:
				flash('All fields are required.')
				return render_template('contact.html', form=form)
		else:
							msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
							msg.body = """
							From: %s <%s>
							%s
							""" % (form.name.data, form.email.data, form.message.data)
							mail.send(msg)
		
							return render_template('contact.html', success=True)

	elif request.method =='GET':
		return render_template('contact.html', form=form)
	
if __name__ == '__main__':
		app.run(debug=True)