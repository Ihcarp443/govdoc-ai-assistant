from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint
)
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
print("HF_TOKEN:", os.getenv("HF_TOKEN"))


class HfProvider:

    def __init__(self):

        self.llm = HuggingFaceEndpoint(
            repo_id="google/gemma-4-31B-it",
            huggingfacehub_api_token=os.getenv("HF_TOKEN"),
            max_new_tokens=1000,    
    )   


    def generate(self, prompt):
        model = ChatHuggingFace(llm=self.llm)
        response = model.invoke(
            prompt
        )
        return response 

    