import os
from datetime import datetime, timedelta
import jwt

# Key for jwt
SECRET_KEY = os.getenv('SECRET_KEY')


# Create Token Function
def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expira em 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def validate_date_format(date):
    formato_esperado = "%Y-%m-%d"

    try:
        datetime.strptime(date, formato_esperado)
        return True
    except ValueError:
        return False
