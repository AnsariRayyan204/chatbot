# from transformers import pipeline

# class ChatBot:
#     def __init__(self):
#         # Load a question-answering model
#         self.qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

#     def respond(self, question: str, context: str = ""):
#         if context:
#             result = self.qa_model({"question": question, "context": context})
#             return result["answer"]
#         return f"I received your query: '{question}', but I need more context!"

# # Test chatbot response
# if __name__ == "__main__":
#     bot = ChatBot()
#     print(bot.respond("What is AI?", "Artificial Intelligence is a field of computer science."))
import torch
from transformers import pipeline

class ChatBot:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"  # Auto-detect
        print(f"Loading model on: {device}")  
        self.qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2", device=-1)  # Force CPU

    def respond(self, question: str, context: str = ""):
        result = self.qa_model({"question": question, "context": context})
        return result["answer"]
