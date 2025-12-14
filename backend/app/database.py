import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ----------------------------------------------------
# Absolute path to backend directory (VERY IMPORTANT)
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SQLite database file (single source of truth)
DB_PATH = os.path.join(BASE_DIR, "sweetshop.db")

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# ----------------------------------------------------
# SQLAlchemy Engine
# ----------------------------------------------------
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite
)

# ----------------------------------------------------
# Session
# ----------------------------------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ----------------------------------------------------
# Base class for models
# ----------------------------------------------------
Base = declarative_base()

# ----------------------------------------------------
# Dependency for FastAPI routes
# ----------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
