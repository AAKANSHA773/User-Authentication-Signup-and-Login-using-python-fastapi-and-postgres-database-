from fastapi import FastAPI
import users.models as models
from core.database import engine
from users.routers import user_router, router as guest_router
from auth.route import auth_router
from starlette.middleware.authentication import AuthenticationMiddleware
from core.security import JWTAuth

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(guest_router)
app.include_router(user_router)
app.include_router(auth_router)

# add  middleware
app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())

@app.get('/')
async def hello():
    return {"message":"Hello World"}





