import uvicorn
from fastapi import FastAPI

from apps.user.router import router as user_router

app = FastAPI()
app.include_router(user_router, prefix="/user")


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
