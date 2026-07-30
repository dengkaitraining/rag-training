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

-- Dumping structure for table test_stock_db.monthly_revenue
DROP TABLE IF EXISTS `monthly_revenue`;
CREATE TABLE IF NOT EXISTS `monthly_revenue` (
  `stock_id` varchar(20) NOT NULL,
  `period_date` date NOT NULL,
  `current_revenue` bigint(20) DEFAULT NULL COMMENT '當月營收(仟元)',
  `mom_percent` float DEFAULT NULL COMMENT '月增率%',
  `last_year_revenue` bigint(20) DEFAULT NULL COMMENT '去年同月營收(仟元)',
  `yoy_percent` float DEFAULT NULL COMMENT '年增率%',
  `acc_revenue` bigint(20) DEFAULT NULL COMMENT '當月累計營收(仟元)',
  `last_year_acc_revenue` bigint(20) DEFAULT NULL COMMENT '去年累計營收(仟元)',
  `acc_yoy_percent` float DEFAULT NULL COMMENT '累計年增率%',
  PRIMARY KEY (`stock_id`,`period_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table test_stock_db.monthly_revenue: ~0 rows (approximately)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
