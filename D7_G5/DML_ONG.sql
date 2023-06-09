------------------------------------------
-- DML para usuarios 
------------------------------------------
INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion)
VALUES ( 'juan', 'carlos', 'juanka_23', '3624987234', 'juanka@gmail.com', MD5('asijdoaisd'), 'activo','2345-45-65');


------------------------------------------
-- DML para Articulo
------------------------------------------
INSERT INTO Articulo(idUsuario, titulo, resumen, contenido, fecha_publicacion, estado, imagen)
VALUES ();


------------------------------------------
-- DML para Comentario
------------------------------------------
INSERT INTO Comentario( idArticulo, idUsuario, contenido, fecha_hora, estado)
VALUES ();


------------------------------------------
-- DML para Categoria
------------------------------------------
INSERT INTO Categoria( nombre, descripcion, imagen, estado, idSubCategoria)
VALUES ();


------------------------------------------
-- DML para CategoriaArticulo
------------------------------------------
INSERT INTO CategoriaArticulo( idCategoria, idArticulo)
VALUES ();


