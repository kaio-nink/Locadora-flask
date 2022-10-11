create table pais
(
    Nome_pais varchar(20),
    Populacao decimal(10,2),
    Num_de_vitorias_em_copas int check (Num_de_vitorias_em_copas >= 0),
    Tecnico varchar (20) not null,
    primary key (Nome_pais)
);

create table jogadores
(
    Jogador_id int,
    Nome varchar (40) not null,
    Pname varchar (20) not null,
    Uname varchar (35),
    DNasc date,
    Pais varchar(20),
    Altura int,
    Clube varchar(30),
    Posicao varchar(10) check (Posicao in ("Goalkeeper", "Defender", "Midfielder", "Forward")),
    Caps_for_Country int,
    E_Capitao Boolean DEFAULT 0,
    primary key(Jogador_id),
    foreign key (Pais) references pais (Nome_pais)
);

create table resultados_jogos
(
    Partida_id int,
    Data_partida date,
    Hora_inicio time,
    Time1 varchar(25),
    Time2 varchar(25),
    Gols_time1 int check (Gols_time1 >= 0),
    Gols_time2 int check (Gols_time2 >= 0),
    Estadio varchar(35),
    Cidade_sede varchar(20) not null,
    primary key(Partida_id),
    foreign key (Time1) references pais (Nome_pais),
    foreign key (Time2) references pais (Nome_pais)
);

create table cartoes_jogadores
(
    Jogador_id int,
    Cartoes_amarelos int check(Cartoes_amarelos >= 0),
    Cartoes_vermelhos int check (Cartoes_vermelhos >= 0),
    primary key(Jogador_id),
    foreign key (Jogador_id) references jogadores (Jogador_id)
);

create table gols_assistencias_jogadores
(
    Jogador_id int,
    Num_de_jogos int check (Num_de_jogos >= 0),
    Gols int check (Gols >= 0),
    Assistencias int check (Assistencias >= 0),
    Minutos_jogados int check (Minutos_jogados >= 0),
    primary key(Jogador_id),
    foreign key (Jogador_id) references jogadores (Jogador_id)
);