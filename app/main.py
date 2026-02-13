from app.core.lifespan import lifespan
from fastapi import FastAPI

from app.api.calls import router as calls_router
from app.api.auth import router as auth_router

app = FastAPI(
    title="CallStream API",
    description="Система обработки событий телефонии Asterisk",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(calls_router, prefix="/api")
app.include_router(auth_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Service is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
