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

-- Dumping structure for table chunk.imychunk
DROP TABLE IF EXISTS `imychunk`;
CREATE TABLE IF NOT EXISTS `imychunk` (
  `id` varchar(6) NOT NULL DEFAULT '' COMMENT 'ID 流水號',
  `keyword` varchar(20) DEFAULT NULL COMMENT '關鍵字\n',
  `content` text DEFAULT NULL COMMENT '文字內容',
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table chunk.imychunk: ~8 rows (approximately)
INSERT IGNORE INTO `imychunk` (`id`, `keyword`, `content`) VALUES
	('C1000', 'AI', '人工智慧，分 Discriminative AI 與 Generative AI。\n'),
	('C2000', 'AI', 'Arttifical Intelligence，Rule Based 是很早以前的技術，現在是生成式人工智慧 Generative AI。\n'),
	('K0001', 'AI', 'Artificial Intelligent 主要分鑑別式AI與生成式AI'),
	('K0002', 'IoT', 'Internet of Things 全面感知、數據處理、決策控制'),
	('K0003', 'AI', '資料探勘有時也被稱為AI'),
	('K0004', 'IoT', '各類感測器是蒐集數據的IoT終端裝置'),
	('K0005', 'AI', '基因演算法這一類的最佳解搜尋也被稱為AI');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
