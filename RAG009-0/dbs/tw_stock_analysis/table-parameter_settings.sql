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

-- Dumping structure for table tw_stock_analysis.parameter_settings
DROP TABLE IF EXISTS `parameter_settings`;
CREATE TABLE IF NOT EXISTS `parameter_settings` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主鍵',
  `language` varchar(10) NOT NULL COMMENT '語系地區',
  `country` varchar(10) NOT NULL COMMENT '地區',
  `period` varchar(10) NOT NULL COMMENT '過去區間的新聞',
  `max_results` int(11) NOT NULL COMMENT '單次抓取量',
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='參數設定表單 (Parameter Settings Table)';

-- Dumping data for table tw_stock_analysis.parameter_settings: ~0 rows (approximately)
INSERT IGNORE INTO `parameter_settings` (`id`, `language`, `country`, `period`, `max_results`, `updated_at`) VALUES
	(1, 'zh-TW', 'TW', '4h', 100, '2026-07-24 15:02:17');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
