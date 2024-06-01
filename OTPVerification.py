import random
import smtplib
from email.mime.text import MIMEText
import PySimpleGUI as sg

# Function to generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP to the user's email
def send_otp(email, otp):
    sender_email = "pskreddy028@gmail.com"  # Replace with your email address
    sender_password = "qjyh vcrq nnqr plcr"  # Replace with your email passkey

    message = MIMEText(f"Your OTP is: {otp}")
    message['Subject'] = 'OTP Verification'
    message['From'] = sender_email
    message['To'] = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Using Gmail SMTP server
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("OTP sent successfully to your email.")
    except Exception as e:
        print("Error sending email:", e)

# Function to prompt user for email input using GUI
def prompt_for_email_gui():
    layout = [
        [sg.Text('Please enter your email address:')],
        [sg.InputText(key='-EMAIL-')],
        [sg.Button('Send OTP')]
    ]

    window = sg.Window('Email Verification', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
            return None
        elif event == 'Send OTP':
            window.close()
            return values['-EMAIL-']

# Function to prompt user for OTP input using GUI
def prompt_for_otp_gui():
    layout = [
        [sg.Text('Please enter the OTP received in your email:')],
        [sg.InputText(key='-OTP-')],
        [sg.Button('Verify')]
    ]

    window = sg.Window('OTP Verification', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
            return None
        elif event == 'Verify':
            window.close()
            return values['-OTP-']

# Function to verify if entered OTP matches the generated OTP
def verify_otp(entered_otp, generated_otp):
    return entered_otp == generated_otp

# Main function
def main():
    # Prompt user for email
    user_email = prompt_for_email_gui()
    if user_email is None:
        print("Email verification canceled.")
        return

    # Generate OTP
    otp = generate_otp()

    # Send OTP to user's email
    send_otp(user_email, otp)

    # Prompt user for OTP input using GUI
    entered_otp = prompt_for_otp_gui()
    if entered_otp is None:
        print("OTP verification canceled.")
        return

    # Verify OTP
    if verify_otp(entered_otp, otp):
        print("OTP verification successful!")
    else:
        print("Invalid OTP.")

if __name__ == "__main__":
    main()
