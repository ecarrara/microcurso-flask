# -*- coding: utf-8 -*-

import json
from datetime import datetime
from flask import Flask, render_template, request, redirect
import posts


#: Representa nossa aplicação web
app = Flask('web')



#### Nossas views (funções que atendem requisições HTTP)
@app.route('/', methods=['GET'])
def home():
    todos_posts = posts.list()
    return render_template('home.html', posts=todos_posts)


@app.route('/ver/<int:pos>', methods=['GET'])
def ver_post(pos):
    post = posts.get(pos)
    return render_template('post.html', post=post, pos=pos)


@app.route('/novo', methods=['GET', 'POST'])
def novo_post():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        conteudo = request.form.get('conteudo')
        posts.create(titulo, conteudo)
        return redirect('/')
    return render_template('novo.html')


@app.route('/excluir/<int:pos>', methods=['POST'])
def excluir_post(pos):
    posts.delete(pos)
    return redirect('/')

