# Data Scienec Tutor
# 🤖 DS Tutor Chat

**DS Tutor Chat** is an interactive AI-powered **Data Science tutor** built with **Streamlit** and **Google's Gemini 1.5 Pro**. It provides **instant explanations, Python code examples, and a quiz mode** to test your knowledge. 🚀

## Deployment URL:
[https://data-scienec-tutor-znyyapr2mc8ji4ckwfnjda.streamlit.app/]

## Features

- **Interactive Chat Interface** – Ask questions and get real-time responses.
- **Data Science Concepts** – Learn about various topics in data science.
- **Code Examples** – Request Python code snippets for better understanding.
- **Memory Retention** – The tutor maintains context across conversations.
- **Customizable Sidebar** – Includes settings, profile links, and more.
- **Quiz Mode** – Test your knowledge with interactive questions.
- **Streamlit UI Enhancements** – Improved layout and custom styling.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- `langchain`
- `langchain-google-genai`
- `google-generativeai`
- `python-dotenv`

### Installation

1. Clone the repository:
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd DS-Tutor-Chat
    ```

2. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Add your Google API key:
    - Create a `.env` file in the project root and add:
      ```
      GOOGLE_API_KEY=YOUR_API_KEY
      ```

5. Run the application:
    ```bash
    streamlit run app.py
    ```

6. Open `http://localhost:8501` to access the app.

## Folder Structure

```
DS-Tutor-Chat/
├── app.py
├── utils/
│   ├── __init__.py
│   ├── session_manager.py
│   ├── llm_utils.py
│   └── data_classes.py
├── components/
│   ├── __init__.py
│   ├── sidebar.py
│   └── chat_interface.py
├── static/
├── .streamlit/
├── .env (for local development)
├── README.md
└── requirements.txt
```

## Deployment (Streamlit Cloud)

1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app.
3. Select your repository and `app.py` file.
4. Add `GOOGLE_API_KEY` as a secret.
5. Click **Deploy** and start using your AI tutor!

## Customization

- Modify `static/style.css` for UI changes.
- Update `components/sidebar.py` for sidebar elements.
- Adjust model settings in `utils/llm_utils.py`.
- Replace `static/logo.png` with your own branding.

---

💡 **DS Tutor Chat** is designed to make learning Data Science engaging and interactive. Happy coding! 🚀
