import mysql.connector

try:
    #Conexão com o banco de dados
    con = mysql.connector.connect(host = 'localhost', database = 'nome da sua tabela', user = 'root', password = 'sua senha')


    # Declaração SQL a ser executada
    # Muito atenção aqui, se o script estiver com erros a tabela não será criada.

    criar_tabela_SQL = """CREATE TABLE tbl_cli (
        IdCliente int (11) NOT NULL,
        NomeCliente VARCHAR (70) NOT NULL,
        Email FLOAT NOT NULL,
        Endereco TINYINT NOT NULL,
        PRIMARY KEY (IdCliente))"""
    
         
    #Criar cursor e executar SQL no banco de dados
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print ("Tabela de Clientes criada com sucesso!")

except mysql.connector.Error as erro:
    print ('Falha ao criar tabela no MySQL:()'.format(erro))
finally:
    if con.is_conneted():
        cursor.close()
        con.close()
        print ("Conexão ao MySQL finalizada.")
