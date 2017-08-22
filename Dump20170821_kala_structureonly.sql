-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: us-cdbr-azure-southcentral-f.cloudapp.net    Database: gestionhc
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
) ENGINE=MyISAM AUTO_INCREMENT=365 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=705 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `diagnostico_fis`
--

DROP TABLE IF EXISTS `diagnostico_fis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagnostico_fis` (
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
  KEY `diagnostico_fis_paciente_id_906bfc53_fk_paciente_id` (`paciente_id`),
  KEY `diagnostico_fis_personal_id_f5891e51_fk_personal_id` (`personal_id`),
  CONSTRAINT `diagnostico_fis_personal_id_f5891e51_fk_personal_id` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`id`),
  CONSTRAINT `diagnostico_fis_paciente_id_906bfc53_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`),
  CONSTRAINT `diagnostico_rutina_id_05f8c41c_fk_rutina_id` FOREIGN KEY (`rutina_id`) REFERENCES `rutina` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=195 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `diagnostico_nut`
--

DROP TABLE IF EXISTS `diagnostico_nut`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagnostico_nut` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `condiciones_previas` varchar(1000) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `dieta_id` int(11) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  `personal_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dieta_id` (`dieta_id`),
  KEY `diagnostico_nut_paciente_id_928c1f95_fk_paciente_id` (`paciente_id`),
  KEY `diagnostico_nut_personal_id_81202fa4_fk_personal_id` (`personal_id`),
  CONSTRAINT `diagnostico_nut_personal_id_81202fa4_fk_personal_id` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`id`),
  CONSTRAINT `diagnostico_nut_dieta_id_32b27952_fk_dieta_id` FOREIGN KEY (`dieta_id`) REFERENCES `dieta` (`id`),
  CONSTRAINT `diagnostico_nut_paciente_id_928c1f95_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dieta`
--

DROP TABLE IF EXISTS `dieta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dieta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `estado` varchar(1) NOT NULL,
  `descripcion` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=175 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=MyISAM AUTO_INCREMENT=95 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=435 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ficha_nutricion`
--

DROP TABLE IF EXISTS `ficha_nutricion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ficha_nutricion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `lacteos` varchar(200) NOT NULL,
  `vegetales` varchar(200) NOT NULL,
  `frutas` varchar(200) NOT NULL,
  `cho` varchar(200) NOT NULL,
  `carnes` varchar(200) NOT NULL,
  `comidas_rapidas` varchar(200) NOT NULL,
  `frituras` varchar(200) NOT NULL,
  `enlatados` varchar(200) NOT NULL,
  `gaseosas` varchar(200) NOT NULL,
  `energizantes` varchar(200) NOT NULL,
  `infusiones` varchar(200) NOT NULL,
  `lacteos_input` varchar(20) NOT NULL,
  `vegetales_input` varchar(20) NOT NULL,
  `frutas_input` varchar(20) NOT NULL,
  `cho_input` varchar(20) NOT NULL,
  `carnes_input` varchar(20) NOT NULL,
  `comidas_rapidas_input` varchar(20) NOT NULL,
  `frituras_input` varchar(20) NOT NULL,
  `enlatados_input` varchar(20) NOT NULL,
  `gaseosas_input` varchar(20) NOT NULL,
  `energizantes_input` varchar(20) NOT NULL,
  `infusiones_input` varchar(20) NOT NULL,
  `pregunta1` varchar(100) NOT NULL,
  `pregunta2` varchar(100) NOT NULL,
  `pregunta3` varchar(100) NOT NULL,
  `pregunta4` varchar(100) NOT NULL,
  `pregunta5` varchar(100) NOT NULL,
  `pregunta6` varchar(100) NOT NULL,
  `proteina` smallint(5) unsigned NOT NULL,
  `grasas` smallint(5) unsigned NOT NULL,
  `carbohidratos` smallint(5) unsigned NOT NULL,
  `dieta` varchar(100) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  `personal_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ficha_nutricion_paciente_id_ab1e320f_fk_paciente_id` (`paciente_id`),
  KEY `ficha_nutricion_personal_id_88a39202_fk_personal_id` (`personal_id`),
  CONSTRAINT `ficha_nutricion_personal_id_88a39202_fk_personal_id` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`id`),
  CONSTRAINT `ficha_nutricion_paciente_id_ab1e320f_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `horario_fis`
--

DROP TABLE IF EXISTS `horario_fis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `horario_fis` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `detalle` varchar(200) NOT NULL,
  `estado` varchar(200) NOT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `personal_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `horario_fis_personal_id_1b619c01_fk_personal_id` (`personal_id`),
  KEY `horario_fis_paciente_id_4a70d69e_fk_paciente_id` (`paciente_id`),
  CONSTRAINT `horario_fis_paciente_id_4a70d69e_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`),
  CONSTRAINT `horario_fis_personal_id_1b619c01_fk_personal_id` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `horario_nut`
--

DROP TABLE IF EXISTS `horario_nut`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `horario_nut` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `detalle` varchar(200) NOT NULL,
  `estado` varchar(200) NOT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `personal_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `horario_nut_paciente_id_21de0da3_fk_paciente_id` (`paciente_id`),
  KEY `horario_nut_personal_id_bd5ed8fa_fk_personal_id` (`personal_id`),
  CONSTRAINT `horario_nut_personal_id_bd5ed8fa_fk_personal_id` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`id`),
  CONSTRAINT `horario_nut_paciente_id_21de0da3_fk_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=375 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=565 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `plan_nut_diario`
--

DROP TABLE IF EXISTS `plan_nut_diario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plan_nut_diario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `dia` varchar(30) NOT NULL,
  `desayuno` varchar(1000) NOT NULL,
  `colacion1` varchar(1000) NOT NULL,
  `almuerzo` varchar(1000) NOT NULL,
  `colacion2` varchar(1000) NOT NULL,
  `cena` varchar(1000) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `dieta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `plan_nut_diario_dieta_id_f40dc24a_fk_dieta_id` (`dieta_id`),
  CONSTRAINT `plan_nut_diario_dieta_id_f40dc24a_fk_dieta_id` FOREIGN KEY (`dieta_id`) REFERENCES `dieta` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=535 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=555 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-21 20:47:37
