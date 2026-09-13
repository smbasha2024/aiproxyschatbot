from fastapi import FastAPI, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from app.routes import emp_leaves_route, emp_details_route

#from app.auth.auth import auth_middleware_call
from app.configs.settings import settings

app = FastAPI(
    title = settings.server.api_name,
    description = "This AI agent automates regulator-authorized portals to extract compliance evidence and integrates with the CMS to enable automatic closure.",
    version = settings.server.version
)

@app.exception_handler(StarletteHTTPException)
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": False,
            "error_code": exc.status_code,
            "error_desc": exc.detail
        }
    )

app.include_router(emp_leaves_route.emp_leaves_route)
app.include_router(emp_details_route.emp_details_route)

origins = settings.server.cors_urls
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def root():
    return {"message": f"Welcome to {app.title} {app.version}! {app.description}"}

@app.get("/health")
def health_check():
    return {"status": "Healthy", "service": "Data Bridge"}