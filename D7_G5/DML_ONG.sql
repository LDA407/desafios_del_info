------------------------------------------
-- DML para usuarios 
------------------------------------------
-- administrador
INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('juan', 'carlos', 'juanka_23', '3624987234', 'juanka@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 0, 1);

-- colaborador
INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('marcos', 'rofriguez', 'marc_ro', '3624987344', 'rofriguez@gmail.com', MD5('asdasd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('silvina', 'escalante', 'silvi', '3624983434', 'es.silvi@gmail.com', MD5('asijdoaasdaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('nicolas', 'quintana', 'nico_q', '3624385234', 'nicoq23@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('sofia', 'marques', 'mar_sofia', '3624987234', 'marsofia@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 0, 1, 0);

-- publico
INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('juanse', 'luna', 'juan234', '3624987233', 'juanse.luna@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('frida', 'calo', 'frida_ca', '3624987234', 'frida@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('macarena', 'esposito', 'maca345', '3624987234', 'maca@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('alejandro', 'rodriguez', 'alejo345', '3624987234', 'alejo.rodriguez@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

INSERT INTO Usuario(nombre, apellido, username, telefono, email, contraseña, estado, fecha_creacion, es_publico, es_colaborador, es_admin)
VALUES ('abel', 'pintos', 'abel', '3624987234', 'pintos35@gmail.com', MD5('asijdoaisd'), 1,'1996-12-31 23:59:59', 1, 0, 0);

UPDATE Usuario SET es_admin=1 WHERE idUsuario=2;


------------------------------------------
-- DML para Articulo
------------------------------------------
-- estado en true
INSERT INTO Articulo(idUsuario, titulo, resumen, contenido, fecha_publicacion, estado)
VALUES (2, 'El veredicto del Tribunal Oral Criminal 4 de La Plata', 'Masacre de Monte: dos policías condenados a prisión perpetua y dos a 15 años de cárcel', 'La fiscalía había pedido penas de reclusión perpetua y de 20 años de cárcel para los efectivos que ya habían sido declarados culpables por un jurado popular: Rubén García, Leonardo Ecilapé, Mariano Ibáñez y Manuel Monreal. El Tribunal Oral en lo Criminal 4 (TOC) de La Plata sentenció este viernes a las penas de prisión perpetua y 15 años de cárcel a los cuatro policías bonaerenses ya declarados culpables por un jurado popular de la "Masacre de San Miguel del Monte", en la que cuatro jóvenes murieron en 2019 mientras eran perseguidos a los tiros por efectivos de esa fuerza de seguridad. Masacre de Monte: el jurado consideró culpables a los acusados. Los dos efectivos condenados a prisión perpetua son el excomisario Rubén García y el oficial Leonardo Ecilapé, mientras que los otros dos oficiales, Mariano Ibáñez y Manuel Monreal, fueron penados con 15 años de cárcel, dio a conocer este mediodía la jueza Carolina Crispiani al leer la sentencia. El 17 de mayo los policías fueron encontrados culpables por un jurado popular por el crimen de Aníbal Suárez, Danilo Sansone, Camila López y Gonzalo Domínguez, así como también por las lesiones a Rocío Quagliariello. Un jurado integrado por 12 personas confirmó que García y Ecilape eran culpables del delito de "homicidio agravado por el abuso de la función o cargo policial, y por ser cometido mediante arma de fuego". En tanto, Ibáñez y Monreal fueron condenados por "tentativa de homicidio agravado por el abuso de la función o cargo policial, y por ser cometido mediante arma de fuego". Masacre del Monte: ¿qué pasó? Se juzgó aquí a los cuatro policías bonaerenses acusados por las muertes de Camila López, Danilo Sansone, Gonzalo Domínguez y Anibal Suárez (el único mayor de edad, con 22 años). Y por lo ocurrido con Rocío Quagliarello quien resultó gravemente herida pero sobrevivió al choque del Fiat 147, en el que los jóvenes paseaban alrededor de la Laguna de Monte durante la medianoche del 19 de mayo de 2019. El coche se partió al medio al estrellarse contra el acoplado de un camión estacionado en la esquina de Pablo Nolasco y 9 de Julio, sobre la colectora de la Ruta 3. “Está acreditado que este hecho no tiene que ver con un accidente vial, y lo fuimos probando, pero ellos fueron cambiando su versión de los hechos a medida que pasaban los testigos”, sentenció durante el juicio la abogada Dora Bernárdez, quien representa a las familias de Gonzalo y Aníbal. Adentro, en el recinto, y una vez que estuvieron ubicados los abogados de las partes y sus familiares, la jueza Carolina Crispiani hizo entrar a los imputados: tres jóvenes oficiales Leonardo Ecilape, Mariano Ibáñez y Manuel Monreal y al excomisario Rubén García. Los imputados ingresaron a las 10:30, con un halo de liviandad al caminar, como desafiando a sus destinos. Luego ingresó el jurado, doce integrantes más seis suplentes. Entonces, la jueza comenzó a leer la instrucción.' , '1996-12-31 23:59:59', 1);

INSERT INTO Articulo(idUsuario, titulo, contenido, fecha_publicacion, estado)
VALUES (3, 'La advertencia sobre la continuidad de Massa en el gobierno', 'Cecilia Moreau apuntó a Daniel Scioli y criticó las PASO: "Le hace daño a la Argentina"', 'La presidenta de la Cámara de Diputados pidió ordenar el Frente de Todos de manera urgente y aseguró que suscribe con la idea de los gobernadores y organizaciones sociales de la importancia de establecer un candidato de unidad. La presidenta de la Cámara de Diputados y referente de Frente Renovador, Cecilia Moreau, pidió ordenar rápidamente el Frente de Todos y avanzar hacia las elecciones primarias con una lista de unidad. Criticó con dureza a Daniel Scioli, dijo que su candidatura "le hace daño a la Argentina" y lanzó una fuerte advertencia sobre el futuro de Sergio Massa: "No puede ser ministro de Economía de un gobierno que se tira barbaridades por los medios". Por AM750, la diputada aseguró la necesidad de lograr una lista de unidad no se debe únicamente a una cuestión de estrategia política, sino que el hecho de no ir a unas PASO es fundamental para ordenar la economía y evitar cimbronazos. Esto explica la contundencia de su opinión sobre la postulación de Daniel Scioli, que aseguró que no va a bajar su candidatura de ninguna manera. “Le hace daño a la Argentina”, apuntó sobre la estrategia del embajador en Brasil. Además, fue muy precisa al señalar que “Sergio Massa no puede ser ministro de Economía de un Gobierno que se está tirando por los medios barbaridades en una PASO cuando la estabilidad económica está en riesgo”. Y, tras asegurar que su continuidad en el puesto es una decisión personal que depende pura y exclusivamente del tigrense, pidió comprender que lo que está en juego no es el resultado electoral, sino el futuro del país. “Veo a muchos haciéndose los cocoritos. Son los mismos que 15 días decían que iban a esperar a ver qué quería hacer Cristina. Cristina no dijo nada porque estoy segura de que está preocupada por ver cómo llegamos con la situación económica”, agregó. Luego, sumó: “Los gobernadores, que piden una lista de unidad, no hablan en nombre de sí mismos. Tienen una lógica política atrás que los viene sosteniendo. Yo ayer hablé con compañeros de movimientos sociales y están todos en lo mismo”. Finalmente, sobre la relación entre el Frente Renovador y La Cámpora, apuntó: “Tenemos una relación de trabajo y de construcción de estrategia política sobre lo que todos los días nos ocupa muy importante”. “Acá hay que correrlo al Presidente del medio. Él debe ser el que llame al diálogo en estos días que quedan para construir el programa. Las bravuconadas no sirven”, concluyó en un minucioso análisis del panorama electoral. ' , '1996-12-31 23:59:59', 1);

INSERT INTO Articulo(idUsuario, titulo, contenido, fecha_publicacion, estado)
VALUES (3, 'ajsdnkajsdnkaj','aksdkalsdk','kajsndjkasndkjnkasjdajsndkasjdn' , '1996-12-31 23:59:59', 1);

-- estado en falso
INSERT INTO Articulo(idUsuario, titulo, contenido, fecha_publicacion, estado)
VALUES (2, 'asdñkasñod','asdpokasdokasdo','ajsdnkajsdnkajasdaksdm kjnaskjanskjnckkajsndkasjdn' , '1996-12-31 23:59:59', 0);

DELETE FROM Articulo WHERE estado=0;

-- Agregar el comando necesario para listar todos los artículos que tengan
-- comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
-- nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho
-- comentario, agrupados por artículos.
SELECT titulo, fecha_publicacion FROM Articulo
LEFT JOIN Comentario ON Articulo.idArticulo = Comentario.idArticulo
GROUP BY Articulo;

SELECT idEmpleado,apPaterno,fechCambio,nombreTienda
FROM (
    SELECT FK_idEmpleado,
    FROM empleado_tienda
    GROUP BY 1  
) c1 JOIN empleado_tienda
USING(FK_idEmpleado,fechCambio)
JOIN empleado ON FK_idEmpleado=idEmpleado
JOIN tienda ON FK_idTienda=idTienda;


------------------------------------------
-- DML para Comentario
------------------------------------------
INSERT INTO Comentario(idArticulo, idUsuario, contenido, fecha_hora, estado)
VALUES (1,9,'aksmdlaksmdlaksmdlkm', '1996-12-31 23:59:59', 1);

INSERT INTO Comentario(idArticulo, idUsuario, contenido, fecha_hora, estado)
VALUES (1,8,'alskdmalksdmlaksmdlalskdmlkasmd', '1996-12-31 23:59:59', 1);

INSERT INTO Comentario(idArticulo, idUsuario, contenido, fecha_hora, estado)
VALUES (1,5,'alskdmlaksd', '1996-12-31 23:59:59', 1);

INSERT INTO Comentario(idArticulo, idUsuario, contenido, fecha_hora, estado)
VALUES (2,7,'asdaksdjkasjdaksjd', '1996-12-31 23:59:59', 1);

INSERT INTO Comentario(idArticulo, idUsuario, contenido, fecha_hora, estado)
VALUES (2,6,'asdaksuhdkasjhd', '1996-12-31 23:59:59', 1);


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


