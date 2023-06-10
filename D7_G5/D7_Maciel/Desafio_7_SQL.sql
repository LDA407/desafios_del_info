#Grupo 5

/*Escribir los comandos SQL que permitan la creación de las tablas con sus 
respectivas restricciones de claves primarias y foráneas*/
DROP DATABASE IF EXISTS blog;
CREATE DATABASE blog;
USE blog;

CREATE TABLE usuarios(
id INT AUTO_INCREMENT,
nombre VARCHAR(30),
apellido VARCHAR(30),
telefono INT,
username VARCHAR(30),
email VARCHAR(30),
contraseña VARCHAR(30),
estado BOOLEAN,
fecha_creacion DATE,
avatar BLOB,
es_publico BOOLEAN,
es_colaborador BOOLEAN,
es_admin BOOLEAN,
CONSTRAINT PK_usuario PRIMARY KEY(id)
);

CREATE TABLE articulos(
id INT AUTO_INCREMENT,
titulo VARCHAR(50),
resumen TEXT,
contenido LONGTEXT,
fecha_publicacion DATE,
estado BOOLEAN,
imagen BLOB,
id_usuario INT,
CONSTRAINT PK_articulos PRIMARY KEY(id),
CONSTRAINT FK_articulos FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
);

CREATE TABLE categorias(
id INT AUTO_INCREMENT,
nombre VARCHAR(30),
descripcion VARCHAR(1000),
imagen BLOB,
estado BOOLEAN,
CONSTRAINT PK_categorias PRIMARY KEY(id)
);

CREATE TABLE comentarios(
id INT AUTO_INCREMENT,
contenido TEXT,
fecha_hora DATETIME,
estado BOOLEAN,
id_usuario INT,
id_articulo INT,
CONSTRAINT PK_comentarios PRIMARY KEY(id),
CONSTRAINT FK_usuarios FOREIGN KEY(id_usuario) REFERENCES usuarios(id),
CONSTRAINT FK_comentarios FOREIGN KEY(id_articulo) REFERENCES articulos(id)
);

CREATE TABLE categorias_articulos(
id_categoria INT,
id_articulo INT,
CONSTRAINT PK_categorias_articulos PRIMARY KEY(id_categoria, id_articulo),
constraint FK_categorias_categorias_articulos FOREIGN KEY(id_categoria) REFERENCES categorias(id),
constraint FK_articulos_categorias_articulos FOREIGN KEY(id_articulo) REFERENCES articulos(id)
);

/*Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol 
de admin, 4 con rol de colaborador y 5 con rol de público*/
INSERT INTO usuarios VALUES
(null, 'Fulano','De', 123456780, 'FA', 'fa@fd.com', 'fdfdfd', 1, '2023/03/30', '', 0, 0, 1),
(null, 'Fulano','Det', 123456781, 'FB', 'fb@fd.com', 'fdfdfd', 1, '2023/03/30', '', 0, 1, 0),
(null, 'Fulano','Deta', 123456782, 'FC', 'fc@fd.com', 'fdfdfd', 1, '2023/03/30', '', 0, 1, 0),
(null, 'Fulano','Detal', 123456783, 'FD', 'fd@fd.com', 'fdfdfd', 1, '2023/03/30', '', 0, 1, 0),
(null, 'Fulano','Ddtal', 123456784, 'FE', 'fe@fd.com', 'fdfdfd', 1, '2023/03/30', '', 0, 1, 0),
(null, 'Fulano','Dddal', 123456785, 'FF', 'ff@fd.com', 'fdfdfd', 1, '2023/03/30', '', 1, 0, 0),
(null, 'Fulano','Ddddl', 123456786, 'FG', 'fg@fd.com', 'fdfdfd', 1, '2023/03/30', '', 1, 0, 0),
(null, 'Fulano','Ddddd', 123456787, 'FH', 'fh@fd.com', 'fdfdfd', 1, '2023/03/30', '', 1, 0, 0),
(null, 'Fulano','Aetal', 123456788, 'FI', 'fi@fd.com', 'fdfdfd', 1, '2023/03/30', '', 1, 0, 0),
(null, 'Fulano','Aatal', 123456789, 'FJ', 'fj@fd.com', 'fdfdfd', 1, '2023/03/30', '', 1, 0, 0);

/*Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios 
agregado con rol de colaborador*/
UPDATE usuarios 
SET es_colaborador = 0, es_admin = 1
WHERE id = 2;

/*Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con 
estado TRUE y uno con estado FALSE*/
INSERT INTO articulos VALUES
(null, 'Titulo1', 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.',
'', '2023/03/30', 1, '', 3),
(null, 'Titulo2', 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.',
'', '2023/03/30', 1, '', 4),
(null, 'Titulo3', 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.',
'', '2023/03/30', 1, '', 5),
(null, 'Titulo4', 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.',
'', '2023/03/30', 0, '', 6);

/*Agregar el comando necesario para eliminar el artículo que tenga estado FALSE*/
#Esta es la única forma en que me dejó borrar el artículo ya que estoy usando actualización en modo seguro
DELETE FROM articulos
WHERE id = (SELECT * FROM ( SELECT id FROM articulos WHERE estado = 0) AS t);
#Otra forma
DELETE FROM articulos
WHERE estado = 0;

/*Agregar el comando necesario que introduzca 3 comentarios al primer artículo 
agregado y 2 comentarios al segundo artículo*/
INSERT INTO comentarios VALUES
(null,'Primer comentario del artículo 1', NOW(), 1, 1, 1),
(null,'Segundo comentario del artículo 1', NOW(), 1, 2, 1),
(null,'Tercer comentario del artículo 1', NOW(), 1, 3, 1),
(null,'Primer comentario del artículo 2', NOW(), 1, 4, 2),
(null,'Segundo comentario del artículo 2', NOW(), 1, 5, 2);

/*Agregar el comando necesario para listar todos los artículos que tengan 
comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el 
nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho 
comentario, agrupados por artículos*/
SELECT a.titulo, a.fecha_publicacion, u.username, c.fecha_hora
FROM articulos a
JOIN comentarios c ON a.id = c.id_articulo
JOIN usuarios u ON c.id_usuario = u.id
GROUP BY a.id;




