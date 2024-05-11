from fastapi import FastAPI

from controller.register_routes import register_controllers

app = FastAPI()
register_controllers(app=app)
