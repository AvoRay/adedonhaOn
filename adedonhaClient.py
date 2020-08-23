# Cliente Adedonha
import mysql.connector

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

else:
    nick= 'Indigente'




while True:
    jogadores = versus()
    if jogadores[0] !='PLAY1' and jogadores[1]!='PLAY2':# se os dois tiver logado ja
        
        mydb = mysql.connector.connect(
        host = 'sql10.freesqldatabase.com',
        user = 'sql10360953',
        password = 'MJgw6pEpcH',
        db = 'sql10360953'
        )
        cursor = mydb.cursor()
          
        cursor.execute('SELECT * FROM charada')
        
        pergunta = cursor.fetchone()[0]
        
        print(pergunta)
        

        mydb = mysql.connector.connect(
        host = 'sql10.freesqldatabase.com',
        user = 'sql10360953',
        password = 'MJgw6pEpcH',
        db = 'sql10360953'
        )
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM resposta')
        respostas = cursor.fetchall()
        
        if respostas[0][0]!='VAZIO':# se ja foi respondido
        
            jogador = respostas[0][1]
            resposta = respostas[0][0]
            print('O jogador {} respondeu {}'.format(jogador,resposta))
            input('\nContinue...')
            cursor.execute('UPDATE charada SET frase = "VAZIO"')
            mydb.commit()

        else:# se nao foi respondido
            resposta = input('Resposta : \n')

            mydb = mysql.connector.connect(
            host = 'sql10.freesqldatabase.com',
            user = 'sql10360953',
            password = 'MJgw6pEpcH',
            db = 'sql10360953'
            )
            
            cursor = mydb.cursor()
            cursor.execute('UPDATE resposta SET resp = (%s),jogador = (%s)',(resposta,nick))
            cursor.execute('UPDATE charada SET frase = "VAZIO"')
            mydb.commit()
    else:
        input('AGUARDANDO JOGADOR 2...\n\n\nPRESSIONE QUAL QUER TECLA')
    
        
