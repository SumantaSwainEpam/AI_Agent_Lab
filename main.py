from Agent.agent import ask_ai
from Tasks.task_example import open_notepad_and_type

def automate_task():
    task = "Open Notepad and type 'Automation works with Gemini AI!'"
    steps = ask_ai(task)

    print("\n🤖 AI Instructions:\n", steps)

    # Run the example task
    open_notepad_and_type()

if __name__ == "__main__":
    automate_task()
