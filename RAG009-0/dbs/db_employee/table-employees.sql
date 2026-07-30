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

-- Dumping structure for table db_employee.employees
DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT EXISTS `employees` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `employee_num` varchar(20) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `national_id` varchar(20) NOT NULL,
  `gender` smallint(5) unsigned NOT NULL CHECK (`gender` >= 0),
  `birth_date` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `personal_email` varchar(100) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `department_id` int(11) DEFAULT NULL,
  `job_title_id` int(11) DEFAULT NULL,
  `status` smallint(5) unsigned NOT NULL CHECK (`status` >= 0),
  `hire_date` date NOT NULL,
  `termination_date` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `manager_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_num` (`employee_num`),
  UNIQUE KEY `national_id` (`national_id`),
  UNIQUE KEY `email` (`email`),
  KEY `employees_manager_id_0674f795_fk_employees_id` (`manager_id`),
  CONSTRAINT `employees_manager_id_0674f795_fk_employees_id` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table db_employee.employees: ~10 rows (approximately)
INSERT IGNORE INTO `employees` (`id`, `employee_num`, `first_name`, `last_name`, `national_id`, `gender`, `birth_date`, `email`, `personal_email`, `phone`, `department_id`, `job_title_id`, `status`, `hire_date`, `termination_date`, `created_at`, `updated_at`, `manager_id`) VALUES
	(1, 'EMP2026001', '大明', '陳', 'A123456789', 1, '1985-05-20', 'daming.chen@company.com', 'personal_emp2026001@gmail.com', '0912345678', 101, 10, 1, '2020-03-01', NULL, '2026-07-23 09:45:21.807237', '2026-07-23 09:45:21.858075', 10),
	(2, 'EMP2026002', '美麗', '林', 'B223456780', 2, '1990-08-15', 'meili.lin@company.com', 'personal_emp2026002@gmail.com', '0923456789', 101, 11, 1, '2021-06-15', NULL, '2026-07-23 09:45:21.817010', '2026-07-23 09:45:21.860454', 10),
	(3, 'EMP2026003', '志豪', '張', 'C123456781', 1, '1988-11-03', 'zhihao.chang@company.com', 'personal_emp2026003@gmail.com', '0934567890', 102, 20, 1, '2019-01-10', NULL, '2026-07-23 09:45:21.822785', '2026-07-23 09:45:21.863051', 10),
	(4, 'EMP2026004', '淑芬', '黃', 'D223456782', 2, '1992-02-28', 'shufen.huang@company.com', 'personal_emp2026004@gmail.com', '0945678901', 102, 21, 1, '2022-09-01', NULL, '2026-07-23 09:45:21.827297', '2026-07-23 09:45:21.865630', 10),
	(5, 'EMP2026005', '冠宇', '李', 'E123456783', 1, '1995-07-07', 'guanyu.lee@company.com', 'personal_emp2026005@gmail.com', '0956789012', 103, 30, 1, '2023-04-12', NULL, '2026-07-23 09:45:21.831772', '2026-07-23 09:45:21.831809', NULL),
	(6, 'EMP2026006', '佩君', '趙', 'F223456784', 2, '1993-12-19', 'peijun.zhao@company.com', 'personal_emp2026006@gmail.com', '0967890123', 103, 31, 3, '2023-08-01', NULL, '2026-07-23 09:45:21.836316', '2026-07-23 09:45:21.836354', NULL),
	(7, 'EMP2026007', '家豪', '許', 'G123456785', 1, '1987-04-30', 'jiahao.hsu@company.com', 'personal_emp2026007@gmail.com', '0978901234', 104, 40, 1, '2018-05-20', NULL, '2026-07-23 09:45:21.840762', '2026-07-23 09:45:21.840799', NULL),
	(8, 'EMP2026008', '怡婷', '郭', 'H223456786', 2, '1996-10-10', 'yiting.guo@company.com', 'personal_emp2026008@gmail.com', '0989012345', 104, 41, 3, '2024-01-15', NULL, '2026-07-23 09:45:21.845273', '2026-07-23 09:45:21.845310', NULL),
	(9, 'EMP2026009', '文彬', '曾', 'I123456787', 3, '1991-03-25', 'wenbin.tseng@company.com', 'personal_emp2026009@gmail.com', '0990123456', 101, 12, 2, '2022-11-01', NULL, '2026-07-23 09:45:21.849255', '2026-07-23 09:45:21.849290', NULL),
	(10, 'EMP2026010', '家瑋', '鄭', 'J123456788', 1, '1984-09-05', 'jiawei.cheng@company.com', 'personal_emp2026010@gmail.com', '0901234567', 101, 1, 1, '2017-07-01', NULL, '2026-07-23 09:45:21.853724', '2026-07-23 09:45:21.853760', NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
