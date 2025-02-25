import os

# Define project structure
project_structure = [
    "app/api/routes",
    "app/core",
    "app/db",
    "app/schemas",
    "app/services",
    "tests"
]

# Define files with initial content
files = {
    "app/main.py": "from fastapi import FastAPI\nfrom app.api.routes.users import router as users_router\n\napp = FastAPI()\n\napp.include_router(users_router, prefix='/api')\n\n@app.get('/')\ndef read_root():\n    return {\"message\": \"Hello, FastAPI!\"}\n",
    "app/api/routes/__init__.py": "",
    "app/api/routes/users.py": "from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get('/users')\ndef get_users():\n    return {\"users\": [{\"id\": 1, \"name\": \"John Doe\"}]}\n",
    "app/core/__init__.py": "",
    "app/core/config.py": "from pydantic import BaseSettings\n\nclass Settings(BaseSettings):\n    DATABASE_URL: str\n    SECRET_KEY: str\n\n    class Config:\n        env_file = \".env\"\n\nsettings = Settings()\n",
    "app/db/__init__.py": "",
    "app/db/session.py": "from sqlalchemy import create_engine\nfrom sqlalchemy.orm import sessionmaker\nfrom app.core.config import settings\n\nengine = create_engine(settings.DATABASE_URL)\nSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\n",
    "app/schemas/__init__.py": "",
    "app/schemas/user.py": "from pydantic import BaseModel, EmailStr\n\nclass UserCreate(BaseModel):\n    email: EmailStr\n    password: str\n",
    "app/services/__init__.py": "",
    "tests/test_users.py": "from fastapi.testclient import TestClient\nfrom app.main import app\n\nclient = TestClient(app)\n\ndef test_get_users():\n    response = client.get('/api/users')\n    assert response.status_code == 200\n    assert response.json() == {\"users\": [{\"id\": 1, \"name\": \"John Doe\"}]}\n",
    ".env": "DATABASE_URL=sqlite:///./test.db\nSECRET_KEY=mysecretkey\n",
    "requirements.txt": "fastapi\nuvicorn\nsqlalchemy\npydantic\npytest\n",
    "Dockerfile": "FROM python:3.10\n\nWORKDIR /app\nCOPY . /app\n\nRUN pip install --no-cache-dir -r requirements.txt\n\nCMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n",
    "README.md": "# FastAPI Project\n\nA simple FastAPI project structure.\n"
}

# Function to create folders and files


def create_project_structure():
    for dir in project_structure:
        os.makedirs(dir, exist_ok=True)

    for file, content in files.items():
        with open(file, "w") as f:
            f.write(content)

    print("FastAPI project structure created successfully!")


if __name__ == "__main__":
    create_project_structure()
