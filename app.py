from flask import Flask, render_template, request, redirect, url_for, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config
import os

app = Flask(__name__)

# Define your products dictionary
products = {
    1: {
        'name': 'Driver Detection',
        'screenshots': ['screenshot1.jpg', 'screenshot2.jpg', 'screenshot3.jpg',],
        'short_description': 'AI-Powered Driver Tracking System with Face Recognition.',
        'description': 'Track your Drivers is appear on the allocated vehicle or not.',
        'price': 'Rs.5,000.00',
        'image_filename': 'dms_webinar.webp'  # Add the filename for the image
        
    },
    2: {
        'name': 'Attendance System',
        'short_description': 'AI-powered fully Automated Attendance system with Reports.',
        'description': 'Experience the power of Ai Attendance System using your existing CCtv cameras.',
        'price': 'Rs.7,500.00',
        'image_filename': 'ezgif.com-gif-maker-6.webp'  # Add the filename for the image
    },
    3: {
        'name': 'CCTV Tracker',
        'short_description': 'From now you Dont need to wasting your time for search a person .',
        'description': 'Welcome to the New Ai called CCtv Tracker, In the modern generation you dont need to wory about Time of Searching a person is arrive or appears on The footages, This Ai tool is automatically identify the faces from footages and live.',
        'Note': "This is a Tool and this only Runs on Windows Computers.",
        'price': 'Rs.7,500.00',
        'image_filename': 'The-AI-In-Security-Debate-What-Is-The-Future-For-CCTV-Monitoring.jpg'  # Add the filename for the image
    },
    4: {
        'name': 'Person Tracker',
        'short_description': 'Track the person with Email alerts with AI.',
        'description': 'This is the new way to Track the persons you want anytime automatically.',
        'price': 'Rs.7,500.00',
        'image_filename': '180725-facial-recognition-mn-1610.webp'  # Add the filename for the image
    }
    # Add more products as needed
}

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Check if the product_id exists in the dictionary
    if product_id in products:
        product = products[product_id]
        return render_template('product_detail.html', product=product)
    else:
        return 'Product not found'
def send_email_with_contact_details(product_name, full_name, phone_number, email):
    subject = f"Contact Form Submission - {product_name}"
    body = f"Product Name: {product_name}\nFull Name: {full_name}\nPhone Number: {phone_number}\nEmail: {email}"

    # Set your email server details
    email_host = 'smtp.gmail.com'
    email_port = 587  # Change this if your email provider uses a different port
    email_username = 'workpurposecolab@gmail.com'
    email_password = 'udsk xeww bpch ptpm'

    # Set sender and recipient email addresses
    sender_email = 'workpurposecolab@gmail.com'
    recipient_email = 'frndlyvijay@gmail.com'  # Replace with the recipient's email address

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the email server and send the email
    try:
        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()
            server.login(email_username, email_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        full_name = request.form['full_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        product_name = request.form['product_name']

        # Use the modified email function to send an email with contact details
        send_email_with_contact_details(product_name, full_name, phone_number, email)

        return jsonify({"message": "Contact form submitted successfully!", "product_name": product_name})


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
