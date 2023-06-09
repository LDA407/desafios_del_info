------------------------------------------
-- DML para usuarios 
------------------------------------------
-- administrador
INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'juan', 'carlos', 'juanka_23', '3624987234', 'juanka@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 0, 1);

-- colaborador
INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'marcos', 'rofriguez', 'marc_ro', '3624987344', 'rofriguez@gmail.com', MD5('asdasd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'silvina', 'escalante', 'silvi', '3624983434', 'es.silvi@gmail.com', MD5('asijdoaasdaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'nicolas', 'quintana', 'nico_q', '3624385234', 'nicoq23@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'sofia', 'marques', 'mar_sofia', '3624987234', 'marsofia@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

-- publico
INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'juanse', 'luna', 'juan234', '3624987233', 'juanse.luna@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'frida', 'calo', 'frida_ca', '3624987234', 'frida@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'macarena', 'esposito', 'maca345', '3624987234', 'maca@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'alejandro', 'rodriguez', 'alejo345', '3624987234', 'alejo.rodriguez@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

INSERT INTO Usuario( nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ( 'juan', 'carlos', 'juanka_23', '3624987234', 'juanka@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

------------------------------------------
-- DML para Articulo
------------------------------------------
-- estado en true
INSERT INTO Articulo(idUsuario, titulo, resumen, contenido, fecha_publicacion, estado, imagen)
VALUES ();

INSERT INTO Articulo(idUsuario, titulo, resumen, contenido, fecha_publicacion, estado, imagen)
VALUES ();

INSERT INTO Articulo(idUsuario, titulo, resumen, contenido, fecha_publicacion, estado, imagen)
VALUES ();

-- estado en falso
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


