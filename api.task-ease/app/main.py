from fastapi import FastAPI
from app.api.routes.users import router as users_router
from app.db.session import engine
from app.db.models import Base

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

app.include_router(users_router, prefix='/api')


@app.get('/')
def read_root():
    return {"message": "Hello, FastAPI!"}
