-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 10, 2021 at 04:10 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs230-pz`
--

-- --------------------------------------------------------

--
-- Table structure for table `korisnik`
--

CREATE TABLE `korisnik` (
  `ID` int(11) NOT NULL,
  `ID_ROLA` int(10) UNSIGNED NOT NULL,
  `ID_RACUNARA` int(10) UNSIGNED NOT NULL,
  `USERNAME` char(50) DEFAULT NULL,
  `PASSWORD` char(50) DEFAULT NULL,
  `UKUPAN_BROJ_MINUTA` int(11) DEFAULT NULL,
  `PREOSTALO_VREME` int(11) DEFAULT NULL,
  `ime_slike` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `korisnik`
--

INSERT INTO `korisnik` (`ID`, `ID_ROLA`, `ID_RACUNARA`, `USERNAME`, `PASSWORD`, `UKUPAN_BROJ_MINUTA`, `PREOSTALO_VREME`, `ime_slike`) VALUES
(1, 1, 1, 'admin', 'admin', 999999, 999988, 'slikaa'),
(2, 2, 0, 'user', 'user', 766, 0, NULL),
(74, 2, 0, 'guestt', '123123', 60, 53, 'default.png'),
(78, 2, 0, 'korisnik', '123123', 0, 0, ''),
(85, 2, 0, 'guesttt', '123123', 0, 0, '1default.png'),
(90, 2, 0, 'stefan', '123123', 0, 0, '2default.png');

-- --------------------------------------------------------

--
-- Table structure for table `racunar`
--

CREATE TABLE `racunar` (
  `ID_RACUNARA` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `racunar`
--

INSERT INTO `racunar` (`ID_RACUNARA`) VALUES
(0),
(1),
(2),
(3),
(4),
(5),
(7),
(8),
(9);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `ID_ROLA` int(10) UNSIGNED NOT NULL,
  `NAZIV_ROLE` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`ID_ROLA`, `NAZIV_ROLE`) VALUES
(0, 'Guest'),
(1, 'Admin'),
(2, 'User');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `USERNAME` (`USERNAME`),
  ADD UNIQUE KEY `ime_slike` (`ime_slike`),
  ADD KEY `FK_IMA` (`ID_ROLA`),
  ADD KEY `ID_RACUNARA` (`ID_RACUNARA`) USING BTREE;

--
-- Indexes for table `racunar`
--
ALTER TABLE `racunar`
  ADD PRIMARY KEY (`ID_RACUNARA`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`ID_ROLA`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `korisnik`
--
ALTER TABLE `korisnik`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=91;

--
-- AUTO_INCREMENT for table `racunar`
--
ALTER TABLE `racunar`
  MODIFY `ID_RACUNARA` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD CONSTRAINT `FK_IMA` FOREIGN KEY (`ID_ROLA`) REFERENCES `role` (`ID_ROLA`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_KORISTI` FOREIGN KEY (`ID_RACUNARA`) REFERENCES `racunar` (`ID_RACUNARA`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
