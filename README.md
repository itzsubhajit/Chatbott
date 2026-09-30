# AI Chatbot – Flask & Groq

This project is a professional AI chatbot built using **Flask** and the **Groq API**.

The chatbot allows users to enter questions and receive AI-generated responses through a clean and responsive web interface.

The application is designed with a focus on simplicity, readability, and a professional user experience.

---

## Features

- AI-powered conversational responses
- Professional chatbot interface
- User and AI message separation
- Structured AI responses
- Bullet-point answers
- Numbered lists for instructions
- Clean dark-themed UI
- Responsive design
- Quick suggestion buttons
- Back navigation option
- Error handling for API failures
- Powered by Groq AI

---

## Technology Used

- **Python**
- **Flask**
- **Groq API**
- **Requests**
- **HTML5**
- **CSS3**
- **JavaScript**

---

## Project Structure

```text
Chatbot/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```
How the Chatbot Works
```text
User Question
      ↓
Flask Web Application
      ↓
Requests Library
      ↓
Groq API
      ↓
AI Language Model
      ↓
Generated Response
      ↓
Displayed in Chat Interface
```
Application Workflow
The user enters a question in the chatbot.
Flask receives the submitted message.
The application sends the message to the Groq API.
The AI model processes the request.
Groq returns the generated response.
Flask sends the response to the webpage.
The response is displayed in the chatbot interface.
Installation
Step 1 – Clone the Repository
```text
git clone YOUR_GITHUB_REPOSITORY_URL
```
Step 2 – Open the Project
```text
cd Chatbot
```
Step 3 – Install Dependencies
```text
pip install flask requests
```
Groq API Setup

Create a Groq API key and add it to app.py.

Find:
```text
api_key = "YOUR_GROQ_API_KEY"
```
Replace it with your actual API key.

Example:
```text
api_key = "gsk_xxxxxxxxxxxxxxxxx"
```
Security Warning

Never upload your actual Groq API key to a public GitHub repository.

For a production application, use an environment variable:
```text
import os

api_key = os.getenv("GROQ_API_KEY")
```
Run the Application

Start the Flask server:
```text
python app.py
```
After the server starts, open the Flask address displayed in the terminal.

Example
User
```text
Explain artificial intelligence in simple terms.
```
AI Assistant
```text
Artificial Intelligence is a technology that allows computers
to perform tasks that normally require human intelligence.

- Learning – AI can learn patterns from data.
- Reasoning – AI can analyze information and make decisions.
- Language – AI can understand and generate human language.
- Vision – AI can analyze images and videos.
- Automation – AI can perform repetitive tasks automatically.
```
Response Formatting

The chatbot is designed to produce structured responses instead of large blocks of plain text.

Bullet Points
```text
- First point
- Second point
- Third point
```
Numbered Steps
```text
1. First step
2. Second step
3. Third step
```
Headings
```text
## Introduction

## Advantages

## Applications
```
This makes AI responses easier to read and understand.

Use Cases

The chatbot can be used for:

General question answering
Programming assistance
Study support
Concept explanations
Writing assistance
Brainstorming
Technical discussions
Learning new topics
Future Improvements

Potential future enhancements include:

Conversation history
Multi-turn memory
New chat option
Delete conversation
Export conversations
Voice input
Voice output
User authentication
Multiple AI models
File upload
Document analysis
Personalized AI instructions
Chat history database
Cloud deployment
Current Limitation

The current version sends the user's current message to the AI model.

It does not permanently store the complete conversation history.

For example:
```text
User: My name is Rahul.
AI: Nice to meet you, Rahul.

User: What is my name?
AI: The current version may not remember the previous message.
```
A future version can implement conversation memory so the chatbot can maintain context across multiple messages.

Disclaimer

AI-generated responses may contain inaccurate or incomplete information. Important information should be independently verified.

Author

Subhajit Pramanick

Built using Flask, Python, Groq API, Requests, HTML, CSS, and JavaScript.
