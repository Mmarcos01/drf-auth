#  Authentication & Production Server

## Feature Tasks and Requirements

- Features - Django
- Add JWT Authentication to API.
- Install needed libraries in project configuration and/or site settings.
- Keep any pre-existing authentication so DRF Browsable API still usable.
- Features - Docker
- Switch to using Gunicorn instead of Django’s built in development server.
- Handle static files using Whitenoise

## Auth Credentials Utilize HTTP requests

    brew install httpie
    within settings.py ALLOWED_HOSTS, add 'localhost'
    http POST :8000/api/token/ username='your username' password='your password'
    receive access and refresh keys.
    http :8000/api/albums/ 'Authorization: Bearer 'access key'
