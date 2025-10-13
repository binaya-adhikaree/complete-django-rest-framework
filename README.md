Django User Authentication & Account Management API

This is a Django REST API for user registration, email verification, password reset, login, logout, profile management, and password change. It uses Django REST Framework and Simple JWT for authentication.

Features

User Registration

Users can register with email and password.

Verification email is sent upon registration.

Email verification is required to activate the account.

Email Verification

Users click the email verification link to verify their email.

JWT tokens are used to securely verify the email.

Login

Users can log in with email and password.

JWT access and refresh tokens are returned for authenticated requests.

Logout

Users can logout and blacklist the refresh token.

Password Reset

Request password reset via email.

Reset link with token is sent to the user's email.

Users can set a new password using the link.

Change Password

Authenticated users can change their password by providing their current password.

User Profile

Authenticated users can view and update their profile.

Tech Stack

Backend: Django, Django REST Framework

Authentication: Simple JWT

Email: Django's built-in email system (SMTP)

Token Handling: itsdangerous for password reset tokens

Installation

Clone the repository:

git clone https://github.com/binaya-adhikaree/complete-django-rest-framework.git
cd folder name where you have cloned this repo


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Set up .env or settings.py for your email and secret key:

# Example for settings.py
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
SECRET_KEY = 'your-secret-key'


Run migrations:

python manage.py migrate


Start the server:

python manage.py runserver

API Endpoints
Method	Endpoint	Description	Permissions
POST	/api/v1/register/	Register a new user	Public
GET	/api/v1/verify-email/?token=<token>	Verify email	Public
POST	/api/v1/login/	Obtain JWT tokens	Public
POST	/api/v1/token/refresh/	Refresh JWT token	Public
POST	/api/v1/logout/	Logout user	Authenticated
POST	/api/v1/password-reset/	Request password reset	Public
POST	/api/v1/reset-password/<token>/	Confirm password reset	Public
POST	/api/v1/change-password/	Change password	Authenticated
GET/PUT	/api/v1/profile/	Retrieve or update user profile	Authenticated
Example Usage
Register
POST /api/v1/register/
{
    "email": "test@example.com",
    "password": "password123"
}

Login
POST /api/v1/login/
{
    "email": "test@example.com",
    "password": "password123"
}

Request Password Reset
POST /api/v1/password-reset/
{
    "email": "test@example.com"
}

Reset Password
POST /api/v1/reset-password/<token>/
{
    "password": "newpassword123"
}

Change Password
POST /api/v1/change-password/
{
    "old_password": "password123",
    "new_password": "newpassword123"
}

Notes

All endpoints under /api/v1/ are prefixed for versioning.

Password reset tokens expire in 1 hour.

Make sure email settings are configured correctly for sending verification and reset emails.
