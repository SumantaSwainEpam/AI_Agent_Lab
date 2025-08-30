
# 🤖 Automation AI Agent (Gemini-powered)

This project is a lightweight **AI-powered task automation framework** that uses **Google Gemini Flash 2.0** to generate task instructions and execute them via Python automation scripts.  

Currently, the system demonstrates a simple task: **opening Notepad and typing a predefined message step by step**. The structure is modular, allowing you to expand functionality to include browser automation, screenshots, and system-level actions.

---

## 📂 **Project Structure**

```
automation_ai_agent/
│── requirements.txt        # Project dependencies
│── config.py                # Gemini API key configuration
│── agent.py                 # AI agent to interact with Gemini
│── main.py                  # Entry point for running automation
│── tasks/
│   └── example_task.py      # Example task (Notepad automation)
```

---

## ⚙️ **Setup Instructions**

### 1️⃣ Clone the Repository  
Open your terminal and run the following commands:  

```bash
git clone https://github.com/yourusername/automation_ai_agent.git
cd automation_ai_agent
```

### 2️⃣ Install Dependencies  
Install all required Python libraries using:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Gemini API Key  
Add your Gemini API key in the `config.py` file:  

```python
GEMINI_API_KEY = "your_api_key_here"
```

### 4️⃣ Run the Automation  
Execute the project using:  
```bash
python main.py
```

---

## 📝 **Example Task**

The AI agent performs predefined tasks step by step using Python automation.  

### Current Example:
The system opens Notepad and types the following text exactly as requested:
```
"Automation works with Gemini AI!
This project demonstrates intelligent task automation.
Step-by-step execution is running successfully."
```

✅ **Result:** Notepad opens, and the above text is typed automatically.

---

## 🚀 **Future Enhancements**  

Here are some ideas for expanding this framework:  
- 🔗 **Browser automation** (search, scrape, fill forms)  
- 📸 **Take and save screenshots**  
- 📂 **File system automation** (create, read, and organize files)  
- 🔐 **Automate logins and workflows**  
- 🖥️ **Cross-platform support** (Windows, Linux, macOS)  

---

## 📌 **Tech Stack**
- **Python 3.9+**  
- **Google Gemini Flash 2.0 API**  
- **PyAutoGUI** (for UI automation)  
- **Webbrowser / OS Libraries**  

---

## 💡 **Contribution**

Want to add more tasks? It’s simple!  
1. Create a new file under the `tasks/` directory, e.g., `browser_task.py`.  
2. Implement a `run()` function inside your file to define the task logic.  
3. Import and call your new task in `main.py`.  

👥 Contributions are welcome! Feel free to fork the repository, add enhancements, and share pull requests.

---

### 👨‍💻 Author

**Sumanta Swain**  
Junior Software Test Automation Engineer 
