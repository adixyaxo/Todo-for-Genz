from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from src.config.database import conn
from pymongo import MongoClient
from pathlib import Path
from bson import ObjectId
from src.config.settings import templates

router = APIRouter()


@router.get("/notes", response_class=HTMLResponse)
async def notes_url(request: Request):
    return templates.TemplateResponse(
        name="notes.html",
        request=request,
        context={}
    )