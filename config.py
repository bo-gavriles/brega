import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///leads.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Redis (for caching and rate limiting)
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    
    # Formspree
    FORMSPREE_WEBHOOK_SECRET = os.environ.get('FORMSPREE_WEBHOOK_SECRET')
    
    # Payment systems
    YOOKASSA_SHOP_ID = os.environ.get('YOOKASSA_SHOP_ID')
    YOOKASSA_SECRET_KEY = os.environ.get('YOOKASSA_SECRET_KEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
    STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET')
    
    # Email
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    
    # Lead settings
    LEAD_EXPIRY_HOURS = 24
    BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')
    
    # Country settings
    COUNTRY_CONFIG = {
        'RU': {
            'name': 'Russia',
            'currency': 'RUB',
            'payment_systems': ['yookassa', 'cloudpayments', 'tinkoff'],
            'recipients': ['sales_ru@example.com', 'manager_ru@example.com']
        },
        'US': {
            'name': 'United States',
            'currency': 'USD',
            'payment_systems': ['stripe', 'paypal'],
            'recipients': ['sales_us@example.com']
        },
        # ... other countries
    }
