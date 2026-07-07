from src.rag_pipeline import RAGAssistant

assistant = RAGAssistant()

question = "What are Knowledge Bases?"

response = assistant.ask(question)

print(f"""
    {"="*50}
    QUESTION:
    {"="*50}
    {question} 
    {"="*50}
    ANSWER: 
    {"="*50}
    {response.answer} 
    {"="*50} 
    SOURCES: 
    {"="*50} 
    {response.sources[0].document}
    {response.sources[0].page_range}
""")

