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


@router.get("/profile", response_class=HTMLResponse)
async def profile_url(request: Request):
    return templates.TemplateResponse(
        name="profile.html",
        request=request,
        context={}
    )


@router.get("/settings", response_class=HTMLResponse)
async def settings_url(request: Request):
    return templates.TemplateResponse(
        name="settings.html",
        request=request,
        context={}
    )

