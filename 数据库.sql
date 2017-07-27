-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 2017-07-27 03:28:50
-- 服务器版本： 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `epay`
--

-- --------------------------------------------------------

--
-- 表的结构 `commodity`
--

CREATE TABLE IF NOT EXISTS `commodity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `price` int(11) NOT NULL,
  `uid` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- 转存表中的数据 `commodity`
--

INSERT INTO `commodity` (`id`, `name`, `price`, `uid`) VALUES
(1, '怡宝矿泉水', 2, ''),
(2, '茶派', 5, ''),
(3, '康帅傅方便面', 4, ''),
(4, '六亿核桃', 4, ''),
(5, '晨光黑色笔芯', 1, ''),
(6, 'YSL #52号', 326, ''),
(7, '10345', 111, 'advertising'),
(8, '10345', 111, 'advertising'),
(9, '10345', 111, 'advertising'),
(10, '10345', 111, 'advertising'),
(11, '10345', 111, 'advertising'),
(12, '10345', 111, 'advertising');

-- --------------------------------------------------------

--
-- 表的结构 `commodity_detail`
--

CREATE TABLE IF NOT EXISTS `commodity_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `price` int(11) NOT NULL,
  `uid` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `commodity_detail`
--

INSERT INTO `commodity_detail` (`id`, `name`, `price`, `uid`) VALUES
(1, '怡宝款泉水', 2, '22810085255'),
(2, '奥利奥夹心饼干', 6, '18217311591');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
