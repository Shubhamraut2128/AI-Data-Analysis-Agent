from .hf_llm import load_llm

def generate_insights(df):
    llm = load_llm()

    summary = df.describe().to_string()

    prompt = f"""
You are a senior data analyst.

Dataset summary:
{summary}

Task:
- Infer trends and insights from the data
- Do NOT repeat numbers
- Return ONLY insights
- Write exactly 3 bullet points
"""

    output = llm(
        prompt,
        max_new_tokens=120,
        do_sample=False,
        temperature=0.0,
        repetition_penalty=1.3,
        truncation=True
    )

    text = output[0]["generated_text"]

    # 🔥 Remove prompt from output
    insights = text.replace(prompt, "").strip()

    return insights
