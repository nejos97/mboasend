from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .models.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/healthcheck", status_code=status.HTTP_200_OK)
async def perform_healthcheck(db: Session = Depends(get_db)) -> dict:
    '''
    Simple route for the healthcheck.
    It basically sends a GET request to the route & hopes to get a "200"
    response code. Failing to return a 200 response code this means that 
    the application is not functional so a strategy must be put in place
    to have an instance still available or rollback to an older version.
    It acts as a last line of defense in case something goes south.
    Additionally, it also returns a JSON response in the form of:
    {
      'healtcheck': 'Everything OK!'
    }
    '''
    try:
        db.execute('SELECT 1')
    except:
        raise HTTPException(status_code=503, detail="Database connection failed")
    return {'healthcheck': 'Everything OK!'} 
