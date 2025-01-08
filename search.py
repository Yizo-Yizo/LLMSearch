from flask import Flask, request, jsonify
from llm_axe import OnlineAgent, PdfReader, OllamaChat

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    date = data.get('date')
    document = data.get('document')

    llm = OllamaChat(model="llama3.2:latest")
    #PdfReader = PdfReader(llm)
    onlineAgent = OnlineAgent(llm)

    prompt = f"What changes are associated with the {date} update to the document {document}. Provide specific detail of any new provisions, include examples of control measures and specific requirements for worker training."

    resp = onlineAgent.search(prompt)
    return jsonify({"result": resp})

if __name__ == '__main__':
    app.run(debug=True)


