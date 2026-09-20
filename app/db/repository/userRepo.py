from .base import BaseRepository
from app.db.models.user import User
from app.db.schema.user import UserinCreate, UserInLogin


class UserRepository(BaseRepository):
    def create_user(self, user_data: UserinCreate):
        newUser = User(user_data.model_dump(exclude_none = True))
        self.session.add(newUser)
        self.sesion.commit()
        self.session.refresh(instance=newUser)
        return newUser

    def user_exist_by_email(self, email:str) -> bool:
        user = self.session.query(User).filter_by(email=email).first()
        return bool(user)

    def get_user_by_email(self, email:str) -> User:
        user = self.session.query(User).filter_by(email=email).first()
        return user

    def get_user_by_id(self, id:int) -> User:
        user = self.session.query(User).filter_by(id = id).first()
        return user



    

    