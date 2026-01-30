from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_debug_chain(memory):
    llm = ChatOllama(
        model = "llama3",
        temperature=0
    )

    with open("prompts/debug.txt", "r", encoding="utf-8") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["code"],
        template=template
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain
