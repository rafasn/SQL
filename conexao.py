# Importando a biblioteca (já instalou junto com python)
import sqlite3

# Conectando com o arquivo do banco de dados
conexao = sqlite3.connect('banco1')
# Passando a conexao para outra variavel
cursor = conexao.cursor()

## Criando a tabebela
    #cursor.execute('CREATE TABLE usuarios(id int, nome VARCHAR(100),endereco VARCHAR(100), email VARCHAR(100));')
    #cursor.execute('CREATE TABLE prudutos(id int, nome VARCHAR(100),endereco VARCHAR(100), email VARCHAR(100));')

## Alterando nome da tabela
    #cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

## Adicionando nova coluna 
    #cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT') 

## Alterando nome da coluna
    #cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

##Excluindo toda a tabela
    #cursor.execute('DROP TABLE prudutos') 

## Inserindo informações
    #cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Isadora", "França", "isa@gmail.com",1234567)')
    #cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2,"Maria", "São Paulo", "maria@gmail.com",1224567)')
    #cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(3,"João", "França", "joao@gmail.com",1234767)')

## Excluindo informações da tabela
    #cursor.execute('DELETE FROM usuario where id=1')

#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Isadora", "França", "isa@gmail.com",1234567)')

## Visualizando [* tudo]
    #dados = cursor.execute('SELECT nome,telefone FROM usuario WHERE id>2')
    # for usuario in dados:
        #print(usuario)

## Alterando dado da tabela 
cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="João"')

#envio das informações
conexao.commit()
#finalizar para não dar conflito!!!
conexao.close