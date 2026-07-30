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

-- Dumping structure for table user_stock_db.stock_schedule_list
DROP TABLE IF EXISTS `stock_schedule_list`;
CREATE TABLE IF NOT EXISTS `stock_schedule_list` (
  `stock_id` varchar(20) NOT NULL,
  `analysis_period` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table user_stock_db.stock_schedule_list: ~4 rows (approximately)
INSERT IGNORE INTO `stock_schedule_list` (`stock_id`, `analysis_period`, `created_at`, `updated_at`) VALUES
	('0050', 3, '2026-07-29 00:37:10.003470', '2026-07-29 00:37:10.003538'),
	('1101', 3, '2026-07-28 06:30:59.160708', '2026-07-28 06:30:59.160780'),
	('2308', 3, '2026-07-29 05:10:50.536510', '2026-07-29 05:10:50.536571'),
	('2330', 3, '2026-07-28 03:04:01.441081', '2026-07-28 03:04:01.441158'),
	('2454', 3, '2026-07-28 10:11:25.533924', '2026-07-28 10:11:25.533980'),
	('4526', 3, '2026-07-28 10:24:42.797735', '2026-07-28 10:24:42.797804'),
	('6488', 3, '2026-07-30 06:47:38.911727', '2026-07-30 06:47:38.911792'),
	('6919', 3, '2026-07-28 13:47:44.421435', '2026-07-28 13:47:44.421500'),
	('7530', 3, '2026-07-30 07:03:46.543267', '2026-07-30 07:03:46.543355');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
