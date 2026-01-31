from agents.hf_llm import load_llm

llm = load_llm()

def create_plan(intent: str) -> dict:
    """
    Creates a deterministic, structured analysis plan
    """

    prompt = f"""
You are a senior autonomous data analysis planner.

USER INTENT:
{intent}

RULES:
- Do NOT repeat the intent
- Create EXACTLY 5 steps
- Each step must start with an action verb
- Keep steps short
- No explanations

FORMAT:
1. Step one
2. Step two
3. Step three
4. Step four
5. Step five
"""

    response = llm(
        prompt,
        max_new_tokens=120,
        do_sample=False,
        temperature=0.0
    )

    plan_text = response[0]["generated_text"]

    steps = [
        line.strip()
        for line in plan_text.split("\n")
        if line.strip().startswith(tuple("12345"))
    ]

    return {
        "intent": intent,
        "plan": steps
    }
