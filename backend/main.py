from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
import openai
from datetime import datetime
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Hospital Virtual Assistant API",
    description="A medical chatbot API that helps with basic health queries",
    version="1.0.0"
)

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatMessage(BaseModel):
    content: str

class ChatResponse(BaseModel):
    response: str
    disclaimer: str

class MedicalChatbot:
    def __init__(self):
        self.model = "gpt-4"
        self.conversation_history: Dict[str, List[dict]] = {}
        self.disclaimer = (
            "IMPORTANT: This is an AI assistant and not a substitute for professional "
            "medical advice, diagnosis, or treatment. Always seek the advice of your "
            "physician or other qualified health provider for any medical condition."
        )

    async def get_response(self, user_id: str, message: str) -> str:
        try:
            # Initialize conversation history if it doesn't exist
            if user_id not in self.conversation_history:
                self.conversation_history[user_id] = []

            
            messages = [
                {"role": "system", "content":"THANK YOUs"},
                *self.conversation_history[user_id],
                {"role": "user", "content": message}
            ]

            
            completion = await openai.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )

            response = completion.choices[0].message.content

            # Update conversation history
            self.conversation_history[user_id].extend([
                {"role": "user", "content": message},
                {"role": "assistant", "content": response}
            ])
            if len(self.conversation_history[user_id]) > 10:
                self.conversation_history[user_id] = self.conversation_history[user_id][-10:]

            return response

        except Exception as e:
            logger.error(f"Error getting response from OpenAI: {str(e)}")
            raise HTTPException(status_code=500, detail="Error processing your request")

# Initialize chatbot
chatbot = MedicalChatbot()

@app.post("/chat/{user_id}", response_model=ChatResponse)
async def chat_endpoint(user_id: str, message: ChatMessage):
   
    try:
        response = await chatbot.get_response(user_id, message.content)
        return ChatResponse(
            response=response,
            disclaimer=chatbot.disclaimer
        )
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/chat/{user_id}")
async def clear_chat_history(user_id: str):
    """Clear the chat history for a specific user"""
    if user_id in chatbot.conversation_history:
        del chatbot.conversation_history[user_id]
    return {"status": "success", "message": "Chat history cleared"}

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }