from app.models.user import User
from app.config.security import hash_password,check_password_strength
from fastapi import HTTPException

async def create_user_account(data,session):
    user_exist = session.query(User).filter(User.email==data.email).first()
    if user_exist:
        raise HTTPException(status_code=400,detail="Email Already Exists")
    
    if not check_password_strength(data.password):
        raise HTTPException(status_code=400,detail="Password is weak")
    user = User()
    user.name= data.name
    user.email = data.email
    user.password = hash_password(data.password)
    user.is_active = False
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
