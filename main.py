# MAIN FILE — Run this to launch the AI Toolkit

from summarizer import run_summarizer
from email_drafter import run_email_drafter
from data_interpreter import run_data_interpreter
from prompt_guide import run_prompt_guide, run_prompt_tester


def print_banner():
    print("\n")
    print("="*55)
    print("  🤖  GENERATIVE AI COPILOT TOOLKIT  🤖")
    print("  Your Personal AI-Powered Work Assistant")
    print("="*55)
    print("  Built with: Python + Google Gemini API")
    print("  Purpose: Learn & use AI for everyday tasks")
    print("="*55)


def print_menu():
    print("\n📋 WHAT WOULD YOU LIKE TO DO?\n")
    print("  1. 📝 Summarize a Document / Long Text")
    print("  2. ✉️  Draft a Professional Email")
    print("  3. 📊 Interpret / Explain Data")
    print("  4. 🧠 Learn Prompt Engineering (5 Lessons)")
    print("  5. 🧪 Test & Improve My Own Prompt")
    print("  6. 📌 View KPIs & Project Info")
    print("  7. 🚪 Exit")
    print()


def show_kpis():
    print("\n" + "="*55)
    print("      📌 PROJECT KPIs & SUCCESS METRICS")
    print("="*55)
    kpis = [
        ("Adoption Rate Target",       "70% of users complete at least 2 modules"),
        ("Time Saved Per Task",         "Target: 15–30 mins saved vs manual effort"),
        ("Task Completion Quality",     "AI output rated 4/5 or above by user"),
        ("Prompt Quality Improvement",  "Users improve prompt score by 2+ points"),
        ("Email Draft Acceptance Rate", "80%+ emails used with minor edits only"),
        ("Summary Accuracy",            "Key points retained in 90%+ of summaries"),
    ]
    for metric, target in kpis:
        print(f"  ✅ {metric}")
        print(f"     → {target}\n")

    print("="*55)
    print("      🗺️  LEARNING PATH MODULES")
    print("="*55)
    modules = [
        ("Module 1", "Use-case Identification — What can AI help with?"),
        ("Module 2", "Responsible AI — Privacy, bias, limitations"),
        ("Module 3", "Prompt Engineering — Write better prompts"),
        ("Module 4", "AI Workflows — Summarise, draft, interpret"),
        ("Module 5", "Measuring Impact — Time saved, quality gained"),
    ]
    for mod, desc in modules:
        print(f"  📚 {mod}: {desc}")
    print()


def main():
    print_banner()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            run_summarizer()
        elif choice == "2":
            run_email_drafter()
        elif choice == "3":
            run_data_interpreter()
        elif choice == "4":
            run_prompt_guide()
        elif choice == "5":
            run_prompt_tester()
        elif choice == "6":
            show_kpis()
        elif choice == "7":
            print("\n👋 Thanks for using the AI Copilot Toolkit. Goodbye!\n")
            break
        else:
            print("\n⚠️  Invalid choice. Please enter a number between 1 and 7.")

        input("\n🔁 Press Enter to return to the main menu...")


if __name__ == "__main__":
    main()
