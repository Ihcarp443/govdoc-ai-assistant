from fastapi import FastAPI
from api.export import router as export_router
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router as chat_router
from api.upload import router as upload_router
from api.threads import router as threads_router
from db_repo.sqlite import init_db
from api.documents import router as document_router
from api.login import router as login_router
from api.signup import router as signup_router
from api.downloadfile import router as download_router
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
app.include_router(export_router,prefix="/report",tags=["Export"])
app.include_router(chat_router, prefix="", tags=['Chat'])
app.include_router(upload_router, prefix="", tags=['Upload'])
app.include_router(threads_router, tags=['Thread'])
app.include_router(document_router, prefix="/documents", tags=["Documents"])
app.include_router(login_router, prefix="/auth", tags=["login"])
app.include_router(signup_router, prefix="/auth", tags=["signup"])

app.include_router(download_router, prefix="", tags=["Download"])
init_db()