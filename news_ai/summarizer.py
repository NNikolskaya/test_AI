import os
import json
from typing import Dict
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SUMMARIZE_PROMPT_TEMPLATE = """
You are a professional news assistant. Please do the following:
1. Summarize the following article in 3-5 sentences.
2. Identify 3-5 main topics from the article as a list of short keywords.

Article:
\"\"\"
{article_text}
\"\"\"

Respond in the following JSON format:

{{
  "summary": "...",
  "topics": ["...", "..."]
}}

Respond ONLY in raw JSON format, without explanations or additional text.

"""

def summarize_article(article_text: str) -> Dict[str, str]:
    prompt = SUMMARIZE_PROMPT_TEMPLATE.format(article_text=article_text[:4000])  # щоб не вийти за токени

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    try:
        content = response.choices[0].message.content
        result = json.loads(content)
        return {
            "summary": result.get("summary", ""),
            "topics": result.get("topics", []),
        }
    except Exception as e:
        return {
            "summary": "",
            "topics": [],
            "error": str(e),
        }
