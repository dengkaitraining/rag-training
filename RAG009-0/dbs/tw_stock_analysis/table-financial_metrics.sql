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

-- Dumping structure for table tw_stock_analysis.financial_metrics
DROP TABLE IF EXISTS `financial_metrics`;
CREATE TABLE IF NOT EXISTS `financial_metrics` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主鍵',
  `stock_id` varchar(10) NOT NULL COMMENT '股票代號',
  `year` int(11) NOT NULL COMMENT '年份',
  `quarter` int(11) NOT NULL COMMENT '季度 (1-4)',
  `eps` decimal(8,2) DEFAULT NULL COMMENT '每股盈餘 (EPS)',
  `gross_margin` decimal(8,4) DEFAULT NULL COMMENT '毛利率 (%)',
  `operating_margin` decimal(8,4) DEFAULT NULL COMMENT '營業利益率 (%)',
  `debt_ratio` decimal(8,4) DEFAULT NULL COMMENT '負債比率 (%)',
  `roe` decimal(8,4) DEFAULT NULL COMMENT '股東權益報酬率 (ROE %)',
  `roa` decimal(8,4) DEFAULT NULL COMMENT '資產報酬率 (ROA %)',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_stock_quarter` (`stock_id`,`year`,`quarter`),
  CONSTRAINT `fk_financial_stock` FOREIGN KEY (`stock_id`) REFERENCES `company_profile` (`stock_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='財務獲利面資料表';

-- Dumping data for table tw_stock_analysis.financial_metrics: ~18 rows (approximately)
INSERT IGNORE INTO `financial_metrics` (`id`, `stock_id`, `year`, `quarter`, `eps`, `gross_margin`, `operating_margin`, `debt_ratio`, `roe`, `roa`, `updated_at`) VALUES
	(1, '2330', 2024, 1, 8.70, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(2, '2330', 2024, 2, 9.56, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(3, '2330', 2024, 3, 12.55, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(4, '2330', 2024, 4, 14.45, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(5, '2330', 2025, 1, 13.95, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(6, '2330', 2025, 2, 15.36, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(7, '2330', 2025, 3, 17.44, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(8, '2330', 2025, 4, 19.51, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(9, '2330', 2026, 1, 22.08, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:10:18'),
	(19, '1101', 2024, 1, 0.26, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28'),
	(20, '1101', 2024, 2, 0.25, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28'),
	(21, '1101', 2024, 3, 0.42, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28'),
	(22, '1101', 2024, 4, 0.52, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28'),
	(23, '1101', 2025, 1, 0.07, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28'),
	(24, '1101', 2025, 2, 0.00, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28'),
	(25, '1101', 2025, 3, -1.36, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28'),
	(26, '1101', 2025, 4, -0.32, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28'),
	(27, '1101', 2026, 1, 0.10, NULL, NULL, NULL, NULL, NULL, '2026-07-23 19:46:28');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
