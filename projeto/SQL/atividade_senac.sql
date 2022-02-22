create database PI_JOGOS;

use PI_JOGOS;


create table jogadores(
	nome_player varchar(30),
    email_player varchar(40),
    usuario_player varchar(20) primary key,
    senha_player varchar(20),
    genero_player varchar(15),
    dia timestamp not null default current_timestamp
);

select * from jogadores;

select senha_player from jogadores where usuario_player = 'jukras'
