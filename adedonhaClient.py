import mysql.connector
from time import sleep

mydb = mysql.connector.connect(
host = 'sql10.freesqldatabase.com',
user = 'sql10360953',
password = 'MJgw6pEpcH',
db = 'sql10360953')

cursor = mydb.cursor()

def versus():
    mydb = mysql.connector.connect(
    host = 'sql10.freesqldatabase.com',
    user = 'sql10360953',
    password = 'MJgw6pEpcH',
    db = 'sql10360953')

    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM versus')

    jogadores = cursor.fetchone()
    return jogadores

jogadores = versus()    
if jogadores[0] =='PLAY1': #jogador 1
    nick = input('Voce eo jogador 1\nDigite seu nome: \n')
    cursor.execute('UPDATE versus SET jogador1 = (%s)',[nick])
    mydb.commit()


elif jogadores[1] == 'PLAY2': #jogador 2
    nick = input('Voce eo jogador 2\nDigite seu nome: \n')
    cursor.execute('UPDATE versus SET jogador2 = (%s)',[nick])
    mydb.commit()




while True:
    jogadores = versus()
    if jogadores[0] !='PLAY1' and jogadores[1]!='PLAY2':
        
        mydb = mysql.connector.connect(
        host = 'sql10.freesqldatabase.com',
        user = 'sql10360953',
        password = 'MJgw6pEpcH',
        db = 'sql10360953'
        )
        cursor = mydb.cursor()
            
        cursor.execute('SELECT * FROM charada')
        print(cursor.fetchone()[0])
        sleep(1)
    else:
        input('AGUARDANDO JOGADOR 2...\n\n\n PRESSIONE QUAL QUER TECLA')
    
        
