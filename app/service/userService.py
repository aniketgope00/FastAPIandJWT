from app.db.repository.userRepo import UserRepository
from app.db.schema.user import UserOutput, UserInCreate, UserInLogin, UserInToken

from app.core.security.hashHelper import HashHelper
from app.core.securityauthHandler import AuthHandler

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException



class UserService:
    def __init__(self, session: Session):
        self.__userRepository = UserRepository(session)


    def signup(self, user_details : UserInCreate) -> UserOutput:
        if self.__userRepository.user_exist_by_email(user_details.email):
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = HashHelper.get_password_hash(plain_password=user_details.password)
        user_details.password = hashed_password
        return self.__userRepository.create_user(user_data = user_details)


    def login(self, login_details: UserInLogin) -> UserWithToken:
        if not self.__userRepository.user_exist_by_email(email = login_details.email):
            raise HTTPException(status_code=400, detail="Invalid email or password/Please create an account")

        user = self.__userRepository.get_user_by_email(email = login_details.email)
        if HashHelper.verify_password(plain_password=login_details.password, hashed_password=user.password):
            token = AuthHandler.encode_token(user_id=user.id)
            if token:
                return UserWithToken(user=user, token=token)
            raise HTTPException(status_code=500, detail="Token generation failed")
        raise HTTPException(status_code=400, detail="Invalid email or password/Please check credentials")