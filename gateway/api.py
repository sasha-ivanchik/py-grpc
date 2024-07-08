from fastapi import FastAPI

from routes.item import router as item_router
from routes.auth import router as auth_router

app = FastAPI()
app.include_router(item_router)
app.include_router(auth_router)
