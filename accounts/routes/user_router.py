from fastapi import APIRouter, HTTPException, Depends
from settings.config import supabase
from accounts.schemas.user_schemas import UserRegister, UserLogin

user_router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# User registration endpoint
@user_router.post("/register")
async def user_register(request: UserRegister):
    try:
        # Register the user with Supabase
        response = supabase.auth.sign_up(
            {
                "email": request.email,
                "password": request.password
            }
        )
        
        if response.user is None:
            raise HTTPException(status_code=400, detail="User registration failed")

        return {"message": "User registered successfully", "user_id": response.user.id}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@user_router.post("/login")
async def user_login(request: UserLogin):
    try:
        # Log in the user with Supabase
        response = supabase.auth.sign_in_with_password(
            {
                "email": request.email,
                "password": request.password
            }
        )

        if response.session is None or response.session.access_token is None:
            raise HTTPException(status_code=401, detail="Login failed")

        return {
            "message": "Login successful",
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))