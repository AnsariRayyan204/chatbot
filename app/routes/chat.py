from fastapi import APIRouter
from pydantic import BaseModel
from app.chatbot.core import ChatBot

router = APIRouter()
bot = ChatBot()

class Query(BaseModel):
    question: str
    context: str = ""

@router.post("/chat")
def chat(query: Query):
    response = bot.respond(query.question, query.context)
    return {"response": response}
