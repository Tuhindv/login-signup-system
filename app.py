
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import bcrypt
import json
import os


# =========================================================
# FastAPI App
# =========================================================

app = FastAPI()


# =========================================================
# Templates
# =========================================================

templates = Jinja2Templates(directory="templates")


# =========================================================
# Static Files
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# =========================================================
# Users JSON File
# =========================================================

USERS_FILE = "users.json"


def load_users():

    if not os.path.exists(USERS_FILE):
        return []

    with open(
        USERS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_users(users):

    with open(
        USERS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            users,
            file,
            indent=4
        )


# =========================================================
# Home / Login Page
# =========================================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


# =========================================================
# Signup Page
# =========================================================

@app.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="signup.html",
        context={}
    )


# =========================================================
# Signup
# =========================================================

@app.post("/signup")
def signup(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):

    users = load_users()


    # =====================================================
    # Check Password
    # =====================================================

    if password != confirm_password:

        return RedirectResponse(
            "/signup?error=password",
            status_code=303
        )


    # =====================================================
    # Check Existing Email
    # =====================================================

    for user in users:

        if user["email"] == email:

            return RedirectResponse(
                "/signup?error=exists",
                status_code=303
            )


    # =====================================================
    # Hash Password
    # =====================================================

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


    # =====================================================
    # Create New User
    # =====================================================

    new_user = {

        "id": len(users) + 1,

        "name": name,

        "email": email,

        "password": hashed_password
    }


    # =====================================================
    # Save User
    # =====================================================

    users.append(new_user)

    save_users(users)


    # =====================================================
    # Redirect To Login
    # =====================================================

    return RedirectResponse(
        "/?success=signup",
        status_code=303
    )


# =========================================================
# Login
# =========================================================

@app.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...)
):

    users = load_users()


    # =====================================================
    # Find User
    # =====================================================

    for user in users:

        if user["email"] == email:


            # =================================================
            # Verify Password
            # =================================================

            password_correct = bcrypt.checkpw(
                password.encode("utf-8"),
                user["password"].encode("utf-8")
            )


            # =================================================
            # Login Successful
            # =================================================

            if password_correct:

                response = RedirectResponse(
                    "/gallery",
                    status_code=303
                )


                # =============================================
                # Save Login Cookie
                # =============================================

                response.set_cookie(
                    key="user_email",
                    value=email,
                    httponly=True
                )


                return response


    # =====================================================
    # Invalid Login
    # =====================================================

    return RedirectResponse(
        "/?error=invalid",
        status_code=303
    )


# =========================================================
# Gallery
# =========================================================

@app.get("/gallery", response_class=HTMLResponse)
def gallery(request: Request):


    # =====================================================
    # Get User Email From Cookie
    # =====================================================

    email = request.cookies.get("user_email")


    # =====================================================
    # User Not Logged In
    # =====================================================

    if not email:

        return RedirectResponse(
            "/",
            status_code=303
        )


    # =====================================================
    # Load Users
    # =====================================================

    users = load_users()

    current_user = None


    # =====================================================
    # Find Current User
    # =====================================================

    for user in users:

        if user["email"] == email:

            current_user = user

            break


    # =====================================================
    # User Not Found
    # =====================================================

    if not current_user:

        return RedirectResponse(
            "/",
            status_code=303
        )


    # =====================================================
    # Get Images From static/images
    # =====================================================

    image_folder = "static/images"

    images = []


    if os.path.exists(image_folder):

        for filename in os.listdir(image_folder):

            if filename.lower().endswith(
                (
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".gif",
                    ".webp"
                )
            ):

                images.append(filename)


    # =====================================================
    # Gallery Page
    # =====================================================

    return templates.TemplateResponse(
        request=request,
        name="gallery.html",
        context={
            "user": current_user,
            "images": images
        }
    )


# =========================================================
# Logout
# =========================================================

@app.get("/logout")
def logout():

    response = RedirectResponse(
        "/",
        status_code=303
    )


    # =====================================================
    # Delete Login Cookie
    # =====================================================

    response.delete_cookie(
        "user_email"
    )


    return response

