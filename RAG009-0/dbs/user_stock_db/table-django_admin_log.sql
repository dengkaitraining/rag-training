-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               12.3.2-MariaDB-ubu2404-log - mariadb.org binary distribution
-- Server OS:                    debian-linux-gnu
-- HeidiSQL Version:             12.20.1.1
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table user_stock_db.django_admin_log
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table user_stock_db.django_admin_log: ~22 rows (approximately)
INSERT IGNORE INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2026-07-28 01:02:45.167341', '2', '* 10 * * * (m/h/dM/MY/d) Asia/Taipei', 1, '[{"added": {}}]', 9, 1),
	(2, '2026-07-28 01:02:55.780748', '2', '0 10 * * * (m/h/dM/MY/d) Asia/Taipei', 2, '[{"changed": {"fields": ["Minute(s)"]}}]', 9, 1),
	(3, '2026-07-28 06:29:23.330669', '1101', '1101 台泥', 3, '', 22, 1),
	(4, '2026-07-28 06:29:47.636062', '2330', '2330 台積電', 3, '', 22, 1),
	(5, '2026-07-28 06:46:34.495418', '1101', '1101 台泥', 3, '', 22, 1),
	(6, '2026-07-28 08:41:24.406691', '1101', '1101 台泥', 3, '', 22, 1),
	(7, '2026-07-28 10:06:52.329251', '2330', '2330 台積電', 3, '', 22, 1),
	(8, '2026-07-29 05:13:23.609253', '2', 'Update all scheduled stocks every 4 hours: every 4 hours', 2, '[{"changed": {"fields": ["Task (registered)"]}}]', 11, 1),
	(9, '2026-07-29 05:42:56.873052', '20363', '2308 - 2026-07-29', 3, '', 21, 1),
	(10, '2026-07-29 05:42:56.873134', '19636', '6919 - 2026-07-29', 3, '', 21, 1),
	(11, '2026-07-29 05:42:56.873179', '18909', '4526 - 2026-07-29', 3, '', 21, 1),
	(12, '2026-07-29 05:42:56.873217', '18182', '2454 - 2026-07-29', 3, '', 21, 1),
	(13, '2026-07-29 05:42:56.873254', '17455', '2330 - 2026-07-29', 3, '', 21, 1),
	(14, '2026-07-29 05:42:56.873292', '16728', '1101 - 2026-07-29', 3, '', 21, 1),
	(15, '2026-07-29 05:42:56.873331', '16000', '0050 - 2026-07-29', 3, '', 21, 1),
	(16, '2026-07-29 08:11:12.946972', '0050', '0050 元大台灣50', 3, '', 22, 1),
	(17, '2026-07-29 08:11:35.445437', '1101', '1101 台泥', 3, '', 22, 1),
	(18, '2026-07-29 08:11:35.445514', '2308', '2308 台達電', 3, '', 22, 1),
	(19, '2026-07-29 08:11:35.445560', '2330', '2330 台積電', 3, '', 22, 1),
	(20, '2026-07-29 08:11:35.445600', '2454', '2454 聯發科', 3, '', 22, 1),
	(21, '2026-07-29 08:11:35.445638', '4526', '4526 東台', 3, '', 22, 1),
	(22, '2026-07-29 08:11:35.445676', '6919', '6919 康霈*', 3, '', 22, 1),
	(23, '2026-07-30 06:34:24.295973', '31277', '2330 - 2026-07-30', 3, '', 21, 1),
	(24, '2026-07-30 07:13:07.548513', '7530', '7530 7530', 3, '', 22, 1),
	(25, '2026-07-30 08:01:32.726726', '7530', '7530 7530', 3, '', 22, 1);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
