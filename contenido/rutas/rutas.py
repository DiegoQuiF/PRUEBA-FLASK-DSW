from flask import Blueprint, render_template, request, redirect, url_for, flash
from contenido.utilidades.db import db;
from app import Task, TaskSchema
from app import task_schema, tasks_schema

rutas = Blueprint("rutas", __name__)

@rutas.route('/tasks', methods = ['POST'])
def create_task():
    title = request.json['title']
    description = request.json['description']

    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)