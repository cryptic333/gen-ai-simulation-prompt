# MODULE 4: INTERACTIVE PROMPT ENGINEERING GUIDE

from google import genai
from config import API_KEY, MODEL_NAME

client = genai.Client(api_key=API_KEY)

LESSONS = {
    "1": {
        "title": "Be Specific, Not Vague",
        "bad_prompt": "Tell me about marketing.",
        "good_prompt": "Explain 3 digital marketing strategies suitable for a small bakery business with a budget under $500/month.",
        "tip": "The more specific your prompt, the more useful the response. Include WHO, WHAT, WHY and any constraints."
    },
    "2": {
        "title": "Assign a Role to the AI",
        "bad_prompt": "How do I invest money?",
        "good_prompt": "You are a financial advisor for beginners. Explain 3 safe investment options for someone starting with $1000, in simple language.",
        "tip": "Saying 'You are a [role]' makes the AI adopt that persona and expertise."
    },
    "3": {
        "title": "Ask for a Specific Format",
        "bad_prompt": "Give me ideas for team building.",
        "good_prompt": "List 5 team building activities for a remote team of 10 people. Format as a numbered list with: Activity Name, Time Required, and Cost Estimate.",
        "tip": "Specify the output format to get structured answers."
    },
    "4": {
        "title": "Give Context / Background",
        "bad_prompt": "Write an email about the meeting.",
        "good_prompt": "I'm a project manager. Write a professional email to my team reminding them about our Monday 10am sprint review meeting.",
        "tip": "Context helps the AI understand your situation better."
    },
    "5": {
        "title": "Use Step-by-Step Reasoning",
        "bad_prompt": "Should I quit my job?",
        "good_prompt": "Help me think through whether I should leave my current job. Walk me through a pros and cons analysis.",
        "tip": "Ask AI to think step-by-step for better reasoning."
    }
}


def show_live_example(lesson):
    print(f"\n🔴 BAD PROMPT:  {lesson['bad_prompt']}")
    print(f"🟢 GOOD PROMPT: {lesson['good_prompt']}")
    print(f"\n💡 TIP: {lesson['tip']}")

    demo = input("\n▶️  Want to run the GOOD prompt? (y/n): ").strip().lower()

    if demo == "y":
        print("\n⏳ Running...\n")

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=lesson["good_prompt"]
        )

        print(response.text)   # ✅ FIXED (now inside)


def run_prompt_guide():
    print("\n" + "="*50)
    print("   🧠 PROMPT ENGINEERING GUIDE")
    print("="*50)

    for key, lesson in LESSONS.items():
        print(f"\n📖 LESSON {key}: {lesson['title']}")
        print("-"*40)
        show_live_example(lesson)

        cont = input("\n➡️ Continue? (y/n): ").strip().lower()
        if cont != "y":
            break

    print("\n✅ Completed!")


def run_prompt_tester():
    print("\n" + "="*50)
    print("   🧪 TEST YOUR PROMPT")
    print("="*50)

    user_prompt = input("Enter your prompt: ").strip()

    if not user_prompt:
        print("⚠️ No prompt entered.")
        return

    print("\n⏳ Running...\n")

    # ✅ FIXED (use client, not model)
    result = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_prompt
    )

    print("\n📤 RESPONSE:\n")
    print(result.text)

    critique_prompt = f"""
    A user wrote this prompt: "{user_prompt}"

    Give:
    1. Score out of 10
    2. What’s good
    3. Improvements
    4. Better version
    """

    critique = client.models.generate_content(
        model=MODEL_NAME,
        contents=critique_prompt
    )

    print("\n🔍 FEEDBACK:\n")
    print(critique.text)
