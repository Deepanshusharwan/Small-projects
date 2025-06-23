from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    url: HttpUrl

class URLInfo(BaseModel):
    original_url: str
    short_code: str
    clicks: int

    class Config:
        orm_mode = True
        
