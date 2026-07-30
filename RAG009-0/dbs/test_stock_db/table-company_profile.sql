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

-- Dumping structure for table test_stock_db.company_profile
DROP TABLE IF EXISTS `company_profile`;
CREATE TABLE IF NOT EXISTS `company_profile` (
  `stock_id` varchar(20) NOT NULL COMMENT '股票代碼',
  `tax_id` varchar(20) DEFAULT NULL COMMENT '統一編號',
  `company_name` varchar(100) NOT NULL COMMENT '公司名稱',
  `spokesperson` varchar(50) DEFAULT NULL COMMENT '發言人',
  `eng_short_name` varchar(100) DEFAULT NULL COMMENT '英文簡稱',
  `deputy_spokesperson` varchar(50) DEFAULT NULL COMMENT '代理發言人',
  `establishment_date` date DEFAULT NULL COMMENT '成立時間',
  `phone` varchar(30) DEFAULT NULL COMMENT '總機電話',
  `listing_date` date DEFAULT NULL COMMENT '掛牌日期',
  `fax` varchar(30) DEFAULT NULL COMMENT '傳真號碼',
  `industry_category` varchar(50) DEFAULT NULL COMMENT '產業類別',
  `website` varchar(255) DEFAULT NULL COMMENT '公司網站',
  `chairman` varchar(50) DEFAULT NULL COMMENT '董事長',
  `email` varchar(100) DEFAULT NULL COMMENT '電子郵件',
  `general_manager` varchar(50) DEFAULT NULL COMMENT '總經理',
  `stock_transfer_agent` varchar(100) DEFAULT NULL COMMENT '股務代理',
  `capital` decimal(20,2) DEFAULT NULL COMMENT '股本(元)',
  `auditor` varchar(100) DEFAULT NULL COMMENT '簽證會計師',
  `issued_shares` bigint(20) DEFAULT NULL COMMENT '已發行普通股數',
  `address` varchar(255) DEFAULT NULL COMMENT '公司地址',
  `market_cap_millions` decimal(20,2) DEFAULT NULL COMMENT '市值(百萬)',
  `market_type` varchar(20) DEFAULT NULL COMMENT '市場別(上市/上櫃/興櫃)',
  `insider_holding_ratio` decimal(5,2) DEFAULT NULL COMMENT '董監持股比例(%)',
  `group_name` varchar(100) DEFAULT NULL COMMENT '所屬集團',
  `main_business` text DEFAULT NULL COMMENT '主要經營業務',
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='公司基本資料表';

-- Dumping data for table test_stock_db.company_profile: ~1 rows (approximately)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
