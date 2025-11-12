import sqlite3

def excluir_cliente(id):
    with sqlite3.connect("clientes.db") as conn:
        sql_excluir_cliente = '''
        DELETE FROM clientes
        WHERE id = ?
        '''
        conn.execute(sql_excluir_cliente, (id,))

def cadastrar_cliente(nome, email):
    with sqlite3.connect("clientes.db") as conn:
        sql_insert_cliente = '''
        INSERT INTO clientes (nome, email)
        VALUES (?, ?)
        '''
        conn.execute(sql_insert_cliente, (nome, email))

def listar_clientes():
    with sqlite3.connect("clientes.db") as conn:
        sql_listar_clientes = '''
        SELECT nome, email
        FROM clientes
        '''
        cur = conn.cursor()        
        cur.execute(sql_listar_clientes)        
        # retorna uma lista de tuplas [(nome,email), (nome, email)...]
        return cur.fetchall() 
    
def pesquisar_cliente(nome):
     with sqlite3.connect("clientes.db") as conn:
        sql_pesquisar_clientes = '''
        SELECT id, nome, email
        FROM clientes
        WHERE nome LIKE ?
        '''
        cur = conn.cursor()
        cur.execute(sql_pesquisar_clientes,(f'%{nome}%',))
        # retorna uma lista de tuplas [(nome,email), (nome, email)...]
        return cur.fetchall() 