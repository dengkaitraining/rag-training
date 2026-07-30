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

-- Dumping structure for table tw_stock_analysis.company_profile
DROP TABLE IF EXISTS `company_profile`;
CREATE TABLE IF NOT EXISTS `company_profile` (
  `stock_id` varchar(10) NOT NULL COMMENT '股票代號',
  `company_name` varchar(100) NOT NULL COMMENT '公司名稱',
  `industry_category` varchar(50) DEFAULT NULL COMMENT '產業類別',
  `capital` bigint(20) DEFAULT NULL COMMENT '實收資本額(元)',
  `listing_date` date DEFAULT NULL COMMENT '上市/上櫃日期',
  `establishment_date` date DEFAULT NULL COMMENT '成立日期',
  `description` text DEFAULT NULL COMMENT '公司業務簡介',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='公司基本面資料表';

-- Dumping data for table tw_stock_analysis.company_profile: ~4 rows (approximately)
INSERT IGNORE INTO `company_profile` (`stock_id`, `company_name`, `industry_category`, `capital`, `listing_date`, `establishment_date`, `description`, `updated_at`) VALUES
	('0050', 'Yuanta/P-shares Taiwan Top 50 ETF', 'ETF', NULL, '2026-07-24', NULL, '無簡介', '2026-07-23 19:20:14'),
	('0056', 'Yuanta/P-shares Taiwan Dividend Plus ETF', 'ETF', NULL, '2026-07-24', NULL, '無簡介', '2026-07-23 19:45:08'),
	('1101', 'TCC Group Holdings Co., Ltd.', 'Building Materials', 179836370944, '2026-07-24', NULL, 'TCC Group Holdings Co., Ltd. manufactures and markets cement, cement-related products, and ready-mixed concrete in Asia, Europe, and Africa. It operates through Cement, Electricity and Energy, Social Aspect of Energy Transition, and Other segments. The company is also involved in the thermal and renewable energy generation; and land and marine transportation business, and production and sale of refractory materials, etc. In addition, it provides engineering, property leasing and development, energy technology, information software design, software development, business consulting, mining excavation, waste collection and treatment, biomass technical, biomass fuel processing, crop straw treatment, import and export trading, resource recycling service technical consultation, tourism and recreation, software product and equipment maintenance, parking management, and property management services, as well as services for accommodation, catering, and health and entertainment. Further, the company engages in the warehousing, transportation, filtering, and sale of sand and gravel; manufacturing and sale of energy storage equipment, batteries, power generation machinery, and electronic components; operation of energy storage and electric vehicle charging stations; sale, import, and export of charging and storage equipment; and sale of charging piles and building materials, as well as intelligent power transmission, distribution and control equipment. Additionally, it is involved in the recycle resource technology development and consultation, business management, and sale activities; biomass solid recovered fuel sales; service of port facility; environmental protection material processing, manufacturing, and operation and related activities; and manufacturing of mortars and paper bags. The company was formerly known as Taiwan Cement Corp. TCC Group Holdings Co., Ltd. was incorporated in 1946 and is headquartered in Taipei, Taiwan.', '2026-07-23 19:46:27'),
	('2330', 'Taiwan Semiconductor Manufacturing Company Limited', 'Semiconductors', 62367350128640, '2026-07-24', NULL, 'Taiwan Semiconductor Manufacturing Company Limited, together with its subsidiaries, manufactures, packages, tests, and sells integrated circuits and other semiconductor devices in Taiwan, China, Europe, the Middle East, Africa, Japan, the United States, and internationally. It provides various wafer fabrication processes, such as processes to manufacture complementary metal- oxide-semiconductor (CMOS) logic, mixed-signal, radio frequency, embedded memory, bipolar CMOS mixed-signal, and others. The company also involved in providing customer and engineering support services; manufacturing of masks; investment in technology start-up companies; research, designing, developing, manufacturing, packaging, testing, and sale of color filters; and investment activities. Its products are used in high performance computing, smartphones, Internet of things, automotive, and digital consumer electronics. Taiwan Semiconductor Manufacturing Company Limited was incorporated in 1987 and is headquartered in Hsinchu City, Taiwan.', '2026-07-23 19:10:18');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
