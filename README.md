# Proyecto-Final
-Instrucciones para que la aplicación funcione, es requerido que ejecutes el siguiente comando:
pip install -r requirements.txt;

Esto instalará la librería de social_share. La alternativa es ejecutar: pip install django-social-share;

Una vez hecho todo esto, haz las migraciones.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
El proyecto final del grupo 8 de la comisión 6 del informatorio.

Nos reunimos el día siguiente a la formación de los grupos para organizarnos y prepararnos para iniciar el proyecto en conjunto; nos dividimos en subgrupos.
Fecha de Inicio del proyecto: 05/08/2021.

Día 1). Un grupo se encargó de buscar la informacion, formular las preguntas y las posibles respuestas, el otro de crear la landing page, la cual fue creada.

Día 2). Se usó HTML5 y CSS3 para el formulario de login y registro (pensando en su posterior modificación con Django). Se crearon las paginas de conocer al equipo y de terminos y condiciones.

Día 3). Nos volvímos a reunir para discutir acerca de por donde iniciar a usar Django, coincidimos en que empezaríamos por el Login y Registro, para luego seguir con el admin. Mockup definido.

Día 4). Nueva Reunión. Participamos los 8 de la misma, iniciamos el proyecto Django. Login, registro y las bases de datos respectivas empiezan su desarrollo.(08/08/2021)

Día 5). El desarrollo del login y Registro sigue su curso, mientras los que no están participando de esa app, siguen aprendiendo cómo hacer lo que sigue.

Día 6). Tareas reasignadas, esencialmente nos dividimos en tres grupos, Login y Registro, Visual y Admin. 
       - Grupos: 
              - Login y Registro: se encargarán del formulario de registro así como del login, para hacerlo funcional.
              - Admin: se encargarán de poner las preguntas en una base de datos y de empezar a configurar el admin.
              - Visual: se encargan de mejorar el apartado visual de la página, esencialmente, así como la interfaz del usuario, para que sea mucho más
              agradable a la vista.
              
Día 7). Más avance en materia del Login y Registro, así como en Admin, llegando a sentar las bases para las preguntas y el multiple choice. Hoy nos volvemos a reunir para trabajar más intensamente en el Login y el Registro. Página generadora de links descubierta: https://developers.facebook.com/docs/plugins/share-button/?locale=es_ES. Replanteamos un poco la estratégia en cuanto a la BBDD. A partir de mañana cargaremos las preguntas y respuestas.             

Día 8). Avances en la BBDD fueron hechos, preguntas y respuestas cargadas. Login y Registro en proceso de finalización, algunos problemas encontrados.

Día 9). Login y Admin finalizados, procedemos a iniciar a trabajar con el admin.

Día 10). Algunos problemas en el login encontrados, pero resueltos. El admin site está a medio camino, el añadido de preguntas está listo.

Día 11). Nos dedicamos a buscar cómo mejorar la carga de preguntas y respuestas.

Día 12). Carga de preguntas y respuestas terminadas, faltan los templates y darle algunos retoques.

Día 13). Hemos tenido avances en los templates de las preguntas y respuestas así como en los del login y registro.

Dia 14). Intento de completas las preguntas, no hubo mucho éxito, pero se pudo avanzar un poco.

Día 15). Problemas con los templates html para mostrar las respuestas. Funcionalidades de registrar intentos, solo mostrar una vez las preguntas y hacerlo con campos multiplechoice.

Día 16). Preguntas son cargadas junto a las respuestas, tanto las preguntas como las respuestas se muestran. Se ven las estadísticas de los jugadores así como los resultados.

Día 17). Nos reunimos para debatir qué era necesario para completar todo, algunos errores en el juego fueron corregidos por completo. Planes para agregar una barra de navegación (usando JavaScript) son discutidos. 

Día 18). El proyecto está basicamente completo, solo nos falta el mostrar estadisticas y compartir los resultados. Hoy se juntaron el login/register y el juego para así estar completo. (22/08/2021)

Día 19). Seguimos con el iniciar con la barra de navegación, estamos dando los estilos a las páginas y asegurandonos de tenerlo listo para entregar.

Esta página consiste en las siguientes partes:

 - Landing Page: contiene la vista principal de la página, dando la bienvenida a los participantes, también contiene unos botones de contacto (redes sociales)
   y el link que une esta página con la página de presentación del equipo de desarrollo.
    - Contiene el boton que lleva al login y el registro.
    - La Landing Page contiene el enlace a nuestra página de "conoce al equipo" en el fondo, en el link "Grupo 8 Informatorio" que se encuentra al lado de los
      botones de las redes sociales. 
    - La página principal(Landing page) así como la página de "conoce al equipo" fueron hechas con HTML5 y CSS3. Ningún framework de CSS3 fue utilizado.
 - Login y Registro: Inicialmente fue hecho únicamente usando HTML5 y CSS3...
    - Contiene el botón de registro o el de login (dependiendo de en cual formulario estés), además de contener un enlace a una página de "Términos y Condiciones" autogenerada de politicadeprivacidadplantilla.com
    - Contiene un botón que permite al usuario el regresar a la página anterior. 
 - Perfil de Admin:
    -  Inicia con un un login, hecho en: HTML5, CSS3 y Django.
    -  Contiene las opciones de agregar y eliminar usuarios, grupos, preguntas y respuestas así como para contabilizar las respuestas correctas.  
    -  Registra los intentos y permite colocar el puntaje máximo por pregunta respondida correctamente.
 - Perfil de Participante:
    - Pantalla de inicio con boton para iniciar.
    - Sigue con un registro y un login, hecho en: HTML5, CSS3 y Django. 
    - Una vez iniciado es redirigido a la pagina principal y luego de eso, el usuario puede jugar. 
 
 - Juego:
    - Se inició gracias a un grupo dentro del nuestro que realizó un buen trabajo de investigación para conseguir las preguntas y las respuestas, las cuales fueron consultadas con todo el equipo. 
    - Se trabajó con django y html principalmente, estuvimos trabajando bastante para conseguirlo. Cuenta con preguntas y respuestas en multiplechoice.
    - Tiene un máximo de 4 posibles respuestas, al finalizar te da la opción de consultar el tablero, el cual contiene tus resultados y los de los demás participantes.
    - Consiste de cuantas preguntas el admin quiera poner, con un mínimo y máximo de 4 respuestas, al finalizar se le da al participante la oportunidad de ver su puntaje comparándolo con los demás jugadores. 


 Participación general:
 Mockup: Federico Asis, Ulises Mariano Melgarejo, Carlos Rudaz, Keith Magin Leonel Denysiuk, Giuliano Conti, Mauricio Sosa;
 
 Preguntas y Respuestas: Keith Magin Leonel Denysiuk, Mauricio Sosa;
 
 Diseño de la página: Ulises Mariano Melgarejo, Giuliano Conti;
 
 Inicialización de proyecto Django: Carlos Rudaz;
 
 Login y registro: Carlos Rudaz;
 
 Base de datos: Ulises Mariano Melgarejo, Carlos Rudaz, Federico Asis;
 
 Admin Site: Ulises Mariano Melgarejo, Carlos Rudaz;
 
 Parte backend y frontend de Preguntas y Respuestas: Ulises Mariano Melgarejo, Federico Asis;
 
 
 
 Tecnologías utilizadas: HTML5, CSS3, Bootstrap, DJANGO, SQLITE3, JavaScript
