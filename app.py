from flask import Flask, render_template, jsonify, request
from flask_cors import CORS 
import openai

# Define sua chave de API do OpenAI
openai.api_key = "API AQUI"
app = Flask(__name__)
CORS(app)



# Define o modelo a ser utilizado
model_engine = "text-curie-001"

# Define a função que envia a mensagem para o GPT-3 e retorna a resposta
def send_message(message):
    # Gera a resposta do GPT-3
    response = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Obtém a resposta gerada pelo GPT-3
    message = response.choices[0].text.strip()

    # Retorna a resposta gerada pelo GPT-3
    return message

@app.route("/home")
def homepage():
    return render_template("index.html")
    
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")
    
@app.route("/api/zen", methods=["GET"])
def getResponseZen():
    message = request.args.get("msg")
    msg = f"O que é {message}? E me envie links de sites para estudar!"
    return jsonify({"message": send_message(msg)})
    
@app.route("/zen")
def zenPage():
    return render_template("chat.html")
    
if __name__ == "__main__":
    app.run(port=9090, debug=True, host="0.0.0.0")