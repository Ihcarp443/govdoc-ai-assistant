from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db_repo.sqlite import get_db_connection
from services.auth import hash_password, verify_password

router=APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(req: LoginRequest):

    conn = get_db_connection()
    cursor = conn.cursor()

    user = cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (req.email,)
    ).fetchone()

    conn.close()

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    # user tuple: (id, full_name, email, password, created_at)
    if not verify_password(req.password, user[3]):
        raise HTTPException(status_code=400, detail="Invalid password")

    return {
        "success": True,
        "user": {
            "id": user[0],
            "email": user[2],
            "full_name": user[1]
        }
    }