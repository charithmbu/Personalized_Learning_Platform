from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Groq API Key (store it securely in production)
GROQ_API_KEY = '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'
client = Groq(api_key=GROQ_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    
    try:
        # Call the Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {   
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",
        )
        response = chat_completion.choices[0].message.content
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
