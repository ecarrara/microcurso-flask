# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime


db_filepath = './posts.json'

if not os.path.exists(db_filepath):
    with open(db_filepath, 'w') as f:
        f.write('[]')


def list():
    db_file = open(db_filepath, 'r')
    return json.load(db_file)


def get(pos):
    db_file = open(db_filepath, 'r')
    posts = json.load(db_file)
    return posts[pos]


def create(titulo, conteudo):
    with open(db_filepath, 'r') as db_file:
        posts = json.load(db_file)

    posts.append({
        'titulo': titulo,
        'conteudo': conteudo,
        'datahora': datetime.now().isoformat(),
        'comentarios': []
    })

    with open(db_filepath, 'w') as db_file:
        json.dump(posts, db_file)


def delete(pos):
    with open(db_filepath, 'r') as db_file:
        posts = json.load(db_file)

    del posts[pos]

    with open(db_filepath, 'w') as db_file:
        json.dump(posts, db_file)
