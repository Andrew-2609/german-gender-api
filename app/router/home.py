from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from library.helpers import openfile

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
