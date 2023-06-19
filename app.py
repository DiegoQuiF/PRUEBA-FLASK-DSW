from flask import Flask, request
#from contenido.rutas.rutas import rutas
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import DATABASE_CONNECTION_URI
from contenido.utilidades.db import db

app = Flask(__name__)

#Configuración de la BD de la app
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
ma = Marshmallow(app)

class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.Integer)

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone

app.app_context().push()
db.create_all()

class contactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fullname', 'email', 'phone')

task_schema = contactSchema()
tasks_schema = contactSchema(many=True)

@app.route('/tasks', methods = ['POST'])
def create_task():
    fullname = request.json['fullname']
    email = request.json['email']
    phone = request.json['phone']

    new_task = contact(fullname, email, phone)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)

if __name__ == '__main__':
    app.run(debug=True)


#No guardar cache
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Rutas e inicio
#app.register_blueprint(rutas)