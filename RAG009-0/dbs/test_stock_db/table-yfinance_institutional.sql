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

-- Dumping structure for table test_stock_db.yfinance_institutional
DROP TABLE IF EXISTS `yfinance_institutional`;
CREATE TABLE IF NOT EXISTS `yfinance_institutional` (
  `stock_id` varchar(20) NOT NULL COMMENT '股票代號',
  `date_reported` date NOT NULL COMMENT '報告日期',
  `holder_name_en` varchar(150) NOT NULL COMMENT '機構名稱(英文)',
  `holder_name_zh` varchar(150) NOT NULL COMMENT '機構名稱(中文)',
  `shares` bigint(20) DEFAULT 0 COMMENT '持有股數',
  `out_ratio` decimal(10,4) DEFAULT 0.0000 COMMENT '流通在外比例',
  `value` bigint(20) DEFAULT 0 COMMENT '總價值',
  PRIMARY KEY (`stock_id`,`holder_name_en`,`date_reported`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Dumping data for table test_stock_db.yfinance_institutional: ~10 rows (approximately)
INSERT IGNORE INTO `yfinance_institutional` (`stock_id`, `date_reported`, `holder_name_en`, `holder_name_zh`, `shares`, `out_ratio`, `value`) VALUES
	('1101', '2025-04-30', 'DFA INVESTMENT DIMENSIONS GROUP INC-Emerging Markets Core Eqy. 2 PORT.', 'DFA INVESTMENT DIMENSIONS GROUP INC-新興市場核心股票2 埠。', 14251055, 0.0000, 346300625),
	('1101', '2025-04-30', 'Dimensional Emerging Markets Value Fund', '維度新興市場價值基金', 18560110, 0.0000, 451010658),
	('1101', '2025-05-31', 'Fidelity Salem Street Trust-Fidelity Series Global ex U.S. Index Fund', '富達塞勒姆街信託-富達系列全球除美國指數基金', 12265302, 0.0000, 298046829),
	('1101', '2025-06-30', 'iShares, Inc.-iShares Core MSCI Emerging Markets ETF', 'iShares, Inc.-iShares 核心 MSCI 新興市場 ETF', 62797182, 0.0000, 1525971474),
	('1101', '2025-06-30', 'iShares, Inc.-iShares MSCI Emerging Markets ETF', 'iShares, Inc.-iShares MSCI 新興市場 ETF', 14087748, 0.0000, 342332265),
	('1101', '2025-06-30', 'iShares, Inc.-iShares MSCI Emerging Markets ex China ETF', 'iShares, Inc.-iShares MSCI 新興市場（中國除外）ETF', 14595671, 0.0000, 354674794),
	('1101', '2025-06-30', 'iShares, Inc.-iShares MSCI Taiwan ETF', 'iShares, Inc.-iShares MSCI 台灣 ETF', 41669645, 0.0000, 1012572341),
	('1101', '2025-04-30', 'VANGUARD Intl Eqy. INDEX Fd.S-Vanguard Emerging Markets Stock Index Fd', '先鋒國際機場INDEX Fd.S-先鋒新興市場股票指數Fd', 84916717, 0.0000, 2063476158),
	('1101', '2025-04-30', 'VANGUARD Intl Eqy. INDEX Fd.S-Vanguard FTSE All-World ex-US Index Fd.', '先鋒國際股票。指數 Fds-Vanguard FTSE 全球（美國除外）指數 Fd。', 13769726, 0.0000, 334604331),
	('1101', '2025-04-30', 'VANGUARD STAR FUNDS-Vanguard Total International Stock Index Fund', 'VANGUARD STAR FUNDS-Vanguard Total International Stock Index Fund', 95034758, 0.0000, 2309344546),
	('2330', '2026-03-31', 'Pacer Advisors, Inc.', '帕瑟顧問公司', 129443, 0.0000, 303543835);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
