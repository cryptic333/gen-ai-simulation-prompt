# MODULE 1: DOCUMENT SUMMARIZER

from google import genai
from config import API_KEY, MODEL_NAME

client = genai.Client(api_key=API_KEY)


def summarize_text(text, style="bullet points"):
    prompt = f"""
    You are a professional document summarizer.
    Summarize the following text in {style} format.
    Keep it clear, concise, and easy to understand.

    TEXT:
    {text}
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
def run_summarizer():
    print("\n" + "="*50)
    print("       📝 DOCUMENT SUMMARIZER")
    print("="*50)
    print("Paste your text below. When done, type END on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    user_text = "\n".join(lines)

    if not user_text.strip():
        print("⚠️  No text entered. Returning to menu.")
        return

    print("\nChoose summary style:")
    print("  1. Bullet Points")
    print("  2. One Paragraph")
    print("  3. Executive Summary")
    choice = input("\nEnter 1, 2 or 3: ").strip()

    style_map = {
        "1": "bullet points",
        "2": "one concise paragraph",
        "3": "executive summary with key takeaways"
    }
    style = style_map.get(choice, "bullet points")

    print("\n⏳ Summarizing...\n")
    result = summarize_text(user_text, style)

    print("="*50)
    print("✅ SUMMARY:")
    print("="*50)
    print(result)

    # Save to file
    with open("summary_output.txt", "w", encoding="utf-8") as f:
        f.write("SUMMARY OUTPUT\n" + "="*50 + "\n")
        f.write(result)
    print("\n💾 Summary saved to: summary_output.txt")
