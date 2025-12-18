from langchain_ollama import ChatOllama
from prompt import generation_prompt, reflection_prompt

llm = ChatOllama(model="llama3.1:8b")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm