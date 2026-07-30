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

-- Dumping structure for table db_employee.django_migrations
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table db_employee.django_migrations: ~50 rows (approximately)
INSERT IGNORE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2026-07-23 09:45:16.198892'),
	(2, 'auth', '0001_initial', '2026-07-23 09:45:16.217679'),
	(3, 'admin', '0001_initial', '2026-07-23 09:45:16.230075'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2026-07-23 09:45:16.241281'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-07-23 09:45:16.255201'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2026-07-23 09:45:16.270501'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2026-07-23 09:45:16.282988'),
	(8, 'auth', '0003_alter_user_email_max_length', '2026-07-23 09:45:16.294356'),
	(9, 'auth', '0004_alter_user_username_opts', '2026-07-23 09:45:16.306216'),
	(10, 'auth', '0005_alter_user_last_login_null', '2026-07-23 09:45:16.317459'),
	(11, 'auth', '0006_require_contenttypes_0002', '2026-07-23 09:45:16.319944'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2026-07-23 09:45:16.331845'),
	(13, 'auth', '0008_alter_user_username_max_length', '2026-07-23 09:45:16.343564'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2026-07-23 09:45:16.355877'),
	(15, 'auth', '0010_alter_group_name_max_length', '2026-07-23 09:45:16.367603'),
	(16, 'auth', '0011_update_proxy_permissions', '2026-07-23 09:45:16.370996'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2026-07-23 09:45:16.382945'),
	(18, 'employees', '0001_initial', '2026-07-23 09:45:16.419064'),
	(19, 'sessions', '0001_initial', '2026-07-23 09:45:16.422105'),
	(20, 'django_celery_beat', '0001_initial', '2026-07-27 07:06:43.410658'),
	(21, 'django_celery_beat', '0002_auto_20161118_0346', '2026-07-27 07:06:43.431221'),
	(22, 'django_celery_beat', '0003_auto_20161209_0049', '2026-07-27 07:06:43.443629'),
	(23, 'django_celery_beat', '0004_auto_20170221_0000', '2026-07-27 07:06:43.449863'),
	(24, 'django_celery_beat', '0005_add_solarschedule_events_choices', '2026-07-27 07:06:43.456610'),
	(25, 'django_celery_beat', '0006_auto_20180322_0932', '2026-07-27 07:06:43.555039'),
	(26, 'django_celery_beat', '0007_auto_20180521_0826', '2026-07-27 07:06:43.603147'),
	(27, 'django_celery_beat', '0008_auto_20180914_1922', '2026-07-27 07:06:43.718133'),
	(28, 'django_celery_beat', '0006_auto_20180210_1226', '2026-07-27 07:06:43.767168'),
	(29, 'django_celery_beat', '0006_periodictask_priority', '2026-07-27 07:06:43.787236'),
	(30, 'django_celery_beat', '0009_periodictask_headers', '2026-07-27 07:06:43.806706'),
	(31, 'django_celery_beat', '0010_auto_20190429_0326', '2026-07-27 07:06:50.954680'),
	(32, 'django_celery_beat', '0011_auto_20190508_0153', '2026-07-27 07:06:50.984232'),
	(33, 'django_celery_beat', '0012_periodictask_expire_seconds', '2026-07-27 07:06:51.004287'),
	(34, 'django_celery_beat', '0013_auto_20200609_0727', '2026-07-27 07:06:51.021878'),
	(35, 'django_celery_beat', '0014_remove_clockedschedule_enabled', '2026-07-27 07:06:51.027891'),
	(36, 'django_celery_beat', '0015_edit_solarschedule_events_choices', '2026-07-27 07:06:51.034484'),
	(37, 'django_celery_beat', '0016_alter_crontabschedule_timezone', '2026-07-27 07:06:51.051996'),
	(38, 'django_celery_beat', '0017_alter_crontabschedule_month_of_year', '2026-07-27 07:06:51.070781'),
	(39, 'django_celery_beat', '0018_improve_crontab_helptext', '2026-07-27 07:06:51.088236'),
	(40, 'django_celery_beat', '0019_alter_periodictasks_options', '2026-07-27 07:06:51.091655'),
	(41, 'django_celery_beat', '0010_auto_20190429_0326', '2026-07-27 07:06:51.460571'),
	(42, 'django_celery_beat', '0011_auto_20190508_0153', '2026-07-27 07:06:51.488587'),
	(43, 'django_celery_beat', '0012_periodictask_expire_seconds', '2026-07-27 07:06:51.508344'),
	(44, 'django_celery_beat', '0013_auto_20200609_0727', '2026-07-27 07:06:51.526518'),
	(45, 'django_celery_beat', '0014_remove_clockedschedule_enabled', '2026-07-27 07:06:51.533003'),
	(46, 'django_celery_beat', '0015_edit_solarschedule_events_choices', '2026-07-27 07:06:51.539776'),
	(47, 'django_celery_beat', '0016_alter_crontabschedule_timezone', '2026-07-27 07:06:51.557892'),
	(48, 'django_celery_beat', '0017_alter_crontabschedule_month_of_year', '2026-07-27 07:06:51.575511'),
	(49, 'django_celery_beat', '0018_improve_crontab_helptext', '2026-07-27 07:06:51.594454'),
	(50, 'django_celery_beat', '0019_alter_periodictasks_options', '2026-07-27 07:06:51.598194'),
	(51, 'core', '0001_initial', '2026-07-27 07:30:17.805203'),
	(52, 'core', '0001_initial', '2026-07-27 07:30:17.827844'),
	(53, 'core', '0001_initial', '2026-07-27 07:30:17.861750'),
	(54, 'stock_db', '0001_initial', '2026-07-28 02:53:51.284214'),
	(55, 'stock_db', '0002_alter_companynews_unique_together_and_more', '2026-07-29 08:20:21.893897'),
	(56, 'stock_db', '0002_alter_companynews_unique_together_and_more', '2026-07-29 08:20:21.940230');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
