CREATE TABLE IF NOT EXISTS`usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contraseña` varchar(10) NOT NULL
  `creado` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
)ENGINE=InnoDB DEFAULT CHARSET = latin1 AUTO_INCREMENT=1;