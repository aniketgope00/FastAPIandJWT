from fastapi import APIRouter
from app.db.schema.user import UserInCreate, UserInLogin


authRouter = APIRouter()


@authRouter.post("/login")
def login(loginDetails: UserInLogin):
    return {"data":loginDetails}



@authRouter.post("/signup")
def signUp(signupDetails: UserInCreate):
    return {"data":signupDetails}
