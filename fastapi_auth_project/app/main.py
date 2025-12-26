from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.models import User
from app.schemas import UserCreate, UserOut
from app.auth import hash_password, verify_password, create_access_token
from app.upload import router as upload_router
from app.schemas import LoginSchema
app = FastAPI(title="FastAPI Auth System")

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "FastAPI Auth System Running 🚀"}

# //here we can  register with body row in postman
@app.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# here we can login with body - x-www-form-urlencoded in postman
# username bhavesh@example.com
# password Bhavesh
# response
# {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImV4cCI6MTc2Njc0MTg1M30.ff6D47BzWG8E7KQS78qa3aDcdlVy_BBXyduXThVtn_E",
#     "token_type": "bearer"
# }
#content-type in header- application/x-www-form-urlencoded
# NOW BOTH WAY LOGIN WORK
@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form.username).first()
    if not user or not verify_password(form.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # token = create_access_token({"sub": user.id})
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

# Include upload router
app.include_router(upload_router)

# If you want JSON login instead of form-data, change your login API like this 👇
# ✅ Fixed Login API (JSON Based)
# class LoginSchema(BaseModel):
#     email: str
#     password: str

#content type in header application/json
@app.post("/login1")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}


# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.database import Base, engine, get_db
# from app import models
# from app.schemas import UserCreate, UserOut
# from app.auth import create_access_token, hash_password, verify_password
# from app.upload import router as upload_router

# app = FastAPI(title="FastAPI Auth System")

# # Create tables
# models.Base.metadata.create_all(bind=engine)

# # Include upload router
# app.include_router(upload_router)

# # ---------------- HOME
# @app.get("/")
# def home():
#     return {"message": "FastAPI Auth System Running 🚀"}

# # ---------------- REGISTER
# @app.post("/register", response_model=UserOut)
# def register(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(models.User).filter(models.User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
    
#     new_user = models.User(
#         name=user.name,
#         email=user.email,
#         password=hash_password(user.password)
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# # ---------------- LOGIN
# @app.post("/login")
# def login(form: UserCreate, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == form.email).first()
#     if not user or not verify_password(form.password, user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     token = create_access_token({"sub": str(user.id)})
#     return {"access_token": token, "token_type": "bearer"}





# from fastapi import FastAPI, Depends
# from app.database import Base, engine
# from app import models
# from app.auth import create_access_token, hash_password, verify_password
# from app.upload import router as upload_router
# from fastapi.security import OAuth2PasswordRequestForm



# app = FastAPI(title="FastAPI Auth System")

# models.Base.metadata.create_all(bind=engine)

# @app.get("/")
# def home():
#     return {"message": "FastAPI Auth System Running 🚀"}

# @app.post("/register")
# def register(form: OAuth2PasswordRequestForm = Depends()):
#     return {"msg": "User registered"}

# @app.post("/login")
# def login(form: OAuth2PasswordRequestForm = Depends()):
#     token = create_access_token({"sub": form.username})
#     return {"access_token": token, "token_type": "bearer"}

# app.include_router(upload_router)
