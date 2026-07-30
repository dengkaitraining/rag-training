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

-- Dumping structure for table test_stock_db.technical_analysis
DROP TABLE IF EXISTS `technical_analysis`;
CREATE TABLE IF NOT EXISTS `technical_analysis` (
  `stock_id` varchar(20) NOT NULL COMMENT '股票代號',
  `trade_date` date NOT NULL COMMENT '交易日期',
  `volume` bigint(20) DEFAULT NULL COMMENT '成交量',
  `open_price` decimal(20,2) DEFAULT NULL COMMENT '開盤價',
  `high_price` decimal(20,2) DEFAULT NULL COMMENT '最高價',
  `low_price` decimal(20,2) DEFAULT NULL COMMENT '最低價',
  `close_price` decimal(20,2) DEFAULT NULL COMMENT '收盤價',
  `k_value` decimal(20,4) DEFAULT NULL COMMENT 'K值',
  `d_value` decimal(20,4) DEFAULT NULL COMMENT 'D值',
  `j_value` decimal(20,4) DEFAULT NULL COMMENT 'J值',
  `macd` decimal(20,4) DEFAULT NULL COMMENT 'MACD',
  `macd_signal` decimal(20,4) DEFAULT NULL COMMENT 'MACD Signal',
  `bias` decimal(20,4) DEFAULT NULL COMMENT '乖離率(6日)',
  `williams_r` decimal(10,4) DEFAULT NULL COMMENT '威廉指標(14日)',
  `bbi` decimal(20,4) DEFAULT NULL COMMENT '多空指標(BBI)',
  `cdp` decimal(20,2) DEFAULT NULL COMMENT 'CDP',
  `ah` decimal(20,2) DEFAULT NULL COMMENT '最高值(AH)',
  `nh` decimal(20,2) DEFAULT NULL COMMENT '近高值(NH)',
  `nl` decimal(20,2) DEFAULT NULL COMMENT '近低值(NL)',
  `al` decimal(20,2) DEFAULT NULL COMMENT '最低值(AL)',
  `pdi` decimal(20,4) DEFAULT NULL COMMENT '+DI',
  `mdi` decimal(20,4) DEFAULT NULL COMMENT '-DI',
  `adx` decimal(20,4) DEFAULT NULL COMMENT 'ADX',
  PRIMARY KEY (`stock_id`,`trade_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='個股技術分析資料表';

-- Dumping data for table test_stock_db.technical_analysis: ~0 rows (approximately)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
