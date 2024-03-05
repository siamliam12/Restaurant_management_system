from passlib.context import CryptContext

SPECIAL_CHARACTER = ['!','@','#','$','%','^','&','*','~','/','>','<','?']
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def check_password_strength(password:str)->bool:
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in SPECIAL_CHARACTER for char in password):
        return False
    return True