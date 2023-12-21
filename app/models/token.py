# from app import db
from app.extensions import db

class UserTokens(db.Document):
    
    meta = {'collection': 'tokens'}
    email = db.StringField(max_length=30)
    token = db.StringField()
    
    @staticmethod
    def getToken(email):
        return UserTokens.objects(email=email).first()
    
    @staticmethod 
    def createToken(email, token):
        userToken = UserTokens.getToken(email)
        if not userToken:
            userToken = UserTokens(email=email, token=token).save()
        return token  
