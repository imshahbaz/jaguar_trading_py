from fastapi import APIRouter
from service import margin_service

def margin_routes(app):
    margin = APIRouter(tags=['Margin'])

    @margin.get('/publishMessage')
    async def get_data():
       return margin_service.publish_message()
    
    @margin.get('/hello')
    async def hello():
       return "Hello from jaguar bot!!"
    
    app.include_router(margin)