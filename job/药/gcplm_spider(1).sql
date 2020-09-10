/*
 Navicat Premium Data Transfer

 Source Server         : 20.50.59.220gcptest
 Source Server Type    : MySQL
 Source Server Version : 50718
 Source Host           : 20.50.59.220:3306
 Source Schema         : gcplm_spider

 Target Server Type    : MySQL
 Target Server Version : 50718
 File Encoding         : 65001

 Date: 08/09/2020 15:43:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for se_spider_item
-- ----------------------------
DROP TABLE IF EXISTS `se_spider_item`;
CREATE TABLE `se_spider_item`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `source` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '数据来源（爬取网站域名）',
  `source_id` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '资源主键ID',
  `source_link` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '资源网络地址',
  `source_data` json COMMENT '资源简介对象',
  `weight` int(11) NOT NULL DEFAULT 0 COMMENT '权重',
  `count` int(11) NOT NULL DEFAULT 0 COMMENT '爬取次数',
  `last_date` date DEFAULT '2019-01-01' COMMENT '最后爬取日期',
  `created` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated` datetime(0) DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 413790 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_seq_trial
-- ----------------------------
DROP TABLE IF EXISTS `t_seq_trial`;
CREATE TABLE `t_seq_trial`  (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `stub` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `stub`(`stub`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 714132 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = 'Trial表自增主键生成器' ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for t_seq_trial_other
-- ----------------------------
DROP TABLE IF EXISTS `t_seq_trial_other`;
CREATE TABLE `t_seq_trial_other`  (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `stub` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `stub`(`stub`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 4275540 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '其它Trial表自增主键生成器' ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for t_trial
-- ----------------------------
DROP TABLE IF EXISTS `t_trial`;
CREATE TABLE `t_trial`  (
  `id` bigint(20) NOT NULL COMMENT '主键ID',
  `OID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '原始ID',
  `source` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '数据来源',
  `source_link` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '数据原始网络地址',
  `language` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '数据语言',
  `is_master` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '是否主数据（1：是，0：否）',
  `trial_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '注册号 - （本系统内部编号）',
  `chinadrugtrials_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '登记号 - （药物临床试验登记与信息公示平台）',
  `chictr_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '注册号 - （中国临床试验注册中心）',
  `clinicaltrials_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '注册号 - （美国临床试验注册中心）',
  `target_disease` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '研究疾病',
  `public_title` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '研究题目',
  `scientific_title` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '研究课题专业名称',
  `protocol_code` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '研究方案编号',
  `clinical_record_no` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '临床申请受理号',
  `drug_record_no` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '化学药备案号',
  `drug_name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '药物名称',
  `drug_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '药物类型',
  `trial_status` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '试验状态',
  `contact_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '联系人姓名',
  `contact_phone` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '联系人电话',
  `contact_email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '联系人Email',
  `contact_address` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '联系人邮政地址',
  `contact_zip_code` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '联系人邮编',
  `study_plan_start_date` date DEFAULT NULL COMMENT '试验计划开始日期',
  `study_plan_end_date` date DEFAULT NULL COMMENT '试验计划终止日期',
  `study_start_date` date DEFAULT NULL COMMENT '试验开始日期',
  `study_end_date` date DEFAULT NULL COMMENT '试验终止日期',
  `first_enter_date` date DEFAULT NULL COMMENT '第一例受试者入组日期',
  `publish_date` date DEFAULT NULL COMMENT '首次公示日期',
  `source_of_funding` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '经费或物资来源',
  `data_committee` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '数据管理委员会',
  `study_purpose` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '研究目的',
  `study_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '研究类型',
  `study_medicine_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '药物研究分类',
  `study_phase` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '研究所处阶段',
  `study_design` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '研究设计',
  `study_randomise` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '随机化',
  `study_blinding` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '盲法',
  `study_scope` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '试验范围',
  `trial_insure` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '为受试者购买试验伤害保险',
  `min_age` int(11) DEFAULT NULL COMMENT '受试者-年龄最小值',
  `max_age` int(11) DEFAULT NULL COMMENT '受试者-年龄最大值',
  `gender` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '受试者-性别',
  `accept_healthy` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '受试者-接受健康志愿者',
  `inclusion_criteria` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '受试者-入选标准',
  `exclusion_criteria` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '受试者-排除标准',
  `target_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '受试者-预计人数',
  `actual_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '受试者-实际人数',
  `raw` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '完整数据对象',
  `create_time` bigint(20) NOT NULL COMMENT '创建时间',
  `update_time` bigint(20) DEFAULT NULL COMMENT '更新时间',
  `is_del` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否删除：0-未删除；1-已删除',
  `is_original` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否是爬虫数据：0-爬虫数据（原数据）；1-系统新增或者修改数据',
  `create_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '创建人ID',
  `update_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '更新人ID',
  `platform_type_dict` int(11) DEFAULT NULL COMMENT '平台类型字典',
  `drug_type_dict` int(11) DEFAULT NULL COMMENT '药物类型字典',
  `trial_status_dict` int(11) DEFAULT NULL COMMENT '试验状态字典',
  `study_medicine_type_dict` int(11) DEFAULT NULL COMMENT '药物研究分类字典',
  `study_phase_dict` int(11) DEFAULT NULL COMMENT '研究所处阶段字典',
  `study_design_dict` int(11) DEFAULT NULL COMMENT '研究设计字典',
  `study_type_dict` int(11) DEFAULT NULL COMMENT '研究类型字典',
  `language_dict` int(11) DEFAULT NULL COMMENT '语言数据字典',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '临床试验项目信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_trial_ethic
-- ----------------------------
DROP TABLE IF EXISTS `t_trial_ethic`;
CREATE TABLE `t_trial_ethic`  (
  `id` bigint(20) NOT NULL COMMENT '主键ID',
  `t_id` bigint(20) NOT NULL COMMENT '研究项目ID',
  `name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '伦理委员会名称',
  `approval_date` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '批准日期',
  `approval_result` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '审查结论',
  `approval_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '批件文号',
  `contact` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '伦理委员会联系人',
  `address` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '伦理委员会联系地址',
  `phone` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '伦理委员会联系人电话',
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '伦理委员会联系人邮箱',
  `create_time` bigint(20) NOT NULL COMMENT '创建时间',
  `update_time` bigint(20) DEFAULT NULL COMMENT '更新时间',
  `is_del` tinyint(4) DEFAULT 0 COMMENT '是否删除：0-未删除；1-已删除',
  `create_user_id` int(11) DEFAULT 0 COMMENT '创建人ID',
  `update_user_id` int(11) DEFAULT 0 COMMENT '更新人ID',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tId`(`t_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '伦理委员会信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_trial_intervene
-- ----------------------------
DROP TABLE IF EXISTS `t_trial_intervene`;
CREATE TABLE `t_trial_intervene`  (
  `id` bigint(20) NOT NULL COMMENT '主键ID',
  `t_id` bigint(20) NOT NULL COMMENT '研究项目ID',
  `category` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '分类（试验药、对照药）',
  `name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '名称',
  `usage` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '用法',
  `group` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '组别',
  `sample_size` int(11) DEFAULT NULL COMMENT '样本量',
  `intervention` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '干预措施',
  `intervention_code` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '干预措施代码或名称',
  `create_time` bigint(20) NOT NULL COMMENT '创建时间',
  `update_time` bigint(20) DEFAULT NULL COMMENT '更新时间',
  `is_del` tinyint(4) DEFAULT 0 COMMENT '是否删除：0-未删除；1-已删除',
  `create_user_id` int(11) DEFAULT 0 COMMENT '创建人ID',
  `update_user_id` int(11) DEFAULT 0 COMMENT '更新人ID',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tId`(`t_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '分组与干预措施' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_trial_outcomes
-- ----------------------------
DROP TABLE IF EXISTS `t_trial_outcomes`;
CREATE TABLE `t_trial_outcomes`  (
  `id` bigint(20) NOT NULL COMMENT '主键ID',
  `t_id` bigint(20) NOT NULL COMMENT '研究项目ID',
  `type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '指标类型（主要终点指标及评价时间、次要终点指标及评价时间）',
  `outcome` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '指标中文名',
  `time_point` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '测量时间点',
  `method` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '测量方法',
  `outcome_end` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '终点指标选择',
  `create_time` bigint(20) NOT NULL COMMENT '创建时间',
  `update_time` bigint(20) DEFAULT NULL COMMENT '更新时间',
  `is_del` tinyint(4) DEFAULT 0 COMMENT '是否删除：0-未删除；1-已删除',
  `create_user_id` int(11) DEFAULT 0 COMMENT '创建人ID',
  `update_user_id` int(11) DEFAULT 0 COMMENT '更新人ID',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tId`(`t_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '测量指标' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_trial_site
-- ----------------------------
DROP TABLE IF EXISTS `t_trial_site`;
CREATE TABLE `t_trial_site`  (
  `id` bigint(20) NOT NULL COMMENT '主键ID',
  `t_id` bigint(20) NOT NULL COMMENT '研究项目ID',
  `is_primary` tinyint(4) NOT NULL COMMENT '是否主要（1：是，0：否）',
  `site_name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '机构名称',
  `pi_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '主要研究者',
  `country` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '国家',
  `province` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '省(直辖市)',
  `city` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '市(区县)',
  `level` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '单位级别',
  `create_time` bigint(20) NOT NULL COMMENT '创建时间',
  `update_time` bigint(20) DEFAULT NULL COMMENT '更新时间',
  `hospital_id` int(11) DEFAULT NULL COMMENT '医院ID',
  `is_del` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否删除：0-未删除；1-已删除',
  `is_original` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否是爬虫数据：0-爬虫数据（原数据）；1-系统新增或者修改数据',
  `create_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '创建人ID',
  `update_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '更新人ID',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tId`(`t_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '研究机构信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_trial_sponsor
-- ----------------------------
DROP TABLE IF EXISTS `t_trial_sponsor`;
CREATE TABLE `t_trial_sponsor`  (
  `id` bigint(20) NOT NULL COMMENT '主键ID',
  `t_id` bigint(20) NOT NULL COMMENT '研究项目ID',
  `name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '名称，单位(医院)',
  `country` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '国家',
  `province` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '省(直辖市)',
  `city` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '市(区县)',
  `address` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '地址',
  `create_time` bigint(20) NOT NULL COMMENT '创建时间',
  `update_time` bigint(20) DEFAULT NULL COMMENT '更新时间',
  `enterprise_id` int(11) DEFAULT NULL COMMENT '企业ID',
  `is_del` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否删除：0-未删除；1-已删除',
  `is_original` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否是爬虫数据：0-爬虫数据（原数据）；1-系统新增或者修改数据',
  `create_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '创建人ID',
  `update_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '更新人ID',
  `enterprise_type` tinyint(4) DEFAULT NULL COMMENT '类型：1-企业, 2-医院',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tId`(`t_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '申办机构信息' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_trial_studier
-- ----------------------------
DROP TABLE IF EXISTS `t_trial_studier`;
CREATE TABLE `t_trial_studier`  (
  `id` bigint(20) NOT NULL COMMENT '主键ID',
  `t_id` bigint(20) NOT NULL COMMENT '研究项目ID',
  `name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '姓名',
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '职称',
  `phone` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '电话',
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '电子邮件',
  `address` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '邮政地址',
  `zip_code` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '邮编',
  `organize` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '所属机构名称',
  `create_time` bigint(20) NOT NULL COMMENT '创建时间',
  `update_time` bigint(20) DEFAULT NULL COMMENT '更新时间',
  `studier_id` int(11) DEFAULT NULL COMMENT '研究者ID',
  `is_del` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否删除：0-未删除；1-已删除',
  `is_original` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否是爬虫数据：0-爬虫数据（原数据）；1-系统新增或者修改数据',
  `create_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '创建人ID',
  `update_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '更新人ID',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tId`(`t_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '研究者信息（主要研究者信息）' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Function structure for fn_get_trial_id
-- ----------------------------
DROP FUNCTION IF EXISTS `fn_get_trial_id`;
delimiter ;;
CREATE DEFINER=`root`@`%` FUNCTION `fn_get_trial_id`() RETURNS bigint(20)
BEGIN  
	REPLACE INTO t_seq_trial (stub) VALUES ('a');
	RETURN  LAST_INSERT_ID() ;
END
;;
delimiter ;

-- ----------------------------
-- Function structure for fn_get_trial_other_id
-- ----------------------------
DROP FUNCTION IF EXISTS `fn_get_trial_other_id`;
delimiter ;;
CREATE DEFINER=`root`@`%` FUNCTION `fn_get_trial_other_id`() RETURNS bigint(20)
BEGIN  
	REPLACE INTO t_seq_trial_other (stub) VALUES ('a');
	RETURN  LAST_INSERT_ID() ;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
