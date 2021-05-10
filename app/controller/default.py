from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.model.tables import Cliente

@app.route("/")
def index():
    #selecionar todos - select * from
    clientes = Cliente.query.all()
    return render_template("index.html", clientes=clientes)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # crio um objeto cliente com os dados do formulario
        cliente = Cliente(request.form['nome'], request.form['comentario'], request.form['email'], request.form['cep'], request.form['rua'], request.form['bairro'], request.form['cidade'], request.form['uf'], request.form['numero'])
        # adiciono o cliente (insert into)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")
    
@app.route("/edit/<int:ra>", methods=['GET', 'POST'])
def edit(ra):
    # select from
    cliente = Cliente.query.get(ra)
    if request.method == 'POST':
        cliente.name = request.form['nome']
        cliente.comment = request.form['comentario']
        cliente.email = request.form['email']
        cliente.cep = request.form['cep']
        cliente.rua = request.form['rua']
        cliente.bairro = request.form['bairro']
        cliente.cidade = request.form['cidade']
        cliente.uf = request.form['uf']
        cliente.numero = request.form['numero']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", cliente = cliente)
 
@app.route("/delete/<int:ra>")
def delete(ra):
    cliente = Cliente.query.get(ra)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))
