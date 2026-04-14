# MODULE 2: EMAIL DRAFTER

from google import genai
from config import API_KEY, MODEL_NAME

client = genai.Client(api_key=API_KEY)


def draft_email(purpose, tone, key_points, recipient):
    prompt = f"""
    Write a professional email:

    Recipient: {recipient}
    Purpose: {purpose}
    Tone: {tone}
    Key points: {key_points}

    Include subject, greeting, body, and closing.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


def run_email_drafter():
    print("\n" + "="*50)
    print("       ✉️  EMAIL DRAFTER")
    print("="*50)

    recipient = input("\nWho is this email to? (e.g. My Manager, HR Team, Client): ").strip()
    purpose = input("What is the email about? (e.g. requesting a day off, following up on a project): ").strip()
    key_points = input("Key points to mention (e.g. dates, details, questions): ").strip()

    print("\nChoose tone:")
    print("  1. Formal / Professional")
    print("  2. Friendly but Professional")
    print("  3. Urgent")
    print("  4. Apologetic")
    tone_choice = input("\nEnter 1, 2, 3 or 4: ").strip()

    tone_map = {
        "1": "formal and professional",
        "2": "friendly but professional",
        "3": "urgent and direct",
        "4": "apologetic and sincere"
    }
    tone = tone_map.get(tone_choice, "professional")

    print("\n⏳ Drafting your email...\n")
    result = draft_email(purpose, tone, key_points, recipient)

    print("="*50)
    print("✅ YOUR EMAIL:")
    print("="*50)
    print(result)

    with open("email_output.txt", "w", encoding="utf-8") as f:
        f.write("EMAIL DRAFT OUTPUT\n" + "="*50 + "\n")
        f.write(result)
    print("\n💾 Email saved to: email_output.txt")
