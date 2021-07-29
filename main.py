import fastapi
import uvicorn
from typing import Optional
from fastapi import responses
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

api = fastapi.FastAPI()
templates = Jinja2Templates('templates')
api.mount('/static',StaticFiles(directory='static'), name='static')

@api.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html',{'request':request})


@api.get('/api/rec/')
def recommand(x: int, y: int, z: Optional[int]):
    result = x+y
    if z == 0:
        return responses.JSONResponse(content={"error": "Error Z cannot be a 0"},status_code=400)
        
    if z is not None:
        result /= z

    return {
        'result': result
    }


uvicorn.run(app=api, port=8000, host="127.0.0.1")
