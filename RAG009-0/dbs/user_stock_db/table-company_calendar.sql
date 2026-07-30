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

-- Dumping structure for table user_stock_db.company_calendar
DROP TABLE IF EXISTS `company_calendar`;
CREATE TABLE IF NOT EXISTS `company_calendar` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `event_type` varchar(50) NOT NULL,
  `event_date` date NOT NULL,
  `description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `stock_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `company_calendar_stock_id_event_type_event_date_30d80fec_uniq` (`stock_id`,`event_type`,`event_date`),
  CONSTRAINT `company_calendar_stock_id_e246d150_fk_company_profile_stock_id` FOREIGN KEY (`stock_id`) REFERENCES `company_profile` (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table user_stock_db.company_calendar: ~4 rows (approximately)
INSERT IGNORE INTO `company_calendar` (`id`, `event_type`, `event_date`, `description`, `created_at`, `updated_at`, `stock_id`) VALUES
	(11, '配股發放日', '2026-09-16', '除權息發放日/除權日', '2026-07-29 08:29:04.275928', '2026-07-30 12:35:06.836959', '2330'),
	(12, '配股發放日', '2026-07-01', '除權息發放日/除權日', '2026-07-30 05:24:12.600742', '2026-07-30 12:31:00.917012', '1101'),
	(13, '配股發放日', '2026-06-17', '除權息發放日/除權日', '2026-07-30 05:25:58.482950', '2026-07-30 12:32:59.736959', '2308'),
	(14, '配股發放日', '2026-07-07', '除權息發放日/除權日', '2026-07-30 05:29:34.544892', '2026-07-30 12:36:54.033810', '2454'),
	(15, '配股發放日', '2026-07-30', '除權息發放日/除權日', '2026-07-30 05:31:02.914037', '2026-07-30 12:38:42.317552', '4526'),
	(16, '配股發放日', '2026-07-16', '除權息發放日/除權日', '2026-07-30 06:49:05.804334', '2026-07-30 12:40:45.466486', '6488');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
