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

-- Dumping structure for table test_stock_db.quarterly_eps
DROP TABLE IF EXISTS `quarterly_eps`;
CREATE TABLE IF NOT EXISTS `quarterly_eps` (
  `stock_id` varchar(20) NOT NULL,
  `period_date` date NOT NULL,
  `eps` float DEFAULT NULL COMMENT '每股盈餘',
  `qoq_percent` float DEFAULT NULL COMMENT '季增率%',
  `yoy_percent` float DEFAULT NULL COMMENT '年增率%',
  `quarter_avg_price` float DEFAULT NULL COMMENT '季均價',
  PRIMARY KEY (`stock_id`,`period_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table test_stock_db.quarterly_eps: ~9 rows (approximately)
INSERT IGNORE INTO `quarterly_eps` (`stock_id`, `period_date`, `eps`, `qoq_percent`, `yoy_percent`, `quarter_avg_price`) VALUES
	('1101', '2025-03-31', 0, NULL, NULL, NULL),
	('1101', '2025-06-30', 0, NULL, NULL, NULL),
	('1101', '2025-09-30', -1, NULL, NULL, NULL),
	('1101', '2026-03-31', 0, NULL, NULL, NULL),
	('2330', '2025-03-31', 13, NULL, NULL, NULL),
	('2330', '2025-06-30', 15, NULL, NULL, NULL),
	('2330', '2025-12-31', 19, NULL, NULL, NULL),
	('2330', '2026-03-31', 22, NULL, NULL, NULL),
	('2330', '2026-06-30', 27, NULL, NULL, NULL),
	('2454', '2025-09-30', 15, NULL, NULL, NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
