import mysql.connector

mydb = mysql.connector.connect(
    host = 'sql10.freesqldatabase.com',
    user = 'sql10360953',
    password = 'MJgw6pEpcH',
    db = 'sql10360953'
    )
cursor = mydb.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS jogador (nome VARCHAR(255),pontos INTEGER(255))')
cursor.execute('CREATE TABLE IF NOT EXISTS charada (frase VARCHAR(255))')
cursor.execute('CREATE TABLE IF NOT EXISTS versus (jogador1 VARCHAR(255),jogador2 VARCHAR(255))')
cursor.execute('CREATE TABLE IF NOT EXISTS resposta (resp VARCHAR(255),jogador VARCHAR(255))')

cursor.execute('INSERT INTO versus (jogador1,jogador2) VALUES ("PLAY1","PLAY2")')
mydb.commit()

cursor.execute('INSERT INTO charada (frase) VALUES ("VAZIO")')
mydb.commit()
cursor.execute('INSERT INTO resposta (resp,jogador) VALUES ("VAZIO","VAZIO")')
mydb.commit()
