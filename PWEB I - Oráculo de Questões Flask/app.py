from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de tarefas
tasks = []

# Rota inicial
@app.route('/')
def index():
    return redirect('/lista-tarefas')

# Rota para exibir a lista de tarefas
@app.route('/lista-tarefas')
def lista_tarefas():
    return render_template('lista_tarefas.html', tasks=tasks)

# Rota para adicionar uma tarefa
@app.route('/adicionar-tarefa', methods=['GET', 'POST'])
def adicionar_tarefa():
    if request.method == 'POST':
        tarefa = request.form['tarefa']
        tasks.append(tarefa)
        return redirect('/lista-tarefas')
    return render_template('adicionar_tarefa.html')

# Rota para concluir uma tarefa
@app.route('/concluir-tarefa/<int:id>')
def concluir_tarefa(id):
    if id < len(tasks):
        tasks[id] = f'[CONCLUÍDA] {tasks[id]}'
    return redirect('/lista-tarefas')

# Rota para excluir uma tarefa
@app.route('/excluir-tarefa/<int:id>')
def excluir_tarefa(id):
    if id < len(tasks):
        del tasks[id]
    return redirect('/lista-tarefas')

if __name__ == '__main__':
    app.run(debug=True)
