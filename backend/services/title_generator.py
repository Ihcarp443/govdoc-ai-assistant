from providers.llm.hf_provider import HfProvider


def generate_title(
    question: str,
    answer: str
):
    prompt = f"""
You are generating chat titles.

Based on the user's question and the assistant's answer,
generate a concise conversation title.

Rules:
- 3 to 6 words
- Capture the main topic
- No quotes
- No punctuation at the end
- Do not use generic titles like "Question", "Government Scheme", or "Chat"
- Return ONLY the title

User Question:
{question}

Assistant Answer:
{answer}

Title:
"""
    model = HfProvider()

    response = model.generate(prompt)

    return response.content.strip()