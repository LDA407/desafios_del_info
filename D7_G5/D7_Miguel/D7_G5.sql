create database D7_G5_blogONG;

use D7_G5_blogONG;

create table if not exists usuario
(
id_usuario int(11) primary key auto_increment,
nombre varchar(50) not null,
apellido varchar(50) not null,
telefono varchar(15),
username varchar(15) not null,
email varchar(80) not null,
contraseña varchar(50) not null,
estado bool not null,
fecha_creacion datetime,
avatar varchar(100),
es_publico bool not null,
es_colaborador bool,
es_admin bool 
);

create table articulo
(
id_articulo int(11) primary key auto_increment,
id_usuario int(11) not null,
titulo varchar(80) not null,
resumen varchar(200),
contenido longtext,
fecha_publicacion datetime,
estado bool,
imagen varchar(100),
foreign key (id_usuario) references usuario(id_usuario)
);

create table comentario
(
id_comentario int(11) primary key auto_increment,
id_articulo int(11) not null,
id_usuario int(11) not null,
contenido varchar(250),
fecha_hora datetime,
estado bool,
foreign key (id_articulo) references articulo(id_articulo),
foreign key (id_usuario) references usuario(id_usuario)
);
create table categoria
(
id_cat int(11) primary key auto_increment,
id_categoria int(11) not null,
nombre varchar(35) not null,
descripcion varchar(150),
imagen varchar(150),
estado bool not null,
foreign key (id_categoria) references categoria(id_cat)
);

create table categoria_articulo
(
id_articulo int(11) not null,
id_categoria int(11) not null,
foreign key (id_articulo) references articulo(id_articulo),
foreign key (id_categoria) references categoria(id_cat)
);
