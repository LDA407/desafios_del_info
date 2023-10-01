
CREATE DATABASE IF NOT EXISTS ong_db;

USE ong_db;



CREATE TABLE IF NOT EXISTS Usuario (
  idUsuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellido VARCHAR(100),
  username VARCHAR(100) NOT NULL,
  telefono VARCHAR(45),
  email VARCHAR(255) NOT NULL,
  contraseña VARCHAR(255) NOT NULL,
  estado TINYINT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  avatar VARCHAR(255),
  es_publico TINYINT NOT NULL,
  es_colaborador TINYINT NOT NULL,
  es_admin TINYINT NOT NULL,
  PRIMARY KEY (idUsuario)
);


CREATE TABLE IF NOT EXISTS Articulo (
  idArticulo INT NOT NULL AUTO_INCREMENT,
  idUsuario INT NOT NULL,
  titulo VARCHAR(100) NOT NULL,
  resumen VARCHAR(255),
  contenido VARCHAR(1000) NOT NULL,
  fecha_publicacion DATETIME NOT NULL,
  estado TINYINT NOT NULL,
  imagen VARCHAR(255),
  PRIMARY KEY (idArticulo),
  FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario)
);


CREATE TABLE IF NOT EXISTS Comentario (
  idComentario INT NOT NULL AUTO_INCREMENT,
  idArticulo INT NOT NULL,
  idUsuario INT NOT NULL,
  contenido VARCHAR(500) NOT NULL,
  fecha_hora DATETIME NOT NULL,
  estado TINYINT NOT NULL,
  PRIMARY KEY (idComentario),
  
  FOREIGN KEY (idArticulo) REFERENCES Articulo(idArticulo),
  FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario)
);


CREATE TABLE IF NOT EXISTS Categoria (
  idCategoria INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255),
  imagen VARCHAR(255),
  estado TINYINT NOT NULL,
  idSubCategoria INT NULL,
  PRIMARY KEY (idCategoria)
);


CREATE TABLE IF NOT EXISTS CategoriaArticulo (
  idCategoriaArticulo INT NOT NULL AUTO_INCREMENT,
  idCategoria INT NOT NULL,
  idArticulo INT NOT NULL,
  PRIMARY KEY (idCategoriaArticulo),

  FOREIGN KEY (idCategoria) REFERENCES Categoria(idCategoria),
  FOREIGN KEY (idArticulo) REFERENCES Articulo(idArticulo)
);
