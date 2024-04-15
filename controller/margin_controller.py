from fastapi import APIRouter
from service import margin_service

def margin_routes(app):
    margin = APIRouter(tags=['Margin'])

    @margin.get('/publishMessage')
    async def get_data():
       return margin_service.publish_message()
    
    app.include_router(margin)