
CREATE DATABASE IF NOT EXISTS ong_db;

USE ong_db;

ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Usuario (
  idUsuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(45) NULL,
  apellido VARCHAR(45) NULL,
  username VARCHAR(45) NOT NULL,
  telefono VARCHAR(45) NULL,
  email VARCHAR(45) NOT NULL,
  contraseña VARCHAR(45) NOT NULL,
  estado TINYINT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  ------------------------------------------
  -- por seguridad no se guardan las imagenes en la base de datos asi que esto hay que cambiarlo
  -- a caracteres ya que django solo guarda las rutas.
  ------------------------------------------
  avatar BLOB NULL,
  ------------------------------------------
  -- [es_publico, es_colaborador, es_admin] campos booleanos
  ------------------------------------------
  es_publico TINYINT NOT NULL,
  es_colaborador TINYINT NOT NULL,
  es_admin TINYINT NOT NULL,
  PRIMARY KEY (idUsuario)
)


CREATE TABLE IF NOT EXISTS Articulo (
  idArticulo INT NOT NULL AUTO_INCREMENT,
  idUsuario INT NOT NULL,
  titulo VARCHAR(45) NOT NULL,
  resumen VARCHAR(45) NULL,
  contenido VARCHAR(45) NOT NULL,
  fecha_publicacion DATETIME NOT NULL,
  estado TINYINT NOT NULL,
  imagen BLOB NULL,
  PRIMARY KEY (idArticulo)
  -- solo faltaria agregar las claves foraneas
)


CREATE TABLE IF NOT EXISTS Comentario (
  idComentario INT NOT NULL AUTO_INCREMENT,
  idArticulo INT NOT NULL,
  idUsuario INT NOT NULL,
  contenido VARCHAR(45) NOT NULL,
  fecha_hora DATETIME NOT NULL,
  estado TINYINT NOT NULL,
  PRIMARY KEY (idComentario)
  -- solo faltaria agregar las claves foraneas
)


CREATE TABLE IF NOT EXISTS Categoria (
  idCategoria INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  descripcion VARCHAR(45) NULL,
  imagen BLOB NULL,
  estado TINYINT NOT NULL,
  idSubCategoria INT NULL,
  PRIMARY KEY (idCategoria)
)


CREATE TABLE IF NOT EXISTS CategoriaArticulo (
  idCategoriaArticulo INT NOT NULL AUTO_INCREMENT,
  idCategoria INT NOT NULL,
  idArticulo INT NOT NULL,
  PRIMARY KEY (idCategoriaArticulo)
  -- solo faltaria agregar las claves foraneas
)
