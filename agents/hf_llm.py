from transformers import pipeline

_llm = None

def load_llm():
    global _llm

    if _llm is None:
        _llm = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )

    return _llm
