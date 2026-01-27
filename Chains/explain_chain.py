from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser


def get_explain_chain():
    llm = ChatOllama(
        model = "llama3:8b",
        temperature=0.2
    )

    with open("prompts/explain.txt", "r", encoding="utf-8") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["code"],
        template=template
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain

