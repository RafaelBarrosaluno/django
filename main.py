''' Aluno: Rafael luis da Silva Barros -- RA: 28320078 '''

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'escola'
    )

def inserir_aluno(nome,idade,curso):
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO alunos(nome,idade,curso)VALUES(%s, %s, %s)", (nome, idade, curso))
    conn.commit()
    conn.close()

def atualizar_aluno(id, nome,idade,curso):
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute("UPDATE alunos SET (nome=%s,idade=%s,curso=%s WHERE id=%s)", (nome, idade, curso, id))
    conn.commit()
    conn.close()

def deletar_aluno(id):
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM alunos  WHERE id=%s", (id))
    conn.commit()
    conn.close()

def buscar_aluno(nome):
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE nome=%s", (nome,))
    result=cursor.fetchall()
    conn.close()
    return result

def buscar_menor_que(idade_max):
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE idade < %s", (idade_max,))
    result=cursor.fetchall()
    conn.close()
    return result


print(buscar_menor_que('25'))
#inserir_aluno('Rafael', 19, 'ADS')
# print (buscar_aluno('Rafael'))
# atualizar_aluno ('Rafael', 88, 'ADS')
# print (buscar_aluno('Rafael'))
# deletar_aluno('6')

