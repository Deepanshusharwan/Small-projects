from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from . import models, schemas, database, utils

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/shorten",response_model=schemas.URLInfo)
def shorten_url(payload: schemas.URLCreate, db: Session = Depends(get_db)):
    short_code = utils.generate_short_code()
    while db.query(models.URL).filter_by(short_code=short_code).first():
        short_code = utils.generate_short_code()

    url = models.URL(original_url=str(payload.url), short_code=short_code)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(models.URL).filter_by(short_code=short_code).first()
    if url is None:
        raise HTTPException(status_code=404, detail="short URL not found")

    url.clicks += 1
    db.commit()
    return RedirectResponse(url.original_url)
