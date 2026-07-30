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

-- Dumping structure for table test_stock_db.large_shareholders
DROP TABLE IF EXISTS `large_shareholders`;
CREATE TABLE IF NOT EXISTS `large_shareholders` (
  `stock_id` varchar(20) NOT NULL COMMENT '股票代號',
  `record_date` date NOT NULL COMMENT '資料日期/年度',
  `foreign_ratio` decimal(10,2) DEFAULT 0.00 COMMENT '外資籌碼(%)',
  `large_holder_ratio` decimal(10,2) DEFAULT 0.00 COMMENT '大戶籌碼(%)',
  `director_ratio` decimal(10,2) DEFAULT 0.00 COMMENT '董監持股(%)',
  `stock_price` decimal(20,2) DEFAULT 0.00 COMMENT '股價',
  PRIMARY KEY (`stock_id`,`record_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Dumping data for table test_stock_db.large_shareholders: ~12 rows (approximately)
INSERT IGNORE INTO `large_shareholders` (`stock_id`, `record_date`, `foreign_ratio`, `large_holder_ratio`, `director_ratio`, `stock_price`) VALUES
	('1101', '2026-07-03', 0.00, 0.00, 0.00, 23.65),
	('1101', '2026-07-10', 0.00, 0.00, 0.00, 22.70),
	('1101', '2026-07-17', 0.00, 0.00, 0.00, 23.50),
	('1101', '2026-07-24', 0.00, 0.00, 0.00, 23.80),
	('2330', '2026-07-03', 0.00, 0.00, 0.00, 2445.00),
	('2330', '2026-07-10', 0.00, 0.00, 0.00, 2415.00),
	('2330', '2026-07-17', 0.00, 0.00, 0.00, 2290.00),
	('2330', '2026-07-24', 0.00, 0.00, 0.00, 2350.00),
	('2454', '2026-07-03', 0.00, 0.00, 0.00, 4170.08),
	('2454', '2026-07-10', 0.00, 0.00, 0.00, 3925.00),
	('2454', '2026-07-17', 0.00, 0.00, 0.00, 3370.00),
	('2454', '2026-07-24', 0.00, 0.00, 0.00, 3750.00);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
