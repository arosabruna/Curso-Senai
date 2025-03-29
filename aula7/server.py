from flask import Flask, jsonify, request, render_template

# Criando aplicação em Flask 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# GET > Buscar algo
@app.route("/helloworld", methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "Ola mundo, como estao voces?"
    })

# Lista de tarefas
tarefas = [
    { "id": 1, "titulo": "Estudar Python", "feito": False},
    { "id": 1, "titulo": "Ler a doc", "feito": True}
]

# GET - Buscar informações
@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)

# POST - Criar uma nova tarefa
""""
JavaScript (Front) -> fetch
ReactJS (Front) -> axios
Insomnia (Aplicativo -> Simular um Front
Postman (Aplicativo) -> Simular um Front

Back-end -> Modelo de API -> FULL REST
Full-strack -> Arquitetura MVC (Model, View, Controller)
"""
@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    nova_tarefa = request.json # pegar a informação no body
    nova_tarefa['id'] =len(tarefas) + 1 # adicionando novo id
    tarefas.append(nova_tarefa) # adicionando nova tarefa na lista
    return jsonify(nova_tarefa), 201 # 201 -> create -> criado com sucesso

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:5000/helloworld