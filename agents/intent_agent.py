from langchain.prompts import PromptTemplate
from agents.hf_llm import load_llm

llm = load_llm()

def detect_intent(query):
    prompt = PromptTemplate(
        input_variables=["query"],
        template="""
        Classify the intent of the user query.
        Possible intents:
        - data_analysis
        - visualization
        - summary

        Query: {query}
        Intent:
        """
    )
    return llm(prompt.format(query=query))
