Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Fake database
events = [
    {'id': 1, 'name': 'OK-NGL Meetup', 'date': '2025-03-15', 'capacity': 10, 'registrations': []},
]

def send_email(to_email, event_name):
    sender_email = "your_generic_email@example.com"
...     subject = "Potvrzení rezervace"
...     body = f"Děkujeme za rezervaci na akci: {event_name}. Těšíme se na vás!"
...     
...     msg = MIMEMultipart()
...     msg['From'] = sender_email
...     msg['To'] = to_email
...     msg['Subject'] = subject
...     msg.attach(MIMEText(body, 'plain'))
...     
...     try:
...         server = smtplib.SMTP('smtp.example.com', 587)
...         server.starttls()
...         server.login("your_generic_email@example.com", "yourpassword")
...         server.sendmail(sender_email, to_email, msg.as_string())
...         server.quit()
...     except Exception as e:
...         print(f"Error sending email: {e}")
... 
... @app.route('/')
... def index():
...     return render_template('index.html', events=events)
... 
... @app.route('/register/<int:event_id>', methods=['POST'])
... def register(event_id):
...     name = request.form['name']
...     email = request.form['email']
...     
...     event = next((e for e in events if e['id'] == event_id), None)
...     if event and len(event['registrations']) < event['capacity']:
...         event['registrations'].append({'name': name, 'email': email})
...         send_email(email, event['name'])
...         flash('Rezervace byla úspěšná! Zkontrolujte svůj e-mail.', 'success')
...     else:
...         flash('Akce je již plně obsazena.', 'danger')
...     
...     return redirect(url_for('index'))
... 
... if __name__ == '__main__':
...     app.run(debug=True)
