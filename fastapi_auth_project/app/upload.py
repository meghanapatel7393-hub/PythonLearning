import os
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.auth import create_access_token, verify_password
from app.config import settings
from jose import jwt, JWTError

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: int = int(payload.get("sub")) #payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/upload-image")
def upload_image(
    image: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not allowed_file(image.filename):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    file_path = os.path.join(settings.UPLOAD_FOLDER, image.filename)
    with open(file_path, "wb") as f:
        f.write(image.file.read())

    current_user.image = image.filename
    db.commit()
    return {"message": "Image uploaded successfully", "file": image.filename}

# import os
# from fastapi import APIRouter, UploadFile, File, Depends
# from app.auth import oauth2_scheme
# from fastapi.responses import JSONResponse

# router = APIRouter()
# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# @router.post("/upload-image")
# async def upload_image(
#     image: UploadFile = File(...),
#     token: str = Depends(oauth2_scheme)
# ):
#     file_path = os.path.join(UPLOAD_DIR, image.filename)

#     with open(file_path, "wb") as f:
#         f.write(await image.read())

#     return {"message": "Image uploaded successfully", "file": image.filename}
