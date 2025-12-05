from langchain_ollama import OllamaChat
from prompt import generation_prompt, reflection_prompt

llm = OllamaChat(model="llama3.1:8b")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm