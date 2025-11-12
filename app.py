from flask import Flask, request, render_template, redirect, flash
import model

srv = Flask(__name__)
srv.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@srv.route("/")
def get_home():
    pass


@srv.post("/atualizar")
def post_atualizar():
    id = request.form["id"]
    nome = request.form["nome"]
    email = request.form["email"]
    model.atualizar_cliente(id, nome, email)
    flash("Cliente atualizado")
    return redirect(f"/editar/cliente/{id}")

@srv.get("/editar/cliente/<id>")
def get_editar_cliente(id):
    umCliente = model.pesquisar_cliente_id(id)
    return render_template("editar_cliente.html", cliente = umCliente)

@srv.get("/excluir/cliente/<id>")
def get_excluir_cliente(id):
    model.excluir_cliente(id)
    flash("Cliente Excluído")
    return redirect("/pesquisar")

@srv.get("/pesquisar")
def get_pesquisar():
    return render_template("pesquisar.html")

@srv.post("/pesquisar")
def post_pesquisar():
    nome = request.form["nome"]
    listagem_clientes = model.pesquisar_cliente(nome)    
    return render_template("pesquisar.html", clientes=listagem_clientes)

@srv.get("/cadastrar")
def get_cadastrar():
    listagem_clientes = model.listar_clientes()
    return render_template("cadastrar.html", clientes=listagem_clientes)

@srv.post("/cadastrar")
def post_cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    model.cadastrar_cliente(nome, email)
    
    return redirect("/cadastrar")

if __name__ == "__main__":
    srv.run(host="localhost",port=5000,debug=True)