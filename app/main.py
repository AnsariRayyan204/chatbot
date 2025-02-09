from fastapi import FastAPI
from app.routes import chat
from app.routes import chat, upload 



app = FastAPI()

# Include chatbot API
app.include_router(chat.router)
app.include_router(upload.router)
@app.get("/")
def root():
    return {"message": "Versatile Chatbot API is running!"}
