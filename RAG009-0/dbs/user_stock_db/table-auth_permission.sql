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

-- Dumping structure for table user_stock_db.auth_permission
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table user_stock_db.auth_permission: ~89 rows (approximately)
INSERT IGNORE INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, '可以管理資料庫與表單資料 (DataTables & 帳號切換)', 7, 'can_manage_db_tables'),
	(26, 'Can add 員工主資料表', 8, 'add_employee'),
	(27, 'Can change 員工主資料表', 8, 'change_employee'),
	(28, 'Can delete 員工主資料表', 8, 'delete_employee'),
	(29, 'Can view 員工主資料表', 8, 'view_employee'),
	(30, 'Can add crontab', 9, 'add_crontabschedule'),
	(31, 'Can change crontab', 9, 'change_crontabschedule'),
	(32, 'Can delete crontab', 9, 'delete_crontabschedule'),
	(33, 'Can view crontab', 9, 'view_crontabschedule'),
	(34, 'Can add interval', 10, 'add_intervalschedule'),
	(35, 'Can change interval', 10, 'change_intervalschedule'),
	(36, 'Can delete interval', 10, 'delete_intervalschedule'),
	(37, 'Can view interval', 10, 'view_intervalschedule'),
	(38, 'Can add periodic task', 11, 'add_periodictask'),
	(39, 'Can change periodic task', 11, 'change_periodictask'),
	(40, 'Can delete periodic task', 11, 'delete_periodictask'),
	(41, 'Can view periodic task', 11, 'view_periodictask'),
	(42, 'Can add periodic task track', 12, 'add_periodictasks'),
	(43, 'Can change periodic task track', 12, 'change_periodictasks'),
	(44, 'Can delete periodic task track', 12, 'delete_periodictasks'),
	(45, 'Can view periodic task track', 12, 'view_periodictasks'),
	(46, 'Can add solar event', 13, 'add_solarschedule'),
	(47, 'Can change solar event', 13, 'change_solarschedule'),
	(48, 'Can delete solar event', 13, 'delete_solarschedule'),
	(49, 'Can view solar event', 13, 'view_solarschedule'),
	(50, 'Can add clocked', 14, 'add_clockedschedule'),
	(51, 'Can change clocked', 14, 'change_clockedschedule'),
	(52, 'Can delete clocked', 14, 'delete_clockedschedule'),
	(53, 'Can view clocked', 14, 'view_clockedschedule'),
	(54, 'Can add 公司基本資料', 15, 'add_companyprofile'),
	(55, 'Can change 公司基本資料', 15, 'change_companyprofile'),
	(56, 'Can delete 公司基本資料', 15, 'delete_companyprofile'),
	(57, 'Can view 公司基本資料', 15, 'view_companyprofile'),
	(58, 'Can add 公司行事曆', 16, 'add_companycalendar'),
	(59, 'Can change 公司行事曆', 16, 'change_companycalendar'),
	(60, 'Can delete 公司行事曆', 16, 'delete_companycalendar'),
	(61, 'Can view 公司行事曆', 16, 'view_companycalendar'),
	(62, 'Can add 公司新聞與個股公告', 17, 'add_companynews'),
	(63, 'Can change 公司新聞與個股公告', 17, 'change_companynews'),
	(64, 'Can delete 公司新聞與個股公告', 17, 'delete_companynews'),
	(65, 'Can view 公司新聞與個股公告', 17, 'view_companynews'),
	(66, 'Can add 排程更新清單', 18, 'add_stockschedulelist'),
	(67, 'Can change 排程更新清單', 18, 'change_stockschedulelist'),
	(68, 'Can delete 排程更新清單', 18, 'delete_stockschedulelist'),
	(69, 'Can view 排程更新清單', 18, 'view_stockschedulelist'),
	(70, 'Can add 排程更新清單', 19, 'add_stockschedulelist'),
	(71, 'Can change 排程更新清單', 19, 'change_stockschedulelist'),
	(72, 'Can delete 排程更新清單', 19, 'delete_stockschedulelist'),
	(73, 'Can view 排程更新清單', 19, 'view_stockschedulelist'),
	(74, 'Can add 公司新聞與個股公告', 20, 'add_companynews'),
	(75, 'Can change 公司新聞與個股公告', 20, 'change_companynews'),
	(76, 'Can delete 公司新聞與個股公告', 20, 'delete_companynews'),
	(77, 'Can view 公司新聞與個股公告', 20, 'view_companynews'),
	(78, 'Can add 個股技術分析', 21, 'add_technicalanalysis'),
	(79, 'Can change 個股技術分析', 21, 'change_technicalanalysis'),
	(80, 'Can delete 個股技術分析', 21, 'delete_technicalanalysis'),
	(81, 'Can view 個股技術分析', 21, 'view_technicalanalysis'),
	(82, 'Can add 公司基本資料', 22, 'add_companyprofile'),
	(83, 'Can change 公司基本資料', 22, 'change_companyprofile'),
	(84, 'Can delete 公司基本資料', 22, 'delete_companyprofile'),
	(85, 'Can view 公司基本資料', 22, 'view_companyprofile'),
	(86, 'Can add 公司行事曆', 23, 'add_companycalendar'),
	(87, 'Can change 公司行事曆', 23, 'change_companycalendar'),
	(88, 'Can delete 公司行事曆', 23, 'delete_companycalendar'),
	(89, 'Can view 公司行事曆', 23, 'view_companycalendar');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
