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

-- Dumping structure for table user_stock_db.company_profile
DROP TABLE IF EXISTS `company_profile`;
CREATE TABLE IF NOT EXISTS `company_profile` (
  `stock_id` varchar(20) NOT NULL,
  `tax_id` varchar(20) DEFAULT NULL,
  `company_name` varchar(100) NOT NULL,
  `spokesperson` varchar(50) DEFAULT NULL,
  `eng_short_name` varchar(100) DEFAULT NULL,
  `deputy_spokesperson` varchar(50) DEFAULT NULL,
  `establishment_date` date DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `listing_date` date DEFAULT NULL,
  `fax` varchar(30) DEFAULT NULL,
  `industry_category` varchar(50) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `chairman` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `general_manager` varchar(50) DEFAULT NULL,
  `stock_transfer_agent` varchar(100) DEFAULT NULL,
  `capital` decimal(20,2) DEFAULT NULL,
  `auditor` varchar(100) DEFAULT NULL,
  `issued_shares` bigint(20) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `market_cap_millions` decimal(20,2) DEFAULT NULL,
  `market_type` varchar(20) DEFAULT NULL,
  `insider_holding_ratio` decimal(5,2) DEFAULT NULL,
  `group_name` varchar(100) DEFAULT NULL,
  `main_business` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table user_stock_db.company_profile: ~8 rows (approximately)
INSERT IGNORE INTO `company_profile` (`stock_id`, `tax_id`, `company_name`, `spokesperson`, `eng_short_name`, `deputy_spokesperson`, `establishment_date`, `phone`, `listing_date`, `fax`, `industry_category`, `website`, `chairman`, `email`, `general_manager`, `stock_transfer_agent`, `capital`, `auditor`, `issued_shares`, `address`, `market_cap_millions`, `market_type`, `insider_holding_ratio`, `group_name`, `main_business`, `created_at`, `updated_at`) VALUES
	('0050', NULL, '元大台灣50', NULL, 'YUANTA SECURITIES INV TRUST CO ', NULL, NULL, '886-2-2516-9339', '2003-06-30', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '上市', NULL, '', NULL, '2026-07-30 05:22:30.600423', '2026-07-30 12:29:01.525283'),
	('1101', NULL, '台泥', NULL, 'TCC GROUP HOLDINGS CO LTD', NULL, NULL, '886 2 2531 7099', '1962-02-09', '886 2 2531 6650', '水泥工業', 'https://www.tccgroupholdings.com', 'Mr. An-Ping  Chang', NULL, 'Mr. An-Ping  Chang', NULL, 74931820000.00, NULL, 7493182000, 'No. 113, Zhongshan North Road Taipei Taiwan', 180211.02, '上市', 13.76, '水泥工業', '台泥集團控股有限公司在亞洲、歐洲和非洲生產和銷售水泥、水泥相關產品和預拌混凝土。它透過水泥、電力和能源、能源轉型社會方面和其他部門運作。該公司還涉足熱能和再生能源發電；此外，還提供工程設計、物業租賃與開發、能源技術、資訊軟體設計、軟體開發、商務諮詢、礦山開採、垃圾收集與處理、生物質技術、生物質燃料加工、農作物秸稈處理、進出口貿易、資源循環利用服務技術諮詢、休閒、軟體產品與設備維修、停車管理、娛樂設備維修服務。此外，公司還從事砂石的倉儲、運輸、過濾、銷售；儲能設備、電池、發電機械、電子元件的製造和銷售；儲能和電動汽車充電站的運作；充電及儲存設備的銷售、進出口；充電樁、建築材料、智慧輸配電及控制設備的銷售。此外，也從事回收資源技術開發和諮詢、業務管理和銷售活動；生物質固體回收燃料銷售；港口設施服務；環保材料加工、製造、經營及相關活動；以及砂漿和紙袋的製造。公司前身為台灣水泥股份有限公司。台泥集團控股有限公司成立於1946年，總部位於台灣台北市。', '2026-07-30 05:24:12.588615', '2026-07-30 12:31:00.904324'),
	('2308', NULL, '台達電', NULL, 'DELTA ELECTRONIC', NULL, NULL, '886 2 8797 2088', '1988-12-19', '886 2 8797 2120', '電子零組件業', 'https://www.deltaww.com', 'Mr. Ping  Cheng', NULL, 'Mr. Ping  Cheng', NULL, 25975433290.00, NULL, 2597543329, '186, Ruey Kuang Road Taipei Taiwan', 3974241.45, '上市', 25.93, '電子零組件業', '台達電子有限公司及其子公司在中國大陸、美國、台灣、泰國和國際上提供電源和熱管理解決方案。它透過電力電子、行動、自動化和基礎設施部門運作。該公司提供電感器、變壓器組件、網路產品、EMI 濾波器、螺線管、電流檢測電阻器、電源模組以及沖壓和包覆成型組件；嵌入式電源、適配器、工業和醫療電源解決方案、工業電池充電、USB插座、氫動力和高壓電源解決方案；直流無水鼓和空氣解決方案它還提供電動車電力電子、牽引和 X-in-1 產品。此外，該公司還提供驅動和電能品質、運動、控制、機器人和製造設備，以及現場設備、軟體和工業 PC；樓宇管理與控制、室內空氣品質、LED照明、智慧監控、健康照明、建築解決方案。此外，還提供電信電源系統、網路和農村電氣化系統、UPS和資料中心基礎設施以及電能品質產品；電動車充電、儲能係統、光伏逆變器、能源管理、風電變流器、固態變壓器、中壓驅動、高壓電源、自動測試設備、氫能和燃料電池解決方案、商業牆面設備和高性能媒體解決方案、設備 DLP 設備和設備解決方案。此外，它還提供建築管理和控制解決方案的諮詢服務。台達電子有限公司成立於 1971 年，總部位於台灣台北。', '2026-07-30 05:25:58.468888', '2026-07-30 12:32:59.724456'),
	('2330', NULL, '台積電', NULL, 'TAIWAN SEMICONDUCTOR MANUFACTUR', NULL, NULL, '886 3 563 6688', '1994-09-05', '886 3 563 7000', '半導體業', 'https://www.tsmc.com', 'Dr. C. C.  Wei Ph.D.', NULL, 'Dr. C. C.  Wei Ph.D.', NULL, 259323700670.00, NULL, 25932370067, 'Hsinchu Science Park Hsinchu City Taiwan', 57180875.13, '上市', 0.02, '半導體業', '台積電及其子公司在台灣、中國大陸、歐洲、中東、非洲、日本、美國和國際上製造、封裝、測試和銷售積體電路和其他半導體裝置。它提供各種晶圓製造工藝，例如製造互補金屬氧化物半導體 (CMOS) 邏輯、混合訊號、射頻、嵌入式記憶體、雙極 CMOS 混合訊號等的製程。該公司還提供客戶和工程支援服務；口罩製造；投資科技新創公司；彩色濾光片的研究、設計、開發、製造、包裝、測試和銷售；和投資活動。其產品應用於高效能運算、智慧型手機、物聯網、汽車和數位消費性電子產品。台積電成立於1987年，總部位於台灣新竹市。', '2026-07-29 08:29:04.258547', '2026-07-30 12:35:06.824169'),
	('2454', NULL, '聯發科', NULL, 'MEDIATEK INC', NULL, NULL, '886 3 5670 766', '2001-07-23', NULL, '半導體業', 'https://www.mediatek.com', 'Dr. Lih Shyng  Tsai Ph.D.', NULL, 'Dr. Lih Shyng  Tsai Ph.D.', NULL, 15961102050.00, NULL, 1596110205, 'No. 1, Dusing 1st Road Hsinchu City Taiwan', 5163416.29, '上市', 8.10, '半導體業', '聯發科公司在台灣、亞洲其他地區和國際上從事多媒體積體電路 (IC) 的研究、開發、生產、製造和行銷。該公司提供各種應用的多媒體、電腦週邊設備、面向消費者的 IC 和其他 IC。並提供軟硬體解決方案的設計、試運轉、維護保養及技術諮詢服務；以及其積體電路產品的銷售及授權專利及電路佈局權。此外，該公司還提供研究、行銷和技術服務；智慧財產權管理服務；和一般投資服務。該公司成立於1997年，總部位於台灣新竹市。', '2026-07-30 05:29:34.532061', '2026-07-30 12:36:54.020287'),
	('4526', NULL, '東台', NULL, 'TONG-TAI MACHINE TOOL CO', NULL, NULL, '886 7 976 1588', '2003-09-15', '886 7 976 1589', '電機機械', 'https://www.tongtai.com.tw', 'Mr. Jui-Hsiung  Yen', NULL, NULL, NULL, 2518270000.00, NULL, 251827000, 'No.3, Luke 3rd Road Kaohsiung Taiwan', 6346.04, '上市', 29.50, '電機機械', '東台精機股份有限公司在台灣、中國大陸、歐洲、亞洲其他地區和國際上製造和銷售工具機、電腦組件、電腦數控車床和切割中心。它透過機器製造商、零件製造商和其他部門運作。本公司提供垂直、臥式、垂直五軸、水平式五軸、超音波輔助加工中心，以及攻牙中心、水平、直立式數控車床；以及 CNC PCB 鑽孔、CNC PCB Routing 和雷射加工機。另提供金屬粉末床熔合機；以及智慧工具，包括生產線管理和智慧軟體。此外，公司還提供交鑰匙解決方案、自動化、智慧製造、機械加工、工程分析和製程規劃、工裝規劃、夾具設計、生產佈局規劃、數控編程、批量試製和驗證、自動化模組和系統整合、生產線監控和視覺化、機器智能源和邊緣運算、感測器技術和應用、彈性製造和智慧調度、數位孿生和資訊物理系統、車銑複合、超音波輔助加工、熱補償、齒輪製造、振盪切削、旋轉中心標定、測量和補償等解決方案，以及框架獨立式、全線式和FMS。此外，也從事電氣自動化設備及客製化機的銷售；金屬零件製造、加工；數位控制機器及系統、印刷電路板的製造及銷售；國際貿易及一般投資活動。該公司成立於1969年，總部位於台灣高雄。', '2026-07-30 05:31:02.900698', '2026-07-30 12:38:42.305014'),
	('6488', NULL, '環球晶', NULL, 'GLOBALWAFERS CO LTD', NULL, NULL, '886 3 577 2255', '2015-09-25', '886 3 578 1706', '半導體業', 'https://www.sas-globalwafers.com', 'Ms. Hsiu-Lan  Hsu', NULL, 'Ms. Hsiu-Lan  Hsu', NULL, 4781137250.00, NULL, 478113725, 'Hsinchu Science Park Hsinchu City Taiwan', 371972.47, '上櫃', 46.86, '半導體業', '環球晶圓股份有限公司及其子公司在台灣和國際上研究、開發、設計、製造和銷售半導體錠/晶圓。該公司提供 Epi 晶圓、拋光晶圓、擴散晶圓、退火晶圓、SOI 晶圓、FZ 晶圓和化合物晶圓，以及外延晶圓和矽錠。它還提供技術和管理資訊諮詢服務。該公司成立於 1981 年，總部位於台灣新竹市。', '2026-07-30 06:49:05.789335', '2026-07-30 12:40:45.454197'),
	('6919', NULL, '康霈*', NULL, 'CALIWAY BIOPHARMACEUTICALS CO L', NULL, NULL, '886 2 2697 1355', '2024-10-02', '886 2 2697 2508', '生技醫療業', 'https://www.caliway.com.tw', 'Mr. Antony  Hsu', NULL, 'Ms. Vivian  Ling', NULL, 15562998600.00, NULL, 1556299860, 'No.99, Xintai 5th Road New Taipei City Taiwan', 160298.89, '上市', 33.26, '生技醫療業', '卡利威生物製藥有限公司及其子公司從事美容醫學和慢性發炎藥物的開發。該公司開發了一種研究藥物 CBL-514，目前正處於非手術減脂和 Dercum 病以及脂肪團治療的 2 期臨床試驗中。該公司還在開發 CBA-539，該藥物處於臨床前階段，用於治療中心性肥胖、色素沉著過度和皮膚老化，並提供膳食補充劑。該公司成立於 2012 年，總部位於台灣新北市。', '2026-07-30 05:32:37.840588', '2026-07-30 12:42:23.142502'),
	('7530', NULL, 'Forward Tek', NULL, 'Forward Tek', NULL, NULL, '886 3 7586 993', NULL, '886 3 7585 987', 'Specialty Industrial Machinery', 'https://www.forward-tek.com.tw', NULL, NULL, NULL, NULL, 465000000.00, NULL, 46500000, 'No.232, Youyi Road Zhunan Taiwan', 1353.15, '上櫃', NULL, NULL, 'Forward Science Corp. 在台灣生產真空幫浦。它提供真空設備以及維修和保養服務；精密機械及OEM/ODM製造服務；智慧機電系統，包括中央管理系統、預測和健康管理、人工智慧測試平台和智慧製造。公司成立於1992年，總部位於台灣竹南。', '2026-07-30 08:05:03.023205', '2026-07-30 12:42:51.935031');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
