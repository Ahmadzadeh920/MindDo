from os import access
import jwt
import uuid
from datetime import timedelta, datetime
from typing import Dict, Any, Optional
from infrastructure.config.settings import settings

from domain.interfaces.jwt_provider import IJWTProvider

class JWTManager(IJWTProvider):
    def __init__(self):
        self.secret = settings.JWT_SECRET_KEY
        self.algoritm = settings.JWT_ALGORITHM


    def create_access_token(self,user_id):
        now = datetime.now()
        expired = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_MINUTES)
        jti = str(uuid.uuid4)
        payload = {
            "subject": user_id,
            "iat":now,
            "exp": expired,
            "jti": jti
        }
        
        access_token = jwt.encode(payload, self.secret, algorithm=self.algoritm)
        return access_token
    

    def create_refresh_token(self, user_id):
        now = datetime.now()
        expired = now + timedelta(days=settings.REFRESH_TOKEN_EXPIRES_DAYS)
        jti = str(uuid.uuid4)
        payload = {
            "subject": user_id,
            "iat":now,
            "exp": expired,
            "jti": jti
        }
        
        refresh_token = jwt.encode(payload, self.secret, algorithm=self.algoritm)
        return refresh_token
    
    def verify_token(token):
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
            return payload
        except jwt.ExpiredSignatureError:
            raise "This token is Expired"
        except jwt.InvalidTokenError:
            raise "Invalid Token"
