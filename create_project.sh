#!/bin/bash

# Create directories
mkdir -p src/domain
mkdir -p src/usecase
mkdir -p src/infrastructure
mkdir -p src/presentation

# Create domain layer
cat <<EOL > src/domain/user.py
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
EOL

# Create usecase layer
cat <<EOL > src/usecase/user_usecase.py
from src.domain.user import User
from src.infrastructure.user_repository import UserRepository

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user_by_id(user_id)
EOL

# Create infrastructure layer
cat <<EOL > src/infrastructure/user_repository.py
from src.domain.user import User

class UserRepository:
    def get_user_by_id(self, user_id: int) -> User:
        # ここでは仮のデータを返しますが、実際にはデータベースから取得します
        return User(id=user_id, name="John Doe", email="john.doe@example.com")
EOL

# Create presentation layer
cat <<EOL > src/presentation/user_controller.py
from fastapi import APIRouter
from src.usecase.user_usecase import UserUseCase
from src.infrastructure.user_repository import UserRepository

router = APIRouter()

user_usecase = UserUseCase(UserRepository())

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_usecase.get_user(user_id)
    return user
EOL

# Create main entry point
cat <<EOL > src/main.py
from fastapi import FastAPI
from src.presentation import user_controller

app = FastAPI()

app.include_router(user_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOL

echo "Project structure created successfully."
