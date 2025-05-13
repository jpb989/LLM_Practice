from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="deepseek32b40k:latest")

template = """
You are an expert in answering questions about a pizza restraunt
Here are some relavant reviews: {reviews}
Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate(template)
chain = prompt | model

result = chain.invoke({"reviews": [], "question": "What is the best pizza place in town?"})
print(result)