use D7_G5_blogONG;

-- DML para tablas del BLOG
-- Rol de Administrador
INSERT INTO usuario(nombre, apellido, telefono, username, email, contraseña, estado, fecha_creacion, avatar, es_publico, es_colaborador, es_admin)
values ("Marcos", "DiPalma", "3516108181", "Markitos", "marcos@gmail.com", MD5("123456"), True,"", "2023-6-5", False, False, True);

-- Roles de Colaborador
INSERT INTO usuario(nombre, apellido, telefono, username, email, contraseña, estado, fecha_creacion, avatar, es_publico, es_colaborador, es_admin)
values ("Roberto", "Gonzalez", "3516108381", "Tito", "roberto@gmail.com", MD5("987654"), True,"", "2023-6-5", False, True, False),
("José", "López", "3516108531", "Pepe", "jose@gmail.com", MD5("963215"), True,"", "2023-6-5", False, True, False),
("Pedro", "Molina", "3624223236", "Pedrito", "pedro@gmail.com", MD5("785421"), True, "", "2023-6-5", False, True, False),
("Alfredo", "Quinodoz", "3624323246", "Fredo", "alfredo@gmail.com", MD5("852145"), True,"", "2023-6-5", False, True, False);

-- Roles de Público
INSERT INTO usuario(nombre, apellido, telefono, username, email, contraseña, estado, fecha_creacion, avatar, es_publico, es_colaborador, es_admin)
values ("Alexis", "Vileta", "3625253654", "Dario", "Alexis@gmail.com", MD5("862359"), True,"","2023-6-5", True, False, False),
("Luciano", "Sosa", "3674223656", "lucho", "Luciano@gmail.com", MD5("321459"), True,"", "2023-6-5", True, False, False),
("Facundo", "Ruiz", "3624225356", "Facu", "facundo@gmail.com", MD5("784569"), True,"", "2023-6-5", True, False, False),
("Mariano", "Martinez", "3674569874", "Marianito", "mariano@gmail.com", MD5("33Mariano"), True,"", "2023-6-5", True, False, False),
("Eliseo", "Andres", "3654256598", "biblico", "eliseo@gmail.com", MD5("212156"), True,"", "2023-6-5", True, False, False);

-- Cambio de ROL de un Colaborador
UPDATE usuario SET es_admin=True, es_colaborador=False WHERE id_usuario=2;

-- Ingreso de artículos a la tabla
INSERT INTO articulo(id_usuario, titulo, resumen, contenido, fecha_publicacion, estado, imagen) 
values (3,"La Economía HOY","Un repaso por el estado Actual de la economía de estos días en el país"
,"Como todos sabemos el presente económico....", "2023-6-10 01:03:25", True, ""),
 (2,"MARTE NOS ESPERA","Declaraciones de un científico de la NASA"
,"Un científico que se encuentra desarrollando el megacombustible para naves... ", "2023-6-10 02:25:25", True, ""),
(4,"OTRA VEZ RUSIA","Nueva invasión de Rusia sobre un pequeño país"
,"El primer día de este mes el Presidente PUTIN dio la orden de iniciar la invasión...", "2023-6-10 01:03:25", True, ""),
 (2,"ELECCIONES DEL FIN DE SEMANA","Un repaso por todos los candidatos habilitados"
,"Este fin de semana se llevarán a cavo las elecciones PASO...", "2023-6-10 01:03:25", False, "");

-- Eliminando los articulos en estado FALSO
DELETE FROM articulo WHERE estado=0;

-- Agregando comentarios a los articulos

INSERT INTO comentario(id_articulo, id_usuario, contenido, fecha_hora, estado)
values (1,6,"Todos sabemos cual es la situación economica", "2023-6-10 05:12:15",True)
,(2,6,"Todavía no conocemos La tierra y vamos a ir a MARTE", "2023-6-10 05:22:15",True)
,(1,7,"El estado de la Economía es culpa de los politicos", "2023-6-10 05:23:33",True)
,(1,8,"Siempre hay alguien que se hace millonario con este estado económico", "2023-6-10 05:30:33",True)
,(2,8,"Muchos gastos para ir a Marte y en la tierra pueblos enteros se mueren de hambre", "2023-6-10 05:35:33",True);

-- listando articulos con comentarios, ordenados por artículo
SELECT articulo.titulo, articulo.fecha_publicacion, usuario.nombre, comentario.fecha_hora
FROM articulo
INNER JOIN comentario
ON comentario.id_articulo=articulo.id_articulo
INNER JOIN usuario
ON comentario.id_usuario=usuario.id_usuario
order by articulo.id_articulo