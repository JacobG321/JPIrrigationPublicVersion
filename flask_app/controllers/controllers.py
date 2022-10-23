
from flask_app import app
from flask import render_template, redirect, request
import smtplib, os
from email.message import EmailMessage
from flask_app.models.customers import Customer
from dotenv import load_dotenv

load_dotenv()
PASSCODE= os.getenv("passcode")
EMAIL=os.getenv("email")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about_us')
def about_us():
    return render_template('about.html')

@app.route('/terms_of_use')
def terms_of_use():
    return render_template('terms_of_use.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/get_a_quote')
def get_a_quote():
    return render_template('get_a_quote.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route("/contact_us", methods=['POST'])
def contact_us():
    user_data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'phone':request.form['phone'],
        'comments':request.form['comments'],
        'contact_method':request.form['contact_method']
    }

    if not Customer.new_quote_validation(user_data):
        return redirect(request.referrer)
    
    stringify_data = (
                        f'First name: {user_data["first_name"]}\n'
                        f'Last name: {user_data["last_name"]}\n'
                        f'Email: {user_data["email"]}\n'
                        f'Phone number: {user_data["phone"]}\n'
                        f'Comments: {user_data["comments"]}\n'
                        f'Preferred contact method: {user_data["contact_method"]}\n'
                        )

    # Customer.save_user(user_data)

    jpEmail = EMAIL

    msg = EmailMessage()
    msg.set_content(stringify_data)
    msg['Subject'] = f'{user_data["email"]}'
    msg['From'] = jpEmail
    msg['To'] = jpEmail

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(jpEmail, PASSCODE)
    server.send_message(msg)
    return redirect('/success')


# services
@app.route('/irrigation_estimates')
def irrigation_estimates():
    return render_template('irrigation_system_estimates.html')

@app.route('/lawn_aeration')
def lawn_aeration():
    return render_template('aeration.html')

@app.route('/dethatching')
def dethatching():
    return render_template('dethatching.html')

@app.route('/landscape_lighting')
def landscape_lighting():
    return render_template('landscape_lighting.html')

@app.route('/holiday_lights')
def holiday_lights():
    return render_template('holiday_lights.html')

@app.route('/pesticide_fertilizer')
def pesticide_fertilizer():
    return render_template('pesticide_fertilizer.html')

@app.route('/lawn_leveling')
def lawn_leveling():
    return render_template('lawn_leveling.html')
