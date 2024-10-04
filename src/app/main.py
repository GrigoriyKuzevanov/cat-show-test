from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.core.config import settings
from src.app.routes import breeds_router, kittens_router


app = FastAPI(
    title="Cat show API",
    description="Test task for WorkMate company",
    contact={
        "name": "Grigoriy Kuzevanov",
        "email": "grkuzevanov@gmail.com",
        "url": "https://github.com/GrigoriyKuzevanov",
    },
)


if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(breeds_router)
app.include_router(kittens_router)
