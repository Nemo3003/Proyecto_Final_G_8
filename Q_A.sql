CREATE DATABASE preguntas_respuestas;
USE preguntas_respuestas;
CREATE TABLE users(
    Username_id INT AUTO_INCREMENT,
    Username
    Email varchar(100) NOT NULL,
    Passwords VARCHAR(100) NOT NULL
    PRIMARY KEY (Username_id),
)
CREATE TABLE quiz (
    id_pregunta INT NOT NULL AUTO_INCREMENT,
    Pregunta1 VARCHAR(200) NOT NULL,
    PRIMARY KEY (id_pregunta)

)
CREATE TABLE quiz_respuestas (
  id_pregunta INT,
  respuesta1 VARCHAR(200),
  respuesta2 VARCHAR(200),
  respuesta3 VARCHAR(200),
  respuesta4 VARCHAR(200),
  enviado DATE NOT NULL,
  PRIMARY KEY (username, enviado)
  FOREIGN KEY (id_pregunta) REFERENCES quiz (id_pregunta)
);