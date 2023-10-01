
------------------------------------------
-- DML para usuarios 
------------------------------------------
-- administrador
INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('juan', 'carlos', 'juanka_23', '3624987234', 'juanka@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 0, 1);

-- colaborador
INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES
    ('marcos', 'rofriguez', 'marc_ro', '3624987344', 'rofriguez@gmail.com', MD5('asdasd'), 1,'1996-12-31 23:59:59', 0, 1, 0),
    ('silvina', 'escalante', 'silvi', '3624983434', 'es.silvi@gmail.com', MD5('asijdoaasdaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0),
    ('nicolas', 'quintana', 'nico_q', '3624385234', 'nicoq23@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0),
    ('sofia', 'marques', 'mar_sofia', '3624987234', 'marsofia@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

-- publico
INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES
    ('juanse', 'luna', 'juan234', '3624987233', 'juanse.luna@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0),
    ('frida', 'calo', 'frida_ca', '3624987234', 'frida@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0),
    ('macarena', 'esposito', 'maca345', '3624987234', 'maca@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0),
    ('alejandro', 'rodriguez', 'alejo345', '3624987234', 'alejo.rodriguez@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0),
    ('abel', 'pintos', 'abel', '3624987234', 'pintos35@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

UPDATE Usuario SET es_admin=1 WHERE idUsuario=2;


------------------------------------------
-- DML para Articulo
------------------------------------------
-- estado en true
INSERT INTO Articulo(idUsuario, titulo, resumen, contenido, fecha_publicacion, estado)
VALUES
    (2, 'El veredicto del Tribunal Oral Criminal 4 de La Plata', 'Masacre de Monte: dos policías condenados a prisión perpetua y dos a 15 años de cárcel', 'ARTIVULO 1' , '1996-12-31 23:59:59', 1),
    (3, 'La advertencia sobre la continuidad de Massa en el gobierno', 'Cecilia Moreau apuntó a Daniel Scioli y criticó las PASO: "Le hace daño a la Argentina"', 'ARTICULO 2' , '1996-12-31 23:59:59', 1),
    (3, 'ajsdnkajsdnkaj','aksdkalsdk','ARTICULO 3' , '1996-12-31 23:59:59', 1);

-- estado en falso
INSERT INTO Articulo(idUsuario, titulo, contenido, fecha_publicacion, estado)
VALUES (2, 'asdñkasñod','asdpokasdokasdo', '1996-12-31 23:59:59', 0);

DELETE FROM Articulo WHERE estado=0;

<<<<<<< Updated upstream
-- Agregar el comando necesario para listar todos los artículos que tengan
-- comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
-- nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho
-- comentario, agrupados por artículos.
---
=======

SELECT Articulo.titulo, Articulo.fecha_publicacion, Usuario.nombre, Comentario.fecha_hora
FROM Articulo
JOIN Comentario ON Articulo.idArticulo = Comentario.idArticulo
JOIN Usuario ON Comentario.idUsuario = Usuario.idUsuario
ORDER BY Articulo.titulo;

>>>>>>> Stashed changes


------------------------------------------
-- DML para Comentario
------------------------------------------
INSERT INTO Comentario(idArticulo, idUsuario, contenido, fecha_hora, estado)
VALUES
    (1,9,'aksmdlaksmdlaksmdlkm', '1996-12-31 23:59:59', 1),
    (1,8,'alskdmalksdmlaksmdlalskdmlkasmd', '1996-12-31 23:59:59', 1),
    (1,5,'alskdmlaksd', '1996-12-31 23:59:59', 1),
    (2,7,'asdaksdjkasjdaksjd', '1996-12-31 23:59:59', 1),
    (2,6,'asdaksuhdkasjhd', '1996-12-31 23:59:59', 1);


-- ==============================  INNER JOIN AGREGADO AL QUERY =================================
-- listando articulos con comentarios, ordenados por artículo
SELECT articulo.titulo, articulo.fecha_publicacion, usuario.nombre, comentario.fecha_hora
FROM articulo
INNER JOIN comentario
ON comentario.id_articulo=articulo.id_articulo
INNER JOIN usuario
ON comentario.id_usuario=usuario.id_usuario
order by articulo.id_articulo

-- ================================================================================================


------------------------------------------
-- DML para Categoria
------------------------------------------

INSERT INTO Categoria(nombre, estado) VALUES ('deportes', 1);

INSERT INTO Categoria(nombre, estado) VALUES ('politica', 1);

INSERT INTO Categoria(nombre, estado) VALUES ('internacionales', 1);

INSERT INTO Categoria(nombre, estado) VALUES ('finanzas', 1);

INSERT INTO Categoria(nombre, estado) VALUES ('economia', 1);

INSERT INTO Categoria(nombre, estado) VALUES ('ciencia', 1);

INSERT INTO Categoria(nombre, estado) VALUES ('tecnonlogia', 1);

INSERT INTO Categoria(nombre, estado) VALUES ('policiales', 1);


------------------------------------------
-- DML para CategoriaArticulo
------------------------------------------

INSERT INTO CategoriaArticulo(idCategoria, idArticulo) VALUES (8,1);

INSERT INTO CategoriaArticulo(idCategoria, idArticulo) VALUES (2,2);

INSERT INTO CategoriaArticulo(idCategoria, idArticulo) VALUES (1,3);


