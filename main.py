from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.base import router
from config.config import settings
import uvicorn

def include_router(app):
    app.include_router(router)

def add_middleware(app):
	app.add_middleware(
    	CORSMiddleware,
    	allow_origins=["*"],
    	allow_credentials=True,
    	allow_methods=["*"],
    	allow_headers=["*"],
	)

def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	add_middleware(app)
	# create_tables()    
	return app

app = start_application()

if __name__=='__main__':
	uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True, log_level='info')


