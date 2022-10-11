from conexao import criar_conexao, fechar_conexao
import csv
from io import StringIO, BytesIO
from datetime import datetime

# Insere pais


def insere_pais(con, nome_pais, populacao, num_de_vitorias_em_copas, tecnico):
    cursor = con.cursor()
    sql = "INSERT INTO pais (Nome_pais, Populacao, Num_de_vitorias_em_copas, Tecnico) values (%s, %s, %s, %s)"
    valores = (nome_pais, populacao, num_de_vitorias_em_copas, tecnico)
    cursor.execute(sql, valores)  # executa o comando no mysql
    cursor.close()
    con.commit()  # commit para salvar no bd

# pega do arquivo csv e passa os parâmetros para inserir no bd


def get_ins_pais(con):
    with open('/home/harison/Documents/BD/trabalho2/input/Pais.csv', 'r') as file:
        infile = csv.reader(StringIO(file.read()), delimiter=',')

    # inserir paises
        for linha in infile:  # linha é uma lista [1,2,3]
            nome = linha[0][1:-1]
            populacao = linha[1]
            vitorias = linha[2]
            tecnico = linha[3][1:-1]

            try:
                insere_pais(con, nome, populacao, vitorias, tecnico)
                print('País adicionado com sucesso!')
            except BaseException as e:
                print('algo de errado não ta certo')
                print(e)  # printa o erro

# Insere Jogadores


def insere_jogadores(con, jogador_id, nome, pNome, uNome, dNasc, pais, altura, clube, posicao, caps_for_country, e_capitao):
    cursor = con.cursor()
    e_capitao = 1 if e_capitao == "TRUE" else 0
    sql = "INSERT INTO jogadores (Jogador_id, Nome, Pname, Uname, DNasc, Pais, Altura, Clube, Posicao, Caps_for_Country, E_capitao) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (jogador_id, nome, pNome, uNome, dNasc, pais,
               altura, clube, posicao, caps_for_country, e_capitao)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()  # commit para salvar no bd


def get_ins_jogadores(con):

    with open('/home/harison/Documents/BD/trabalho2/input/Jogadores.csv', 'r') as file:
        infile = csv.reader(StringIO(file.read()), delimiter=',')

    # inserir jogadores
        for linha in infile:  # linha é uma lista [1,2,3]
            jogador_id = linha[0]
            nome = linha[1][1:-1]
            pNome = linha[2][1:-1]
            uNome = linha[3][1:-1]
            dNasc = linha[4][1:-1]
            pais = linha[5][1:-1]
            altura = linha[6]
            clube = linha[7][1:-1]
            posicao = linha[8][1:-1]
            caps_for_country = linha[9]
            e_capitao = linha[10]

            try:
                insere_jogadores(con, jogador_id, nome, pNome, uNome, dNasc,
                                 pais, altura, clube, posicao, caps_for_country, e_capitao)
                print('Jogador adicionado com sucesso!')
            except BaseException as e:
                print('algo de errado não ta certo')
                print(e)

# INSERE RESULTADO_JOGOS


def insere_resultado_jogos(con, partida_id, data_partida, hora_inicio, time1, time2, gols_time1, gols_time2, estadio, cidade_sede):
    cursor = con.cursor()
    sql = "INSERT INTO resultados_jogos (Partida_id, Data_partida, Hora_inicio, Time1, Time2, Gols_time1, Gols_time2, Estadio, Cidade_sede) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (partida_id, data_partida, hora_inicio, time1,
               time2, gols_time1, gols_time2, estadio, cidade_sede)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()  # commit para salvar no bd


def get_ins_resultado_jogos(con):

    with open('/home/harison/Documents/BD/trabalho2/input/Resultados_jogos.csv', 'r') as file:
        infile = csv.reader(StringIO(file.read()), delimiter=',')

    # inserindo os resultados
        for linha in infile:  # linha é uma lista [1,2,3]
            partida_id = linha[0]
            data_partida = linha[1][1:-1]
            hora_inicio = linha[2][1:-1]
            time1 = linha[3][1:-1]
            time2 = linha[4][1:-1]
            gols_time1 = linha[5]
            gols_time2 = linha[6]
            estadio = linha[7][1:-1]
            cidade_sede = linha[8][1:-1]

            try:
                insere_resultado_jogos(con, partida_id, data_partida, hora_inicio,
                                       time1, time2, gols_time1, gols_time2, estadio, cidade_sede)
                print('Resultado adicionado com sucesso!')
            except BaseException as e:
                print('algo de errado não ta certo')
                print(e)  # para printar o erro

# INSERE CARTOES_JOGADORES


def insere_cartoes_jogadores(con, jogador_id, cartoes_amarelos, cartoes_vermelhos):
    cursor = con.cursor()
    sql = "INSERT INTO cartoes_jogadores (Jogador_id, Cartoes_amarelos, Cartoes_vermelhos) values (%s, %s, %s)"
    valores = (jogador_id, cartoes_amarelos, cartoes_vermelhos)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()  # commit para salvar no bd


def get_ins_cartoes_jogadores(con):

    with open('/home/harison/Documents/BD/trabalho2/input/Cartoes_Jogadores.csv', 'r') as file:
        infile = csv.reader(StringIO(file.read()), delimiter=',')

    # inserindo os resultados
        for linha in infile:  # linha é uma lista [1,2,3]
            jogador_id = linha[0]
            cartoes_amarelos = linha[1]
            cartoes_vermelhos = linha[2]

            try:
                insere_cartoes_jogadores(
                    con, jogador_id, cartoes_amarelos, cartoes_vermelhos)
                print('Cartões adicionado com sucesso!')
            except BaseException as e:
                print('algo de errado não ta certo')
                print(e)  # para printar o erro

# INSERE gols_assistencias_jogadores


def insere_gols_assistencias_jogadores(con, jogador_id, num_de_jogos, gols, assistencias, minutos_jogados):
    cursor = con.cursor()
    sql = "INSERT INTO gols_assistencias_jogadores (Jogador_id, Num_de_jogos, Gols, Assistencias, Minutos_jogados) values (%s, %s, %s, %s, %s)"
    valores = (jogador_id, num_de_jogos, gols, assistencias, minutos_jogados)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()  # commit para salvar no bd


def get_ins_gols_assistencias_jogadores(con):

    with open('/home/harison/Documents/BD/trabalho2/input/Gols_assistencias_jogadores.csv', 'r') as file:
        infile = csv.reader(StringIO(file.read()), delimiter=',')

    # inserindo os gols e assistencias
        for linha in infile:  # linha é uma lista [1,2,3]
            jogador_id = linha[0]
            num_de_jogos = linha[1]
            gols = linha[2]
            assistencias = linha[3]
            minutos_jogados = linha[4]

            try:
                insere_gols_assistencias_jogadores(
                    con, jogador_id, num_de_jogos, gols, assistencias, minutos_jogados)
                print('Gols e Assistências adicionado com sucesso!')
            except BaseException as e:
                print('algo de errado não ta certo')
                print(e)  # para printar o erro

# INSERE gols_assistencias_jogadores


def insere_gols_assistencias_jogadores(con, jogador_id, num_de_jogos, gols, assistencias, minutos_jogados):
    cursor = con.cursor()
    sql = "INSERT INTO gols_assistencias_jogadores (Jogador_id, Num_de_jogos, Gols, Assistencias, Minutos_jogados) values (%s, %s, %s, %s, %s)"
    valores = (jogador_id, num_de_jogos, gols, assistencias, minutos_jogados)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()  # commit para salvar no bd


def select_todos_usuarios(con):

    cursor = con.cursor()
    sql = "SELECT * FROM pais"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print(resultado)
    cursor.close()


def main():
    con = criar_conexao("localhost", "root", "harison123", "Copa_2014")

    get_ins_pais(con)
    get_ins_jogadores(con)
    get_ins_resultado_jogos(con)
    get_ins_cartoes_jogadores(con)
    get_ins_gols_assistencias_jogadores(con)

    fechar_conexao(con)

    return


if __name__ == "__main__":
    main()
