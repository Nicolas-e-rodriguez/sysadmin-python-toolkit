from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sys
import os

# Agregamos la ruta raíz para importar 'core'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.providers import DirectoryProvider

app = FastAPI(title="SysAdmin Toolkit Web", description="Panel local de gestión")

# Configuramos la carpeta de plantillas HTML
templates_path = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_path)

provider = DirectoryProvider(mode="mock")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, q: str = ""):
    # Obtenemos los usuarios (filtrados o todos)
    users = provider.search_users(q)
    return templates.TemplateResponse(
        request,
        "index.html", 
        {"users": users, "query": q}
    )
