import sqlite3
conexao = sqlite3.connect('banco_SQL')
cursor = conexao.cursor()

#1. Criar tabela
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100),idade INT, curso VARCHAR(50))')

#2. Inserir pelo menos 5 registros
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Rafaela",24,"Eng. de Produção") ')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Vitória",25,"Eng. Ambiental") ')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Eduarda",24,"Farmácia") ')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Roberta",27,"Eng. de Produção") ')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Pedro",24,"Eng. de Produção") ')

#cursor.execute('UPDATE alunos SET curso="Engenharia" WHERE id=1 ')
#cursor.execute('UPDATE alunos SET curso="Engenharia" WHERE id=2 ')
#cursor.execute('UPDATE alunos SET curso="Engenharia" WHERE id=4 ')
#cursor.execute('UPDATE alunos SET curso="Engenharia" WHERE id=5 ')

#3. Consultas básicas: 
print("3. Consultas básicas:")

print("a) Selecionar todos os registros da tabela")
dados_2 = cursor.execute('SELECT * FROM alunos')
for alunos in dados_2:
    print(alunos)

print("b) Selecionar nome e idade dos alunos com mais de 20 anos")
dados_2 = cursor.execute('SELECT * FROM alunos WHERE idade>20')
for alunos in dados_2:
    print(alunos)

print("c) Selecionar alunos do curso Engenharia em ordem alfabética")
dados_2 = cursor.execute('SELECT nome FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for alunos in dados_2:
    print(alunos)

print("d) Contar o número total de alunos")
dados_2 = cursor.execute('SELECT count(nome) FROM alunos')
for alunos in dados_2:
    print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno
#cursor.execute('UPDATE alunos SET idade="26" WHERE nome="Pedro" ')

#b) Remova um aluno pelo seu ID
#cursor.execute('DELETE FROM alunos WHERE id=5')

#5. Criar uma tabela e inserir dados
#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100),idade INT, saldo FLOAT)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3, "Patricia", 32, 22100)')

#6. Consultas e Funções agregadas
print("6. CONSULTAS E FUNÇÕES AGREGADAS")
print("a) Selecionar nome e idade dos clientes com idade superior a 30 anos")
#dados_3 = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
dados_maior30 = cursor.execute('SELECT nome,idade FROM clientes GROUP BY idade HAVING idade>30')
for clientes in dados_maior30:
    print(clientes)

print("b) Calcule o saldo médio dos clientes")
dados_media_saldo = cursor.execute('SELECT avg(saldo) FROM clientes')
for clientes in dados_media_saldo:
    print(clientes)

print("c) Encontre o cliente com o saldo máximo")
dados_max_saldo = cursor.execute('SELECT nome,max(saldo) FROM clientes')
for clientes in dados_max_saldo:
    print(clientes)

print("d) Conte quantos clientes tem acima de 1000")
dados_max_saldo = cursor.execute('SELECT count(nome) FROM clientes WHERE saldo>1000')
for clientes in dados_max_saldo:
    print(clientes)

#7. Atualização e Remoção com condição
#cursor.execute('UPDATE clientes SET saldo="30000" WHERE nome="Roberta" ')
#cursor.execute('DELETE FROM clientes WHERE id=1')

#8. JUNÇÃO DE TABELAS
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT)')
FOREIGN KEY(cliente_id) REFERENCES clientes(id);

#Envio das informações/alterações para o banco 
conexao.commit()
#Finalizar para não dar conflito!!!
conexao.close