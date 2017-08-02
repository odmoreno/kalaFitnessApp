-- MySQL dump 10.13  Distrib 5.5.45, for Win64 (x86)
--
-- Host: localhost    Database: gestionhc
-- ------------------------------------------------------
-- Server version	5.5.45-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=125 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add message',1,'add_message'),(2,'Can change message',1,'change_message'),(3,'Can delete message',1,'delete_message'),(4,'Can add log entry',2,'add_logentry'),(5,'Can change log entry',2,'change_logentry'),(6,'Can delete log entry',2,'delete_logentry'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add user',5,'add_user'),(14,'Can change user',5,'change_user'),(15,'Can delete user',5,'delete_user'),(16,'Can add content type',6,'add_contenttype'),(17,'Can change content type',6,'change_contenttype'),(18,'Can delete content type',6,'delete_contenttype'),(19,'Can add session',7,'add_session'),(20,'Can change session',7,'change_session'),(21,'Can delete session',7,'delete_session'),(22,'Can add rol',8,'add_rol'),(23,'Can change rol',8,'change_rol'),(24,'Can delete rol',8,'delete_rol'),(25,'Can add usuario',9,'add_usuario'),(26,'Can change usuario',9,'change_usuario'),(27,'Can delete usuario',9,'delete_usuario'),(28,'Can add empresa',10,'add_empresa'),(29,'Can change empresa',10,'change_empresa'),(30,'Can delete empresa',10,'delete_empresa'),(31,'Can add personal',11,'add_personal'),(32,'Can change personal',11,'change_personal'),(33,'Can delete personal',11,'delete_personal'),(34,'Can add paciente',12,'add_paciente'),(35,'Can change paciente',12,'change_paciente'),(36,'Can delete paciente',12,'delete_paciente'),(37,'Can add paciente personal',13,'add_pacientepersonal'),(38,'Can change paciente personal',13,'change_pacientepersonal'),(39,'Can delete paciente personal',13,'delete_pacientepersonal'),(40,'Can add facturas',14,'add_facturas'),(41,'Can change facturas',14,'change_facturas'),(42,'Can delete facturas',14,'delete_facturas'),(43,'Can add subrutina',15,'add_subrutina'),(44,'Can change subrutina',15,'change_subrutina'),(45,'Can delete subrutina',15,'delete_subrutina'),(46,'Can add rutina',16,'add_rutina'),(47,'Can change rutina',16,'change_rutina'),(48,'Can delete rutina',16,'delete_rutina'),(49,'Can add diagnostico',17,'add_diagnostico'),(50,'Can change diagnostico',17,'change_diagnostico'),(51,'Can delete diagnostico',17,'delete_diagnostico'),(52,'Can add log entry',1,'add_logentry'),(53,'Can change log entry',1,'change_logentry'),(54,'Can delete log entry',1,'delete_logentry'),(55,'Can add group',11,'add_group'),(56,'Can change group',11,'change_group'),(57,'Can delete group',11,'delete_group'),(58,'Can add permission',21,'add_permission'),(59,'Can change permission',21,'change_permission'),(60,'Can delete permission',21,'delete_permission'),(61,'Can add user',31,'add_user'),(62,'Can change user',31,'change_user'),(63,'Can delete user',31,'delete_user'),(64,'Can add content type',41,'add_contenttype'),(65,'Can change content type',41,'change_contenttype'),(66,'Can delete content type',41,'delete_contenttype'),(67,'Can add session',51,'add_session'),(68,'Can change session',51,'change_session'),(69,'Can delete session',51,'delete_session'),(70,'Can add message',61,'add_message'),(71,'Can change message',61,'change_message'),(72,'Can delete message',61,'delete_message'),(73,'Can add rol',71,'add_rol'),(74,'Can change rol',71,'change_rol'),(75,'Can delete rol',71,'delete_rol'),(76,'Can add usuario',81,'add_usuario'),(77,'Can change usuario',81,'change_usuario'),(78,'Can delete usuario',81,'delete_usuario'),(79,'Can add empresa',91,'add_empresa'),(80,'Can change empresa',91,'change_empresa'),(81,'Can delete empresa',91,'delete_empresa'),(82,'Can add paciente',101,'add_paciente'),(83,'Can change paciente',101,'change_paciente'),(84,'Can delete paciente',101,'delete_paciente'),(85,'Can add paciente personal',111,'add_pacientepersonal'),(86,'Can change paciente personal',111,'change_pacientepersonal'),(87,'Can delete paciente personal',111,'delete_pacientepersonal'),(88,'Can add personal',121,'add_personal'),(89,'Can change personal',121,'change_personal'),(90,'Can delete personal',121,'delete_personal'),(91,'Can add facturas',131,'add_facturas'),(92,'Can change facturas',131,'change_facturas'),(93,'Can delete facturas',131,'delete_facturas'),(94,'Can add diagnostico',141,'add_diagnostico'),(95,'Can change diagnostico',141,'change_diagnostico'),(96,'Can delete diagnostico',141,'delete_diagnostico'),(97,'Can add subrutina',142,'add_subrutina'),(98,'Can change subrutina',142,'change_subrutina'),(99,'Can delete subrutina',142,'delete_subrutina'),(100,'Can add rutina',143,'add_rutina'),(101,'Can change rutina',143,'change_rutina'),(102,'Can delete rutina',143,'delete_rutina'),(104,'Can add ficha',24,'add_ficha'),(114,'Can change ficha',24,'change_ficha'),(124,'Can delete ficha',24,'delete_ficha');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'bcrypt_sha256$$2b$12$C0JX2lxfyZyxpaPQJbQFaODDrMWCGHyeq/Q8VAJ2JKT0sHeOLRbqe','2017-07-26 20:31:40',1,'0987654321','','','admin@admin.com',1,1,'2017-07-17 23:58:46'),(2,'bcrypt_sha256$$2b$12$lXFIvvqCHL.v5lOQyPVdceV0Xc.wDXuhU6C2ianpGyu5fk4Ls/TxO',NULL,0,'0999999999','','','',0,1,'2017-07-18 02:35:56'),(3,'bcrypt_sha256$$2b$12$1AeFFvyeIsioxPKC18Ynh.3btc4dlU7z15ywLrgdyqb6cy1uW.vN2',NULL,0,'0852585258','','','',0,1,'2017-07-18 02:36:59'),(4,'bcrypt_sha256$$2b$12$Tzv3gTtepU1DPNn5qqD8NuFET5FPsEy1IF68ciQh58d6xmpp3/lJS',NULL,0,'0921587454','','','',0,1,'2017-07-18 02:39:06'),(5,'bcrypt_sha256$$2b$12$Gpn0N/zy.WwvhfZHlxWH6OjI2HMMtDEYe7/4.S03d3kj.PoDw7SZG',NULL,0,'4545454454','','','',0,1,'2017-07-18 02:47:17'),(104,'bcrypt_sha256$$2b$12$9LOi/brAUGGyxeXvIi7X1u3F6W79/wXAdpSalEojZWnxQu5KUIc2y',NULL,0,'0999958748','','','',0,1,'2017-07-26 20:59:28'),(124,'bcrypt_sha256$$2b$12$uCWOp1ooanT.MALSyUkHCekO3qARhG67AtMR2KiY8O9jQ/UrEKxrC',NULL,0,'0999958742','','','',0,1,'2017-07-26 21:22:45'),(134,'bcrypt_sha256$$2b$12$f/LT0rfd0tOGM4a9H1iAPOkyD/8GLfBGyxjg35sIVsDefw3GvHj2G','2017-07-28 02:21:37',1,'carlos','','','cmanosalvas95@gmail.com',1,1,'2017-07-28 02:21:05');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnostico`
--

DROP TABLE IF EXISTS `diagnostico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagnostico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `condiciones_previas` varchar(1000) NOT NULL,
  `area_afectada` varchar(1000) NOT NULL,
  `receta` varchar(1000) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  `personal_id` int(11) NOT NULL,
  `rutina_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rutina_id` (`rutina_id`),
  KEY `diagnostico_paciente_id_c0f000a3_fk_paciente_id` (`paciente_id`),
  KEY `diagnostico_personal_id_7e42c766_fk_personal_id` (`personal_id`),
  CONSTRAINT `diagnostico_paciente_id_c0f000a3_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`),
  CONSTRAINT `diagnostico_personal_id_7e42c766_fk_personal_id` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`id`),
  CONSTRAINT `diagnostico_rutina_id_05f8c41c_fk_rutina_id` FOREIGN KEY (`rutina_id`) REFERENCES `rutina` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnostico`
--

LOCK TABLES `diagnostico` WRITE;
/*!40000 ALTER TABLE `diagnostico` DISABLE KEYS */;
INSERT INTO `diagnostico` VALUES (4,'2017-07-21 07:26:06','2017-07-21 07:33:59','sd','asd','as','I',1,1,7),(14,'2017-07-21 07:34:11','2017-07-21 07:38:54','dv','c4','c2','A',1,1,8),(24,'2017-07-25 00:14:06','2017-07-25 00:14:06','q','q','q','A',1,1,9),(34,'2017-07-25 00:14:22','2017-07-25 00:14:22','78','78','78','A',1,1,10),(44,'2017-07-25 00:14:34','2017-07-25 00:14:34','45','45','45','A',1,1,11),(54,'2017-07-25 00:14:46','2017-07-25 00:52:57','nm','nm','nm','A',1,1,12),(64,'2017-07-25 00:15:02','2017-07-25 00:15:02','nmq','nm','n','A',1,1,13),(74,'2017-07-25 00:15:18','2017-07-25 00:15:18','lksdff','nd','nd','A',1,1,14),(84,'2017-07-25 00:15:33','2017-07-25 00:42:30','hj','h','h','A',1,1,15),(94,'2017-07-25 00:15:47','2017-07-25 00:15:47','qw','qw','qw','A',1,1,16),(104,'2017-07-25 00:16:00','2017-07-25 00:16:00','sdf','sd','sdf','A',1,1,17),(114,'2017-07-25 00:16:20','2017-07-25 00:16:20','34','34','23','A',1,1,18),(124,'2017-07-25 00:20:46','2017-07-25 00:21:21','kj','kj','jhj','I',1,1,19),(134,'2017-07-25 00:21:34','2017-07-25 00:21:34','jk','jk','kj','A',1,1,20),(144,'2017-07-26 21:24:41','2017-07-26 21:25:44','','','','I',4,1,4);
/*!40000 ALTER TABLE `diagnostico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `directmessaging_message`
--

DROP TABLE IF EXISTS `directmessaging_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `directmessaging_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `sent_at` datetime DEFAULT NULL,
  `read_at` datetime DEFAULT NULL,
  `recipient_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `directmessaging_message_recipient_id_0a60168e_fk_auth_user_id` (`recipient_id`),
  KEY `directmessaging_message_sender_id_87e5f147_fk_auth_user_id` (`sender_id`),
  CONSTRAINT `directmessaging_message_recipient_id_0a60168e_fk_auth_user_id` FOREIGN KEY (`recipient_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `directmessaging_message_sender_id_87e5f147_fk_auth_user_id` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directmessaging_message`
--

LOCK TABLES `directmessaging_message` WRITE;
/*!40000 ALTER TABLE `directmessaging_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `directmessaging_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'directmessaging','message'),(2,'admin','logentry'),(3,'auth','group'),(4,'auth','permission'),(5,'auth','user'),(6,'contenttypes','contenttype'),(7,'sessions','session'),(8,'kalaapp','rol'),(9,'kalaapp','usuario'),(10,'kalaapp','empresa'),(11,'personal','personal'),(12,'paciente','paciente'),(13,'paciente','pacientepersonal'),(14,'factura','facturas'),(15,'diagnostico','subrutina'),(16,'diagnostico','rutina'),(17,'diagnostico','diagnostico'),(24,'fisioterapia','ficha');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=285 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (4,'contenttypes','0001_initial','2017-07-20 02:55:56'),(14,'auth','0001_initial','2017-07-20 02:56:23'),(24,'admin','0001_initial','2017-07-20 02:56:31'),(34,'admin','0002_logentry_remove_auto_add','2017-07-20 02:56:33'),(44,'contenttypes','0002_remove_content_type_name','2017-07-20 02:56:36'),(54,'auth','0002_alter_permission_name_max_length','2017-07-20 02:56:37'),(64,'auth','0003_alter_user_email_max_length','2017-07-20 02:56:39'),(74,'auth','0004_alter_user_username_opts','2017-07-20 02:56:40'),(84,'auth','0005_alter_user_last_login_null','2017-07-20 02:56:41'),(94,'auth','0006_require_contenttypes_0002','2017-07-20 02:56:42'),(104,'auth','0007_alter_validators_add_error_messages','2017-07-20 02:56:43'),(114,'auth','0008_alter_user_username_max_length','2017-07-20 02:56:44'),(124,'kalaapp','0001_initial','2017-07-20 02:57:14'),(134,'personal','0001_initial','2017-07-20 02:57:19'),(144,'paciente','0001_initial','2017-07-20 02:57:33'),(154,'diagnostico','0001_initial','2017-07-20 02:57:58'),(164,'directmessaging','0001_initial','2017-07-20 02:58:05'),(174,'factura','0001_initial','2017-07-20 02:58:17'),(184,'sessions','0001_initial','2017-07-20 02:58:20'),(194,'factura','0002_auto_20170720_0846','2017-07-21 05:29:13'),(204,'factura','0003_auto_20170720_1644','2017-07-21 05:29:14'),(214,'fisioterapia','0001_initial','2017-07-21 20:17:39'),(224,'fisioterapia','0002_auto_20170720_0250','2017-07-21 20:18:01'),(234,'fisioterapia','0003_auto_20170720_0502','2017-07-21 20:18:02'),(244,'fisioterapia','0004_auto_20170720_0503','2017-07-21 20:18:03'),(254,'fisioterapia','0005_auto_20170720_0504','2017-07-21 20:18:04'),(264,'fisioterapia','0006_auto_20170720_0505','2017-07-21 20:18:05'),(274,'fisioterapia','0007_auto_20170720_0506','2017-07-21 20:18:11'),(284,'fisioterapia','0008_auto_20170720_0522','2017-07-21 20:18:11');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('a8r721mqzkhv0rruhep5kmgh37rvx2de','ZjEzODU0NzE1MmM2NjYzYmNhNzU2ZDRiNDI5NDM1MmQzYjg5MzRmYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjRlZDk5YTBjYTk4MDE5Y2NlYWMxNTI5ZjY3MmZmMDI0YjU0NzcwZGUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-08-03 03:00:28'),('btlmhflf2cnmvavxya2jo9b1lzesuq7g','ZmM3Njg5NTEyMTRkNmVjYTc5MjBmN2VhYWJmMWVkMWFhNDYzOTU5NDp7Il9hdXRoX3VzZXJfaGFzaCI6IjFiZjFjZGQ3OWFiMmNmZGM1Y2RhZTk2Nzc1YjIxYzVlZjI2MDUyNjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMzQifQ==','2017-08-11 02:21:37'),('hrsum9wp2fh9fpmpupyr1g5l5we33rrs','ZjEzODU0NzE1MmM2NjYzYmNhNzU2ZDRiNDI5NDM1MmQzYjg5MzRmYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjRlZDk5YTBjYTk4MDE5Y2NlYWMxNTI5ZjY3MmZmMDI0YjU0NzcwZGUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-08-09 20:31:40');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `razon_social` varchar(200) DEFAULT NULL,
  `propietario_nombre` varchar(200) DEFAULT NULL,
  `propietario_apellido` varchar(200) DEFAULT NULL,
  `ruc` varchar(50) NOT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `iva` int(11) NOT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,'2017-07-17 23:55:08','2017-07-17 23:55:08','Kala Fitness','Kala Fitness','ABC','XYZ','0999999999001','0987665432','Urdesa central',12,'A');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas`
--

DROP TABLE IF EXISTS `facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `facturas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `serie` varchar(25) NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `total` double NOT NULL,
  `estado` varchar(1) NOT NULL,
  `empresa_id` int(11) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `serie` (`serie`),
  KEY `facturas_empresa_id_1231f80e_fk_empresa_id` (`empresa_id`),
  KEY `facturas_paciente_id_504dec4c_fk_paciente_id` (`paciente_id`),
  CONSTRAINT `facturas_empresa_id_1231f80e_fk_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `empresa` (`id`),
  CONSTRAINT `facturas_paciente_id_504dec4c_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=215 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas`
--

LOCK TABLES `facturas` WRITE;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
INSERT INTO `facturas` VALUES (14,'2017-07-18 03:29:08','2017-07-23 23:45:18','1','2017-07-17',100,'I',1,1),(24,'2017-07-21 02:58:25','2017-07-21 02:58:25','234234424234','2017-07-23',1.64,'A',1,1),(34,'2017-07-21 03:02:01','2017-07-21 03:02:01','12332','2017-07-20',1.23,'A',1,1),(44,'2017-07-21 03:05:30','2017-07-21 03:05:30','2342342424','2018-10-15',34,'A',1,1),(54,'2017-07-23 23:46:44','2017-07-23 23:46:44','42323','2017-07-23',1.18,'A',1,1),(64,'2017-07-25 01:10:51','2017-07-25 01:10:51','234234234','2017-07-24',1.04,'A',1,1),(74,'2017-07-25 01:11:36','2017-07-25 01:11:36','234242451','2017-07-24',1.02,'A',1,1),(84,'2017-07-25 01:11:57','2017-07-25 01:11:57','22212','2017-07-31',1.2,'A',1,1),(94,'2017-07-25 01:12:22','2017-07-25 01:12:22','44745646','2017-07-24',1.04,'A',1,1),(104,'2017-07-25 01:13:25','2017-07-25 01:13:25','313','2017-07-24',1.14,'A',1,1),(114,'2017-07-25 01:13:44','2017-07-25 01:13:44','86857464','2017-07-28',1.2,'A',1,1),(124,'2017-07-25 01:14:14','2017-07-25 01:14:14','44745646999','2017-07-24',3,'A',1,1),(134,'2017-07-25 01:14:55','2017-07-25 01:14:55','2221287','2017-07-24',2323,'A',1,1),(144,'2017-07-26 15:11:41','2017-07-26 15:11:41','213123123','2018-07-26',1.21,'A',1,2),(154,'2017-07-26 21:06:30','2017-07-26 21:06:30','555555','2018-12-04',23,'A',1,1),(164,'2017-07-26 21:09:19','2017-07-26 21:09:19','55555','2018-12-04',10000,'A',1,1),(174,'2017-07-26 21:10:21','2017-07-26 21:10:21','4555','2018-12-04',22358,'A',1,1),(184,'2017-07-26 21:12:07','2017-07-26 21:12:07','5555555555555','2018-12-04',23.55,'A',1,1),(204,'2017-07-26 21:13:44','2017-07-26 21:15:30','000000000','2018-12-04',1.47,'I',1,1),(214,'2017-07-26 21:14:26','2017-07-26 21:15:10','2345555555555555555555555','2018-12-04',23,'I',1,1);
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ficha`
--

DROP TABLE IF EXISTS `ficha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ficha` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `fecha` date NOT NULL,
  `altura` double DEFAULT NULL,
  `peso` double DEFAULT NULL,
  `imc` double DEFAULT NULL,
  `musculo` double DEFAULT NULL,
  `grasa_visceral` double DEFAULT NULL,
  `grasa_porcentaje` double DEFAULT NULL,
  `cuello` double DEFAULT NULL,
  `hombros` double DEFAULT NULL,
  `pecho` double DEFAULT NULL,
  `brazo_derecho` double DEFAULT NULL,
  `brazo_izquierdo` double DEFAULT NULL,
  `antebrazo_derecho` double DEFAULT NULL,
  `antebrazo_izquierdo` double DEFAULT NULL,
  `cintura` double DEFAULT NULL,
  `cadera` double DEFAULT NULL,
  `muslo_derecho` double DEFAULT NULL,
  `muslo_izquierdo` double DEFAULT NULL,
  `pantorrilla_derecha` double DEFAULT NULL,
  `pantorrilla_izquierda` double DEFAULT NULL,
  `paciente_id` int(11) NOT NULL,
  `personal_id` int(11) NOT NULL,
  `abdomen_alto` smallint(5) unsigned NOT NULL,
  `abdomen_bajo` smallint(5) unsigned NOT NULL,
  `espinales` smallint(5) unsigned NOT NULL,
  `flexiones` smallint(5) unsigned NOT NULL,
  `lumbares` smallint(5) unsigned NOT NULL,
  `saltoLargo` smallint(5) unsigned NOT NULL,
  `sentadillas` smallint(5) unsigned NOT NULL,
  `suspension` varchar(200) NOT NULL,
  `trenInferior` time NOT NULL,
  `trenSuperior` time NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ficha_paciente_id_f72260d9_fk_paciente_id` (`paciente_id`),
  KEY `ficha_personal_id_55599894_fk_personal_id` (`personal_id`),
  CONSTRAINT `ficha_paciente_id_f72260d9_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`),
  CONSTRAINT `ficha_personal_id_55599894_fk_personal_id` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ficha`
--

LOCK TABLES `ficha` WRITE;
/*!40000 ALTER TABLE `ficha` DISABLE KEYS */;
INSERT INTO `ficha` VALUES (4,'2017-07-21 22:18:36','2017-07-21 22:18:36','2017-07-21',11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,'baja','00:00:00','00:00:00'),(14,'2017-07-21 23:34:46','2017-07-21 23:34:46','2017-07-21',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,'baja','00:00:00','00:00:00'),(24,'2017-07-21 23:36:24','2017-07-21 23:36:24','2017-07-21',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,'baja','00:00:00','00:00:00');
/*!40000 ALTER TABLE `ficha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paciente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `n_hijos` smallint(5) unsigned NOT NULL,
  `observaciones` varchar(200) NOT NULL,
  `motivo_consulta` varchar(200) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  UNIQUE KEY `paciente_id_usuario_id_682ad907_uniq` (`id`,`usuario_id`),
  CONSTRAINT `paciente_usuario_id_f988892d_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES (1,'2017-07-18 02:35:57','2017-07-18 02:35:57',0,' ',' ','A',1),(2,'2017-07-18 02:35:57','2017-07-18 02:35:57',1,' ',' ','A',2),(4,'2017-07-26 20:59:29','2017-07-26 20:59:29',0,'','','A',14);
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente_personal`
--

DROP TABLE IF EXISTS `paciente_personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paciente_personal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `estado` varchar(1) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  `personal_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paciente_personal_paciente_id_95dfbd3a_fk_paciente_id` (`paciente_id`),
  KEY `paciente_personal_personal_id_f819ef30_fk_personal_id` (`personal_id`),
  CONSTRAINT `paciente_personal_paciente_id_95dfbd3a_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`),
  CONSTRAINT `paciente_personal_personal_id_f819ef30_fk_personal_id` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente_personal`
--

LOCK TABLES `paciente_personal` WRITE;
/*!40000 ALTER TABLE `paciente_personal` DISABLE KEYS */;
INSERT INTO `paciente_personal` VALUES (4,'2017-07-26 21:16:21','2017-07-26 21:16:21','A',1,1),(24,'2017-07-26 21:16:21','2017-07-26 21:16:21','A',4,1),(34,'2017-07-26 21:17:13','2017-07-26 21:17:13','A',2,1);
/*!40000 ALTER TABLE `paciente_personal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal`
--

DROP TABLE IF EXISTS `personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `estado` varchar(1) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  UNIQUE KEY `personal_id_usuario_id_0ae164d5_uniq` (`id`,`usuario_id`),
  CONSTRAINT `personal_usuario_id_0f2b7609_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal`
--

LOCK TABLES `personal` WRITE;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` VALUES (1,'2017-07-18 02:35:57','2017-07-18 02:35:57','A',3);
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `tipo` varchar(30) NOT NULL,
  `es_personal` tinyint(1) NOT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (1,'2017-07-17 10:00:00','2017-07-17 10:00:00','administrador',0,'A'),(2,'2017-07-17 10:00:00','2017-07-26 21:22:45','paciente',0,'A'),(3,'2017-07-17 10:00:00','2017-07-17 10:00:00','nutricionista',1,'A'),(4,'2017-07-17 10:00:00','2017-07-17 10:00:00','fisioterapista',1,'A');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rutina`
--

DROP TABLE IF EXISTS `rutina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rutina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rutina`
--

LOCK TABLES `rutina` WRITE;
/*!40000 ALTER TABLE `rutina` DISABLE KEYS */;
INSERT INTO `rutina` VALUES (4,'2017-07-26 21:24:41','2017-07-26 21:24:41','A');
/*!40000 ALTER TABLE `rutina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rutina_subrutina`
--

DROP TABLE IF EXISTS `rutina_subrutina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rutina_subrutina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rutina_id` int(11) NOT NULL,
  `subrutina_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rutina_subrutina_rutina_id_subrutina_id_0bc814a3_uniq` (`rutina_id`,`subrutina_id`),
  KEY `rutina_subrutina_subrutina_id_a015a5f2_fk_subrutina_id` (`subrutina_id`),
  CONSTRAINT `rutina_subrutina_rutina_id_59e44e86_fk_rutina_id` FOREIGN KEY (`rutina_id`) REFERENCES `rutina` (`id`),
  CONSTRAINT `rutina_subrutina_subrutina_id_a015a5f2_fk_subrutina_id` FOREIGN KEY (`subrutina_id`) REFERENCES `subrutina` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rutina_subrutina`
--

LOCK TABLES `rutina_subrutina` WRITE;
/*!40000 ALTER TABLE `rutina_subrutina` DISABLE KEYS */;
INSERT INTO `rutina_subrutina` VALUES (4,4,4);
/*!40000 ALTER TABLE `rutina_subrutina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subrutina`
--

DROP TABLE IF EXISTS `subrutina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subrutina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `nombre` varchar(1000) NOT NULL,
  `detalle` varchar(1000) NOT NULL,
  `veces` smallint(5) unsigned NOT NULL,
  `repeticiones` smallint(5) unsigned NOT NULL,
  `descanso` smallint(5) unsigned NOT NULL,
  `link` varchar(500) NOT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subrutina`
--

LOCK TABLES `subrutina` WRITE;
/*!40000 ALTER TABLE `subrutina` DISABLE KEYS */;
INSERT INTO `subrutina` VALUES (4,'2017-07-26 21:24:41','2017-07-26 21:24:41','caminata','caminata x 60 minutos',2,1,45,'http://google.ec','A');
/*!40000 ALTER TABLE `subrutina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `cedula` varchar(10) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `ocupacion` varchar(200) DEFAULT NULL,
  `genero` varchar(1) DEFAULT NULL,
  `edad` smallint(5) unsigned DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `estado_civil` varchar(30) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `rol_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula` (`cedula`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  KEY `usuario_rol_id_ac58b608_fk_rol_id` (`rol_id`),
  CONSTRAINT `usuario_rol_id_ac58b608_fk_rol_id` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`),
  CONSTRAINT `usuario_usuario_id_806a6575_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'2017-07-18 02:35:57','2017-07-18 02:35:57','carola','toledo','0999999999','cl sta','0987654125','enfermera','F',34,NULL,'usuario/noimagen.jpg','Soltero','A',11,11),(2,'2017-07-18 02:37:00','2017-07-18 02:37:00','javier','moran','0852585258','puente alto','012454544','traumatologo','H',38,NULL,'usuario/noimagen.jpg','Soltero','A',11,21),(3,'2017-07-18 02:39:07','2017-07-18 02:39:07','christian','jaramillo','0921587454','el condor','098653210','analista','H',99,NULL,'usuario/noimagen.jpg','Soltero','A',31,31),(4,'2017-07-18 02:47:17','2017-07-18 02:47:17','pablo','kea','4545454454','kkjkjjk','444578787','oooi','H',21,NULL,'usuario/noimagen.jpg','Soltero','A',31,41),(14,'2017-07-26 20:59:29','2017-07-26 20:59:29','Carlos','Manosalvas','0999958748','Todo','0212665','fisioterapista','M',18,NULL,'usuario/noimagen.jpg','Soltero','A',2,104),(24,'2017-07-26 21:22:45','2017-07-26 21:22:45','Carlos','EL HUevo','0999958742','Alborada','2340082','Huevear','x',300,NULL,'usuario/noimagen.jpg','Soltero','A',2,124);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-28  7:17:41
