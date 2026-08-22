from fastapi import APIRouter


authRouter = APIRouter()


@authRouter.post("/login")
def login():
    return {"data":"login"}



@authRouter.post("/signup")
def signUp():
    return {"data":"signUp"}
