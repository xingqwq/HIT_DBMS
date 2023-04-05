-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1:3306
-- 生成日期： 2023-04-03 13:38:22
-- 服务器版本： 8.0.31
-- PHP 版本： 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `lab1`
--

-- --------------------------------------------------------

--
-- 表的结构 `acti`
--

DROP TABLE IF EXISTS `acti`;
CREATE TABLE IF NOT EXISTS `acti` (
  `活动编号` int NOT NULL AUTO_INCREMENT,
  `名称` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `内容` text NOT NULL,
  `参与方式` tinytext NOT NULL,
  PRIMARY KEY (`活动编号`),
  UNIQUE KEY `名称` (`名称`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `acti`
--

INSERT INTO `acti` (`活动编号`, `名称`, `内容`, `参与方式`) VALUES
(1, '拉新人', '拉新人赚积分', '点击加入即可'),
(3, '投稿', '投稿赚积分', '点击加入即可'),
(4, '内测', '赚积分', '点击加入即可'),
(5, '投票', '选出你最喜爱的创作组', '点击加入即可'),
(6, '天选板块', '选出你最喜爱的板块', '点击加入即可');

-- --------------------------------------------------------

--
-- 表的结构 `com_doc`
--

DROP TABLE IF EXISTS `com_doc`;
CREATE TABLE IF NOT EXISTS `com_doc` (
  `用户编号t` int NOT NULL,
  `文章编号t` int NOT NULL,
  `评论时间` date NOT NULL,
  `情绪` tinytext NOT NULL,
  PRIMARY KEY (`用户编号t`,`文章编号t`),
  KEY `评论文章文章编号` (`文章编号t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `com_doc`
--

INSERT INTO `com_doc` (`用户编号t`, `文章编号t`, `评论时间`, `情绪`) VALUES
(1, 3, '2023-03-27', 'HATE'),
(1, 7, '2023-03-27', 'HATE'),
(3, 7, '2023-03-27', 'LIKE'),
(4, 3, '2023-03-22', 'LIKE'),
(4, 8, '2023-03-22', 'NO LIKE'),
(5, 4, '2023-03-27', 'SUB'),
(5, 7, '2023-03-27', 'SUB'),
(5, 8, '2023-03-27', 'LIKE'),
(5, 9, '2023-03-27', 'SUB'),
(5, 10, '2023-03-27', 'SUB'),
(12, 3, '2023-03-29', 'LIKE'),
(12, 7, '2023-03-29', 'LIKE'),
(12, 8, '2023-03-29', 'HATE'),
(12, 9, '2023-03-29', 'HATE'),
(12, 10, '2023-03-29', 'HATE'),
(22, 1, '2023-03-27', 'NO LIKE'),
(22, 4, '2023-03-27', 'SUB'),
(22, 8, '2023-03-27', 'SUB'),
(22, 9, '2023-03-27', 'NO LIKE'),
(22, 10, '2023-03-27', 'HATE');

-- --------------------------------------------------------

--
-- 表的结构 `creation`
--

DROP TABLE IF EXISTS `creation`;
CREATE TABLE IF NOT EXISTS `creation` (
  `板块编号` int NOT NULL,
  `创作组编号` int NOT NULL AUTO_INCREMENT,
  `名称` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `简介` text NOT NULL,
  PRIMARY KEY (`创作组编号`),
  UNIQUE KEY `名称` (`名称`),
  KEY `创作组服务板块` (`板块编号`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `creation`
--

INSERT INTO `creation` (`板块编号`, `创作组编号`, `名称`, `简介`) VALUES
(1, 2, '原始创作组', '原始创作组致力于氪金软文'),
(1, 3, 'OpenAI', '牛逼的AI创作组'),
(2, 4, 'MidJourney', '生成插画大模型创作者'),
(6, 5, 'DBMS', '数据库管理系统');

-- --------------------------------------------------------

--
-- 表的结构 `creation_per`
--

DROP TABLE IF EXISTS `creation_per`;
CREATE TABLE IF NOT EXISTS `creation_per` (
  `身份证号` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `姓名` text NOT NULL,
  `联系方式` text NOT NULL,
  PRIMARY KEY (`身份证号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `creation_per`
--

INSERT INTO `creation_per` (`身份证号`, `姓名`, `联系方式`) VALUES
('271889198705128764', '玄五', '17534893574'),
('450009199812134567', '周一宁', '12793456523'),
('461112198110238764', '张三', '13075987465'),
('461112198705128764', '李四', '13043677465');

-- --------------------------------------------------------

--
-- 表的结构 `doc`
--

DROP TABLE IF EXISTS `doc`;
CREATE TABLE IF NOT EXISTS `doc` (
  `文章编号` int NOT NULL AUTO_INCREMENT,
  `名称` tinytext NOT NULL,
  `存储地址` text NOT NULL,
  PRIMARY KEY (`文章编号`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `doc`
--

INSERT INTO `doc` (`文章编号`, `名称`, `存储地址`) VALUES
(1, 'chatGPT使用指南', './text.txt\r\n'),
(3, 'DV使用指南', './text.txt\r\n'),
(4, 'chatGPT4升级', './text.txt\r\n'),
(5, '科学上网', './text.txt\r\n'),
(6, 'RM2023超级对抗赛规则', './text.txt\r\n'),
(7, 'RC比赛时间', './text.txt\r\n'),
(8, 'RC活动名单', './text.txt\r\n'),
(9, 'NLP前景', './text.txt\r\n'),
(10, 'DBMS最新综述', './xingqwq'),
(26, 'DBMS实验二要验收啦！', './xingqwq');

--
-- 触发器 `doc`
--
DROP TRIGGER IF EXISTS `delete_page`;
DELIMITER $$
CREATE TRIGGER `delete_page` BEFORE DELETE ON `doc` FOR EACH ROW begin       
    DELETE FROM pub_doc WHERE 文章编号t = old.文章编号;
    DELETE FROM com_doc WHERE 文章编号t = old.文章编号;
    DELETE FROM join_topic WHERE 文章编号t = old.文章编号;
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- 表的结构 `join_acti`
--

DROP TABLE IF EXISTS `join_acti`;
CREATE TABLE IF NOT EXISTS `join_acti` (
  `用户编号t` int NOT NULL,
  `活动编号t` int NOT NULL,
  `参与时间` date NOT NULL,
  PRIMARY KEY (`用户编号t`,`活动编号t`),
  KEY `参与活动编号` (`活动编号t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `join_acti`
--

INSERT INTO `join_acti` (`用户编号t`, `活动编号t`, `参与时间`) VALUES
(22, 3, '2022-06-19');

-- --------------------------------------------------------

--
-- 表的结构 `join_topic`
--

DROP TABLE IF EXISTS `join_topic`;
CREATE TABLE IF NOT EXISTS `join_topic` (
  `文章编号t` int NOT NULL,
  `话题编号t` int NOT NULL,
  `发布时间` date NOT NULL,
  PRIMARY KEY (`文章编号t`,`话题编号t`),
  KEY `参与话题话题编号` (`话题编号t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `join_topic`
--

INSERT INTO `join_topic` (`文章编号t`, `话题编号t`, `发布时间`) VALUES
(4, 6, '2022-06-19'),
(26, 4, '2023-03-27'),
(26, 6, '2023-03-27');

-- --------------------------------------------------------

--
-- 表的结构 `le_topic`
--

DROP TABLE IF EXISTS `le_topic`;
CREATE TABLE IF NOT EXISTS `le_topic` (
  `板块编号t` int NOT NULL,
  `创作组编号t` int NOT NULL,
  `话题编号t` int NOT NULL,
  `开始时间` date NOT NULL,
  `结束时间` date NOT NULL,
  PRIMARY KEY (`板块编号t`,`创作组编号t`,`话题编号t`),
  KEY `负责话题创作组编号` (`创作组编号t`),
  KEY `负责话题话题编号` (`话题编号t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `ma_creation`
--

DROP TABLE IF EXISTS `ma_creation`;
CREATE TABLE IF NOT EXISTS `ma_creation` (
  `身份证号t` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `创作组编号t` int NOT NULL,
  `开始时间` int NOT NULL,
  `结束时间` int NOT NULL,
  PRIMARY KEY (`身份证号t`,`创作组编号t`),
  KEY `管理创作组创作组编号` (`创作组编号t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `ma_creation`
--

INSERT INTO `ma_creation` (`身份证号t`, `创作组编号t`, `开始时间`, `结束时间`) VALUES
('450009199812134567', 5, 2020, 2035);

-- --------------------------------------------------------

--
-- 表的结构 `ma_plate`
--

DROP TABLE IF EXISTS `ma_plate`;
CREATE TABLE IF NOT EXISTS `ma_plate` (
  `身份证号t` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `板块编号t` int NOT NULL,
  `开始时间` date NOT NULL,
  `结束时间` date NOT NULL,
  PRIMARY KEY (`身份证号t`,`板块编号t`),
  KEY `管理板块板块编号` (`板块编号t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `ma_plate`
--

INSERT INTO `ma_plate` (`身份证号t`, `板块编号t`, `开始时间`, `结束时间`) VALUES
('147642198705128764', 1, '2023-03-08', '2025-03-12'),
('238880200212180387', 3, '2020-03-20', '2035-03-19');

-- --------------------------------------------------------

--
-- 表的结构 `plate`
--

DROP TABLE IF EXISTS `plate`;
CREATE TABLE IF NOT EXISTS `plate` (
  `板块编号` int NOT NULL AUTO_INCREMENT,
  `名称` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `简介` text NOT NULL,
  PRIMARY KEY (`板块编号`),
  UNIQUE KEY `名称` (`名称`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `plate`
--

INSERT INTO `plate` (`板块编号`, `名称`, `简介`) VALUES
(1, 'NLP', '自然语言处理相关板块。'),
(2, 'CV', '计算机视觉板块'),
(3, 'RoboMaster', '牛马的机器人赛事'),
(5, 'RoboCon', '更加牛马的机器人赛事'),
(6, '人工智能', '不那么高深的科技板块'),
(12, '微积分', '微积分（Calculus），数学概念，是高等数学中研究函数的微分（Differentiation）、积分（Integration）以及有关概念和应用的数学分支。它是数学的一个基础学科，内容主要包括极限、微分学、积分学及其应用。');

-- --------------------------------------------------------

--
-- 替换视图以便查看 `plate_info`
-- （参见下面的实际视图）
--
DROP VIEW IF EXISTS `plate_info`;
CREATE TABLE IF NOT EXISTS `plate_info` (
`名称` varchar(20)
,`姓名` text
,`板块编号` int
,`简介` text
,`联系方式` text
,`身份证号` varchar(18)
);

-- --------------------------------------------------------

--
-- 表的结构 `plate_per`
--

DROP TABLE IF EXISTS `plate_per`;
CREATE TABLE IF NOT EXISTS `plate_per` (
  `身份证号` varchar(18) NOT NULL,
  `姓名` text NOT NULL,
  `联系方式` text NOT NULL,
  PRIMARY KEY (`身份证号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `plate_per`
--

INSERT INTO `plate_per` (`身份证号`, `姓名`, `联系方式`) VALUES
('117643199612174864', '阿周', '17613487645'),
('147642198705128764', '阿兴', '17613487465'),
('238880200212180387', '王笑笑', '12793456523'),
('354216200004254869', '阿王', '13417468465'),
('420001200406237985', '阿张', '17834487465');

-- --------------------------------------------------------

--
-- 表的结构 `pub_doc`
--

DROP TABLE IF EXISTS `pub_doc`;
CREATE TABLE IF NOT EXISTS `pub_doc` (
  `板块编号t` int NOT NULL,
  `创作组编号t` int NOT NULL,
  `文章编号t` int NOT NULL,
  `发表时间` int NOT NULL,
  PRIMARY KEY (`板块编号t`,`创作组编号t`,`文章编号t`),
  KEY `发布文章创作组编号` (`创作组编号t`),
  KEY `发布文章文章编号` (`文章编号t`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `pub_doc`
--

INSERT INTO `pub_doc` (`板块编号t`, `创作组编号t`, `文章编号t`, `发表时间`) VALUES
(5, 3, 26, 2023);

-- --------------------------------------------------------

--
-- 表的结构 `topic`
--

DROP TABLE IF EXISTS `topic`;
CREATE TABLE IF NOT EXISTS `topic` (
  `话题编号` int NOT NULL AUTO_INCREMENT,
  `名称` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `简介` text NOT NULL,
  `创建时间` date NOT NULL,
  PRIMARY KEY (`话题编号`),
  UNIQUE KEY `名称` (`名称`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `topic`
--

INSERT INTO `topic` (`话题编号`, `名称`, `简介`, `创建时间`) VALUES
(2, 'DV', 'AI作画', '2023-03-16'),
(3, 'RM十佳画面', 'RM十佳画面', '2023-03-16'),
(4, 'RC十佳画面', 'RC十佳画面', '2023-03-16'),
(5, 'RM MVP', 'RM MVP', '2023-03-16'),
(6, 'chatGPT', 'OpenAI 发布的新一代预训练的大模型', '2023-03-16');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `用户编号` int NOT NULL AUTO_INCREMENT,
  `名称` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `联系方式` text NOT NULL,
  PRIMARY KEY (`用户编号`),
  UNIQUE KEY `名称` (`名称`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`用户编号`, `名称`, `联系方式`) VALUES
(1, 'xingqwq', '176978894561'),
(3, '放肆按', '17769853674'),
(4, '强强', '17647613674'),
(5, '阿伟', '17764353674'),
(12, 'test', '66894523'),
(22, '玉院士', '19872553809');

--
-- 触发器 `user`
--
DROP TRIGGER IF EXISTS `delete_user`;
DELIMITER $$
CREATE TRIGGER `delete_user` BEFORE DELETE ON `user` FOR EACH ROW begin       
    DELETE FROM join_acti WHERE 用户编号t = old.用户编号;
    DELETE FROM com_doc WHERE 用户编号t = old.用户编号;
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- 替换视图以便查看 `user_com`
-- （参见下面的实际视图）
--
DROP VIEW IF EXISTS `user_com`;
CREATE TABLE IF NOT EXISTS `user_com` (
`情绪` tinytext
,`文章名` tinytext
,`文章编号` int
,`用户昵称` varchar(11)
,`用户编号` int
,`评论时间` date
);

-- --------------------------------------------------------

--
-- 视图结构 `plate_info`
--
DROP TABLE IF EXISTS `plate_info`;

DROP VIEW IF EXISTS `plate_info`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `plate_info`  AS SELECT `plate_per`.`身份证号` AS `身份证号`, `plate_per`.`姓名` AS `姓名`, `plate_per`.`联系方式` AS `联系方式`, `plate`.`板块编号` AS `板块编号`, `plate`.`名称` AS `名称`, `plate`.`简介` AS `简介` FROM ((`plate` join `plate_per`) join `ma_plate`) WHERE ((`plate`.`板块编号` = `ma_plate`.`板块编号t`) AND (`plate_per`.`身份证号` = `ma_plate`.`身份证号t`))  ;

-- --------------------------------------------------------

--
-- 视图结构 `user_com`
--
DROP TABLE IF EXISTS `user_com`;

DROP VIEW IF EXISTS `user_com`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `user_com`  AS SELECT `com_doc`.`评论时间` AS `评论时间`, `user`.`用户编号` AS `用户编号`, `user`.`名称` AS `用户昵称`, `doc`.`文章编号` AS `文章编号`, `doc`.`名称` AS `文章名`, `com_doc`.`情绪` AS `情绪` FROM ((`user` join `com_doc`) join `doc`) WHERE ((`user`.`用户编号` = `com_doc`.`用户编号t`) AND (`doc`.`文章编号` = `com_doc`.`文章编号t`))  ;

--
-- 限制导出的表
--

--
-- 限制表 `com_doc`
--
ALTER TABLE `com_doc`
  ADD CONSTRAINT `评论文章文章编号` FOREIGN KEY (`文章编号t`) REFERENCES `doc` (`文章编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `评论文章用户编号` FOREIGN KEY (`用户编号t`) REFERENCES `user` (`用户编号`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `creation`
--
ALTER TABLE `creation`
  ADD CONSTRAINT `创作组服务板块` FOREIGN KEY (`板块编号`) REFERENCES `plate` (`板块编号`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `join_acti`
--
ALTER TABLE `join_acti`
  ADD CONSTRAINT `参与活动用户编号` FOREIGN KEY (`用户编号t`) REFERENCES `user` (`用户编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `参与活动编号` FOREIGN KEY (`活动编号t`) REFERENCES `acti` (`活动编号`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `join_topic`
--
ALTER TABLE `join_topic`
  ADD CONSTRAINT `参与话题文章编号` FOREIGN KEY (`文章编号t`) REFERENCES `doc` (`文章编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `参与话题话题编号` FOREIGN KEY (`话题编号t`) REFERENCES `topic` (`话题编号`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `le_topic`
--
ALTER TABLE `le_topic`
  ADD CONSTRAINT `负责话题创作组编号` FOREIGN KEY (`创作组编号t`) REFERENCES `creation` (`创作组编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `负责话题板块编号` FOREIGN KEY (`板块编号t`) REFERENCES `plate` (`板块编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `负责话题话题编号` FOREIGN KEY (`话题编号t`) REFERENCES `topic` (`话题编号`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `ma_creation`
--
ALTER TABLE `ma_creation`
  ADD CONSTRAINT `管理创作组创作组编号` FOREIGN KEY (`创作组编号t`) REFERENCES `creation` (`创作组编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `管理创作组身份证号` FOREIGN KEY (`身份证号t`) REFERENCES `creation_per` (`身份证号`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `ma_plate`
--
ALTER TABLE `ma_plate`
  ADD CONSTRAINT `管理板块板块编号` FOREIGN KEY (`板块编号t`) REFERENCES `plate` (`板块编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `管理板块身份证号` FOREIGN KEY (`身份证号t`) REFERENCES `plate_per` (`身份证号`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `pub_doc`
--
ALTER TABLE `pub_doc`
  ADD CONSTRAINT `发布文章创作组编号` FOREIGN KEY (`创作组编号t`) REFERENCES `creation` (`创作组编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `发布文章文章编号` FOREIGN KEY (`文章编号t`) REFERENCES `doc` (`文章编号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `发布文章板块编号` FOREIGN KEY (`板块编号t`) REFERENCES `plate` (`板块编号`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
