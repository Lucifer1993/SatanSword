/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : localhost:3306
 Source Schema         : SatanSword

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 14/06/2020 21:09:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cmsprint
-- ----------------------------
DROP TABLE IF EXISTS `cmsprint`;
CREATE TABLE `cmsprint` (
  `cmsname` varchar(50) NOT NULL,
  `staticurl` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `checksum` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `homeurl` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `keyword` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `type` varchar(50) NOT NULL,
  `remark` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for hostexploit
-- ----------------------------
DROP TABLE IF EXISTS `hostexploit`;
CREATE TABLE `hostexploit` (
  `vulname` varchar(50) NOT NULL,
  `description` varchar(150) DEFAULT NULL,
  `poc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `exp` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `sysname` varchar(50) DEFAULT NULL,
  `param` varchar(20) DEFAULT NULL,
  `level` varchar(10) DEFAULT NULL,
  `extfile` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`vulname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for hostprint
-- ----------------------------
DROP TABLE IF EXISTS `hostprint`;
CREATE TABLE `hostprint` (
  `servicename` varchar(50) NOT NULL,
  `servicepoc` varchar(5000) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`servicename`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for hostrecon
-- ----------------------------
DROP TABLE IF EXISTS `hostrecon`;
CREATE TABLE `hostrecon` (
  `Project` varchar(100) DEFAULT NULL,
  `Host` varchar(255) DEFAULT NULL,
  `Port` varchar(50) DEFAULT NULL,
  `Service` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for hostvulnlist
-- ----------------------------
DROP TABLE IF EXISTS `hostvulnlist`;
CREATE TABLE `hostvulnlist` (
  `vulnhost` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `vulnport` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `vulnname` varchar(255) DEFAULT NULL,
  `isvul` varchar(10) DEFAULT NULL,
  `payload` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `proof` varchar(255) DEFAULT NULL,
  `exception` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for webexploit
-- ----------------------------
DROP TABLE IF EXISTS `webexploit`;
CREATE TABLE `webexploit` (
  `vulname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `poc` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `cmsname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `param` varchar(20) DEFAULT NULL,
  `level` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `extfile` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`vulname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for webrecon
-- ----------------------------
DROP TABLE IF EXISTS `webrecon`;
CREATE TABLE `webrecon` (
  `Project` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `URL` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cdnheader` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Dig` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Headers` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Whois` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Builtwith` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Mycdn` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `wappalyzer` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Whatweb` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Hsec` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Iprecon` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for webvulnlist
-- ----------------------------
DROP TABLE IF EXISTS `webvulnlist`;
CREATE TABLE `webvulnlist` (
  `url` varchar(255) DEFAULT NULL,
  `vulname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `vulnurl` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `isvul` varchar(10) DEFAULT NULL,
  `payload` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `proof` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `exception` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
