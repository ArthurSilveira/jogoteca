from flask import Flask, render_template

class jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = jogo('Valorant','Fps','PC')
jogo2 = jogo('CS:GO','Fps','PC')
jogo3 = jogo('Minecraft','Aventura','PC/Xbox')
jogo4 = jogo('LoL','Moba','PC')

lista = [jogo1, jogo2, jogo3, jogo4]

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html',titulo='Novo Jogo')

app.run()