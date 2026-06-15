from openai import OpenAI
from repo_loader import load_repo_text

client = OpenAI()

def ask_aide(question, repo_path="."):
    repo_files = load_repo_text(repo_path)

    context = "\n\n".join(
        f"FILE: {f['path']}\n{f['content']}"
        for f in repo_files
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You are an aerospace engineering assistant helping design "
                    "an open-source modular drone (MK0-MK4). "
                    "Focus on practical engineering, safety, and feasibility."
                )
            },
            {
                "role": "user",
                "content": f"""
REPO CONTEXT:
{context}

QUESTION:
{question}

Give:
1. Engineering analysis
2. Problems or risks
3. Suggested improvements
"""
            }
        ]
    )

    return response.output_text


if __name__ == "__main__":
    print(ask_aide("Is a 7-inch X-frame viable for MK2?"))