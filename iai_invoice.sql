-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Czas generowania: 29 Kwi 2020, 11:55
-- Wersja serwera: 5.7.29-0ubuntu0.18.04.1
-- Wersja PHP: 7.2.24-0ubuntu0.18.04.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `iai_invoice`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
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
(25, 'Can add firm data', 7, 'add_firmdata'),
(26, 'Can change firm data', 7, 'change_firmdata'),
(27, 'Can delete firm data', 7, 'delete_firmdata'),
(28, 'Can view firm data', 7, 'view_firmdata'),
(29, 'Can add invoices0', 8, 'add_invoices0'),
(30, 'Can change invoices0', 8, 'change_invoices0'),
(31, 'Can delete invoices0', 8, 'delete_invoices0'),
(32, 'Can view invoices0', 8, 'view_invoices0'),
(33, 'Can add invoices', 9, 'add_invoices'),
(34, 'Can change invoices', 9, 'change_invoices'),
(35, 'Can delete invoices', 9, 'delete_invoices'),
(36, 'Can view invoices', 9, 'view_invoices'),
(37, 'Can add invoices items', 10, 'add_invoicesitems'),
(38, 'Can change invoices items', 10, 'change_invoicesitems'),
(39, 'Can delete invoices items', 10, 'delete_invoicesitems'),
(40, 'Can view invoices items', 10, 'view_invoicesitems'),
(41, 'Can add vats', 11, 'add_vats'),
(42, 'Can change vats', 11, 'change_vats'),
(43, 'Can delete vats', 11, 'delete_vats'),
(44, 'Can view vats', 11, 'view_vats'),
(45, 'Can add jms', 12, 'add_jms'),
(46, 'Can change jms', 12, 'change_jms'),
(47, 'Can delete jms', 12, 'delete_jms'),
(48, 'Can view jms', 12, 'view_jms'),
(49, 'Can add items', 13, 'add_items'),
(50, 'Can change items', 13, 'change_items'),
(51, 'Can delete items', 13, 'delete_items'),
(52, 'Can view items', 13, 'view_items');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$180000$MaqZqf81dfM5$la3ujcDz932/W7Yae17MWxloIqqNUXgSRZby4lv5t6w=', NULL, 1, 'wiks', '', '', 'wiks@wiks.eu', 1, 1, '2020-04-25 15:45:11.327681'),
(2, 'pbkdf2_sha256$180000$37dWdUmKv7np$I0ySpLyhJPGlYx/VJPrFhdnpyYET7yEBSiE2K8xpPTg=', NULL, 1, 'iai', '', '', 'iai@iai.pl', 1, 1, '2020-04-25 15:45:43.580796');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'invoices', 'invoices'),
(8, 'invoices', 'invoices0'),
(10, 'invoices', 'invoicesitems'),
(13, 'items', 'items'),
(12, 'items', 'jms'),
(11, 'items', 'vats'),
(7, 'myfirm', 'firmdata'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-04-25 15:39:59.628559'),
(2, 'auth', '0001_initial', '2020-04-25 15:40:00.045485'),
(3, 'admin', '0001_initial', '2020-04-25 15:40:01.431436'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-04-25 15:40:01.776587'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-04-25 15:40:01.793866'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-04-25 15:40:02.043436'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-04-25 15:40:02.076201'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-04-25 15:40:02.106084'),
(9, 'auth', '0004_alter_user_username_opts', '2020-04-25 15:40:02.140752'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-04-25 15:40:02.264726'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-04-25 15:40:02.270141'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-04-25 15:40:02.292679'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-04-25 15:40:02.317187'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-04-25 15:40:02.347912'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-04-25 15:40:02.380419'),
(16, 'auth', '0011_update_proxy_permissions', '2020-04-25 15:40:02.405854'),
(17, 'sessions', '0001_initial', '2020-04-25 15:40:02.475934'),
(18, 'myfirm', '0001_initial', '2020-04-25 15:42:35.840748'),
(19, 'items', '0001_initial', '2020-04-25 15:42:36.045718'),
(20, 'invoices', '0001_initial', '2020-04-25 15:42:36.615028'),
(21, 'invoices', '0002_auto_20200425_2137', '2020-04-25 19:37:18.435354'),
(22, 'invoices', '0003_auto_20200425_2321', '2020-04-25 21:21:10.669957'),
(23, 'invoices', '0004_delete_invoices0', '2020-04-28 20:38:36.259940'),
(24, 'items', '0002_auto_20200428_2238', '2020-04-28 20:38:36.459963');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `invoices_invoices`
--

CREATE TABLE `invoices_invoices` (
  `id` int(11) NOT NULL,
  `nr` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `dt_created` date DEFAULT NULL,
  `dt_delivery` date DEFAULT NULL,
  `pay_form_id` int(11) DEFAULT NULL,
  `dt_pait_to` date DEFAULT NULL,
  `person_auth_name` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `price_sum_netto` decimal(6,2) NOT NULL,
  `price_sum_brutto` decimal(6,2) NOT NULL,
  `paid_sum_brutto` decimal(6,2) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `invoices_invoices`
--

INSERT INTO `invoices_invoices` (`id`, `nr`, `dt_created`, `dt_delivery`, `pay_form_id`, `dt_pait_to`, `person_auth_name`, `price_sum_netto`, `price_sum_brutto`, `paid_sum_brutto`, `dt_update`, `customer_id`) VALUES
(6, '44/14', '2020-04-25', '2020-05-25', NULL, '2020-05-25', '', '411.00', '0.00', '0.00', '2020-04-25 21:57:57.832425', 1),
(9, 'ccc', '2020-05-28', '2020-05-28', NULL, '2020-05-28', 'Janek', '290.57', '0.00', '0.00', '2020-05-28 22:10:04.000000', 2),
(10, 'ale/numer', '2020-04-28', '2020-05-08', NULL, '2020-05-08', 'Janko Muzykant', '32.70', '0.00', '0.00', '2020-05-28 23:10:51.000000', 3),
(11, '123', '2020-05-29', '2021-04-29', NULL, '2020-05-29', '', '117.15', '0.00', '0.00', '2020-05-29 08:58:01.000000', 3);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `invoices_invoicesitems`
--

CREATE TABLE `invoices_invoicesitems` (
  `id` int(11) NOT NULL,
  `items_number` double DEFAULT NULL,
  `invoice_id` int(11) NOT NULL,
  `items_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `invoices_invoicesitems`
--

INSERT INTO `invoices_invoicesitems` (`id`, `items_number`, `invoice_id`, `items_id`) VALUES
(17, 5, 6, 57),
(26, 3, 9, 3),
(27, 4, 9, 7),
(29, 3, 11, 65),
(30, 3, 10, 6),
(33, 3, 11, 1),
(34, 2, 10, 65);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `items_items`
--

CREATE TABLE `items_items` (
  `id` int(11) NOT NULL,
  `name` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `price_netto` decimal(10,2) NOT NULL,
  `jm_id` int(11) NOT NULL,
  `vat_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `items_items`
--

INSERT INTO `items_items` (`id`, `name`, `price_netto`, `jm_id`, `vat_id`) VALUES
(1, 'jabłka', '27.95', 1, 4),
(2, 'pomarańcze', '94.09', 2, 1),
(3, 'banany', '87.39', 1, 3),
(4, 'truskawki', '82.96', 1, 3),
(5, 'awokado', '9.50', 2, 2),
(6, 'pomidory', '3.50', 2, 4),
(7, 'ananas', '7.10', 1, 3),
(8, 'grejpfrut', '50.10', 1, 3),
(9, 'cytryny', '44.10', 1, 1),
(10, 'mleko o niskiej zawartości tłuszczu', '27.90', 2, 4),
(11, 'jogurt', '82.20', 2, 3),
(12, 'jajka', '26.80', 2, 4),
(13, 'twarożek', '93.60', 2, 2),
(14, 'ser żółty', '6.90', 1, 3),
(15, 'masło', '1.00', 1, 4),
(16, 'miód', '3.10', 2, 1),
(17, 'pierś z kurczaka', '3.40', 2, 3),
(18, 'szynka z indyka', '62.50', 1, 3),
(19, 'owoce morza', '4.50', 1, 1),
(20, 'łosoś', '5.40', 2, 1),
(21, 'dorsz', '20.20', 1, 2),
(22, 'sól', '4.10', 2, 2),
(23, 'cukier', '49.60', 1, 3),
(24, 'cynamon', '12.50', 1, 4),
(25, 'kolendra', '7.60', 1, 3),
(26, 'oregano', '45.00', 2, 1),
(27, 'czarny pieprz', '19.70', 1, 3),
(28, 'czosnek', '92.60', 1, 2),
(29, 'goździki', '4.70', 1, 2),
(30, 'kminek', '48.80', 2, 1),
(31, 'imbir', '4.70', 1, 4),
(32, 'pietruszka', '89.50', 1, 4),
(33, 'liście bazylii', '17.40', 1, 3),
(34, 'ketchup', '23.80', 1, 2),
(35, 'musztarda', '30.00', 2, 3),
(36, 'cebula', '40.50', 2, 1),
(37, 'ziemniaki', '7.30', 2, 3),
(38, 'brokuły', '61.70', 2, 2),
(39, 'marchew', '20.30', 2, 2),
(40, 'buraki', '18.80', 1, 2),
(41, 'szpinak', '68.60', 2, 1),
(42, 'papryka', '4.20', 2, 2),
(43, 'sałata', '93.80', 2, 1),
(44, 'seler', '0.40', 2, 1),
(45, 'ogórek', '4.50', 2, 3),
(46, 'ciecierzyca', '51.90', 2, 2),
(47, 'fasola', '7.70', 2, 2),
(48, 'soja', '73.30', 1, 1),
(49, 'olej sezamowy', '42.10', 1, 3),
(50, 'olej rzepakowy', '52.10', 1, 3),
(51, 'oliwa z oliwek', '0.40', 2, 1),
(52, 'migdały', '69.60', 2, 1),
(53, 'nasiona lnu', '2.10', 2, 4),
(54, 'orzeszki ziemne', '45.30', 1, 4),
(55, 'orzechy włoskie', '24.70', 2, 1),
(56, 'słonecznik', '31.50', 1, 1),
(57, 'masło orzechowe', '82.20', 1, 3),
(58, 'dżem', '91.70', 1, 1),
(59, 'koncentrat pomidorowy', '3.60', 1, 4),
(60, 'pomidory w puszce', '96.60', 1, 4),
(61, 'tofu', '28.50', 2, 1),
(62, 'pasztet roślinny', '71.40', 2, 3),
(63, 'daktyle', '16.80', 1, 3),
(64, 'rodzynki suszone', '54.30', 2, 2),
(65, 'hummus', '11.10', 1, 3),
(66, 'mąka', '39.40', 1, 3);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `items_jms`
--

CREATE TABLE `items_jms` (
  `id` int(11) NOT NULL,
  `name` longtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `items_jms`
--

INSERT INTO `items_jms` (`id`, `name`) VALUES
(1, 'szt.'),
(2, 'kg');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `items_vats`
--

CREATE TABLE `items_vats` (
  `id` int(11) NOT NULL,
  `percent` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `items_vats`
--

INSERT INTO `items_vats` (`id`, `percent`) VALUES
(1, 7),
(2, 15),
(3, 22),
(4, 23);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `myfirm_firmdata`
--

CREATE TABLE `myfirm_firmdata` (
  `id` int(11) NOT NULL,
  `fname` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `address_json` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `nip` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `regon` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `pesel` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `bank_account` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `icon` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `dt_update` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `myfirm_firmdata`
--

INSERT INTO `myfirm_firmdata` (`id`, `fname`, `address_json`, `email`, `nip`, `regon`, `pesel`, `bank_account`, `icon`, `dt_update`) VALUES
(1, 'WikS.eu', '[\"ul. Pi\\u0142sudskiego 5\\/1\",\"72-600 \\u015awinouj\\u015bcie\"]', 'wiks@wiks.eu', '5732147863', '12345678512347', NULL, '[\"75 1020 4870 0000 5602 0076 5859\",\"PKO BP\"]', NULL, '2020-04-25 15:48:00.095894'),
(2, 'Kupiciel', '[\"ul. Pi\\u0142sudskiego 5/1\", \"72-600 \\u015awinouj\\u015bcie\"]', 'wiks@wiks.eu', '573-214-78-63', '12345678512347', '71050103357', '[\"75 1020 4870 0000 5602 0076 5859\", \"PKO BP\"]', NULL, '2020-04-25 15:48:00.095894'),
(3, 'przekupski', '[\"Przekupin 1\",\"00-950 Warszawa-Przekupin\"]', 'biuro@fnserwis.pl', '8551575195', '320861875', NULL, '[\"94 1090 1492 0000 0001 1438 8447\"]', NULL, '2020-04-28 21:10:28.760608'),
(4, 'Trzecia Sp. z bo.o', '[\"jaka\\u015b jedna linia\"]', NULL, NULL, NULL, '71050103357', '[\"75 1020 4870 0000 5602 0076 5859\"]', NULL, '2020-04-29 10:48:13.000000'),
(8, 'Klient Niewymagający ąę', '[\"ul. Pi\\u0142sudskiego 5\\/1\"]', NULL, NULL, NULL, '71050103357', '[\"75 1020 4870 0000 5602 0076 5859\"]', NULL, '2020-04-29 11:10:05.000000');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `invoices_invoices`
--
ALTER TABLE `invoices_invoices`
  ADD PRIMARY KEY (`id`),
  ADD KEY `invoices_invoices_customer_id_143e6705_fk_myfirm_firmdata_id` (`customer_id`);

--
-- Indexes for table `invoices_invoicesitems`
--
ALTER TABLE `invoices_invoicesitems`
  ADD PRIMARY KEY (`id`),
  ADD KEY `invoices_invoicesite_invoice_id_55c98b5f_fk_invoices_` (`invoice_id`),
  ADD KEY `invoices_invoicesitems_items_id_51634ca0_fk_items_items_id` (`items_id`);

--
-- Indexes for table `items_items`
--
ALTER TABLE `items_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `items_items_jm_id_864d4159_fk_items_jms_id` (`jm_id`),
  ADD KEY `items_items_vat_id_3db0214e_fk_items_vats_id` (`vat_id`);

--
-- Indexes for table `items_jms`
--
ALTER TABLE `items_jms`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `items_vats`
--
ALTER TABLE `items_vats`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myfirm_firmdata`
--
ALTER TABLE `myfirm_firmdata`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;
--
-- AUTO_INCREMENT dla tabeli `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT dla tabeli `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT dla tabeli `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT dla tabeli `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT dla tabeli `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT dla tabeli `invoices_invoices`
--
ALTER TABLE `invoices_invoices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT dla tabeli `invoices_invoicesitems`
--
ALTER TABLE `invoices_invoicesitems`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
--
-- AUTO_INCREMENT dla tabeli `items_items`
--
ALTER TABLE `items_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
--
-- AUTO_INCREMENT dla tabeli `items_jms`
--
ALTER TABLE `items_jms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT dla tabeli `items_vats`
--
ALTER TABLE `items_vats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT dla tabeli `myfirm_firmdata`
--
ALTER TABLE `myfirm_firmdata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ograniczenia dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ograniczenia dla tabeli `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ograniczenia dla tabeli `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ograniczenia dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ograniczenia dla tabeli `invoices_invoices`
--
ALTER TABLE `invoices_invoices`
  ADD CONSTRAINT `invoices_invoices_customer_id_143e6705_fk_myfirm_firmdata_id` FOREIGN KEY (`customer_id`) REFERENCES `myfirm_firmdata` (`id`);

--
-- Ograniczenia dla tabeli `invoices_invoicesitems`
--
ALTER TABLE `invoices_invoicesitems`
  ADD CONSTRAINT `invoices_invoicesite_invoice_id_55c98b5f_fk_invoices_` FOREIGN KEY (`invoice_id`) REFERENCES `invoices_invoices` (`id`),
  ADD CONSTRAINT `invoices_invoicesitems_items_id_51634ca0_fk_items_items_id` FOREIGN KEY (`items_id`) REFERENCES `items_items` (`id`);

--
-- Ograniczenia dla tabeli `items_items`
--
ALTER TABLE `items_items`
  ADD CONSTRAINT `items_items_jm_id_864d4159_fk_items_jms_id` FOREIGN KEY (`jm_id`) REFERENCES `items_jms` (`id`),
  ADD CONSTRAINT `items_items_vat_id_3db0214e_fk_items_vats_id` FOREIGN KEY (`vat_id`) REFERENCES `items_vats` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
