from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, sweets

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register routers
app.include_router(auth.router)
app.include_router(sweets.router)

@app.get("/")
def root():
    return {"status": "Sweet Shop API running"}
