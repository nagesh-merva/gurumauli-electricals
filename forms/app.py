from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

def send_email(name, email, subject, message):
    receiving_email_address = 'portfolionagesh.1957@gmail.com'

    try:
        msg = EmailMessage()
        msg.set_content(f"From: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

        msg['Subject'] = f"New contact form submission: {subject}"
        msg['From'] = email
        msg['To'] = receiving_email_address

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('portfolionagesh.1957@gmail.com', 'qlqy eoda vftd mtkx')
            server.send_message(msg)

        return jsonify({'message': 'Form submitted successfully and email sent'}), 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'message': 'Error sending email'}), 500

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    location = request.form.get('message')
    project_details = request.form.get('message')
    service = request.form.get('message')  # Modify as needed to get the correct field name
    service_type = request.form.get('service_type')

    materials = []
    quantities = []
    for i in range(1, 13):
        material = request.form.get(f'material{i}')
        quantity = request.form.get(f'quantity{i}')
        if material and quantity:
            materials.append(material)
            quantities.append(quantity)

    message = f"Location: {location}\nProject Details: {project_details}\nService: {service}\nMaterials Needed:\n"
    for material, quantity in zip(materials, quantities):
        message += f"{material}: {quantity}\n"

    # Additional information: service type
    message += f"Service Type: {service_type}\n"

    return send_email(name, email, subject, message)

if __name__ == '__main__':
    app.run(debug=True)


