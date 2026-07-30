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

-- Dumping structure for table test_stock_db.cash_flow
DROP TABLE IF EXISTS `cash_flow`;
CREATE TABLE IF NOT EXISTS `cash_flow` (
  `stock_id` varchar(20) NOT NULL,
  `period_date` date NOT NULL,
  `operating_cf` bigint(20) DEFAULT NULL COMMENT '營業現金流',
  `investing_cf` bigint(20) DEFAULT NULL COMMENT '投資現金流',
  `financing_cf` bigint(20) DEFAULT NULL COMMENT '融資現金流',
  `free_cf` bigint(20) DEFAULT NULL COMMENT '自由現金流',
  `net_cf` bigint(20) DEFAULT NULL COMMENT '淨現金流',
  PRIMARY KEY (`stock_id`,`period_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table test_stock_db.cash_flow: ~13 rows (approximately)
INSERT IGNORE INTO `cash_flow` (`stock_id`, `period_date`, `operating_cf`, `investing_cf`, `financing_cf`, `free_cf`, `net_cf`) VALUES
	('1101', '2024-12-31', NULL, NULL, NULL, NULL, NULL),
	('1101', '2025-03-31', 6829705000, -13158475000, 17923856000, -1924353000, NULL),
	('1101', '2025-06-30', 4807591000, -2276552000, -15707758000, -128586000, NULL),
	('1101', '2025-09-30', 7275702000, 3547143000, 3453557000, 495848000, NULL),
	('1101', '2025-12-31', 14278584000, -1674252000, -11125769000, 7728203000, NULL),
	('1101', '2026-03-31', 3358179000, 4029757000, -892488000, -5367617000, NULL),
	('2330', '2024-12-31', NULL, NULL, NULL, NULL, NULL),
	('2330', '2025-03-31', NULL, NULL, NULL, NULL, NULL),
	('2330', '2025-06-30', 497064085000, -228488307000, -119700601000, 197501479000, NULL),
	('2330', '2025-09-30', 426829081000, -259752617000, -128293126000, 138385742000, NULL),
	('2330', '2025-12-31', 725508762000, -365960050000, -107685281000, 364041064000, NULL),
	('2330', '2026-03-31', 698976265000, -356853756000, -119910612000, 347270237000, NULL),
	('2330', '2026-06-30', 783365000000, -492810000000, -184654000000, 287363000000, NULL),
	('2454', '2025-09-30', 39180927000, -3370032000, -31019959000, 34359964000, NULL),
	('2454', '2025-12-31', 64520283000, -16638717000, -14578763000, 58948484000, NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
