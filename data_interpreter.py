
# MODULE 3: DATA INTERPRETER

from google import genai
from config import API_KEY, MODEL_NAME

client = genai.Client(api_key=API_KEY)


def interpret_data(data, context):
    prompt = f"""
    Explain this data simply:

    Context: {context}
    Data:
    {data}

    Include:
    - Summary
    - Trends
    - Issues
    - Recommendations
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


def run_data_interpreter():
    print("\n" + "="*50)
    print("       📊 DATA INTERPRETER")
    print("="*50)
    print("This tool explains any data in plain English.\n")

    context = input("What is this data about? (e.g. monthly sales figures, website traffic, survey results): ").strip()
    print("\nPaste your data below. When done, type END on a new line and press Enter.\n")
    print("Example data format:")
    print("  January: 1200 users")
    print("  February: 980 users")
    print("  March: 1450 users\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    user_data = "\n".join(lines)

    if not user_data.strip():
        print("⚠️  No data entered. Returning to menu.")
        return

    print("\n⏳ Interpreting your data...\n")
    result = interpret_data(user_data, context)

    print("="*50)
    print("✅ DATA INTERPRETATION:")
    print("="*50)
    print(result)

    with open("data_output.txt", "w", encoding="utf-8") as f:
        f.write("DATA INTERPRETATION OUTPUT\n" + "="*50 + "\n")
        f.write(result)
    print("\n💾 Interpretation saved to: data_output.txt")
