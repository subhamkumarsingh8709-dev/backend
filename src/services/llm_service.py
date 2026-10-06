from groq import Groq

from src.core import config


client = Groq(
    api_key=config.GROQ_API_KEY
)


def generate_response(query: str, context: str) -> str:

    prompt = f"""
    You are a customer support assistant.

    Answer the customer's question using only the information
    provided in the knowledge base context.

    If the answer is not available in the context, say:
    "I don't have enough information in the knowledge base to answer that."

    Do not invent policies, prices, timelines, or procedures.

    Knowledge base context:
    {context}

    Customer question:
    {query}

    Answer:
    """

    response = client.chat.completions.create(
        model=config.GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt,
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content #type:ignore