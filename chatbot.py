from flask import Flask, request, render_template
import requests

app = Flask(__name__)

api_key = 'Put your own API key'


@app.route('/', methods=['GET', 'POST'])
def home():
    reply = ""

    if request.method == 'POST':
        message = request.form['message']

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "model": "openai/gpt-oss-20b",
                "messages": [
                    {
                        "role": "system",
                        "content": """You are a helpful assistant.

Always format your answers clearly and professionally.

Rules:
- Use bullet points whenever explaining information.
- Use numbered lists for step-by-step instructions.
- Keep paragraphs short.
- Use headings when the answer has multiple sections.
- Highlight important words using bold formatting.
- Avoid giving long blocks of plain text.
- Make answers easy to read and scan.
- If there are multiple points, separate them into bullet points.
- Give concise but useful answers."""
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }
        )

        data = response.json()

        if response.ok:
            reply = data['choices'][0]['message']['content']
        else:
            reply = data.get(
                'error', {}
            ).get(
                'message',
                'Something went wrong.'
            )

    return render_template('index.html', reply=reply)


if __name__ == '__main__':
    app.run(debug=True)