from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser


def get_explain_chain(memory):
    llm = ChatOllama(
        model = "llama3",
        temperature=0.2
    )

    with open("prompts/explain.txt", "r", encoding="utf-8") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["code","chat_history"],
        template=template
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain

