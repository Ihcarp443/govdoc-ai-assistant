from fastapi import FastAPI
from api.export import router as export_router
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router as chat_router
from api.upload import router as upload_router
from db_repo.sqlite import init_db
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(export_router,prefix="",tags=["Export"])
app.include_router(chat_router, prefix="", tags=['Chat'])
app.include_router(upload_router, prefix="", tags=['Upload'])
init_db()