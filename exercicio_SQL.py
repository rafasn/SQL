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

# Atualização e Remoção
#a) Atualize a idade de um aluno
#cursor.execute('UPDATE alunos SET idade="26" WHERE nome="Pedro" ')

#b) Remova um aluno pelo seu ID
cursor.execute('DELETE FROM alunos WHERE id=5')
#Envio das informações/alterações para o banco 
conexao.commit()
#inalizar para não dar conflito!!!
conexao.close