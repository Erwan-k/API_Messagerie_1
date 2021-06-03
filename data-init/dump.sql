 SET NAMES utf8 ;
DROP TABLE IF EXISTS `Message`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Message` (
  `Nom` varchar(255) DEFAULT NULL,
  `Message_` varchar(255) DEFAULT NULL,
  `Date_` int(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Message` WRITE;

UNLOCK TABLES;
