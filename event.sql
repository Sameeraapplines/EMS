-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 08, 2021 at 04:16 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `event`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `event_name` text NOT NULL,
  `person_name` text NOT NULL,
  `event_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `event_name`, `person_name`, `event_date`) VALUES
(1, 'Birthday', 'Ann', '2021-01-11'),
(2, 'Anniversary', 'Jack', '2021-01-19'),
(3, 'Engagement', 'Rose', '2021-01-22'),
(4, 'Birthday', 'Janaki', '2021-02-17'),
(5, 'Medical checkup', 'Mom', '2021-02-25'),
(6, 'Project meet', 'Manager', '2021-03-07'),
(7, 'Birthday', 'Jack', '2021-03-11'),
(8, 'Birthday', 'Martha', '2021-03-18'),
(9, 'Baby shower', 'Sam', '2021-04-13'),
(10, 'Medical checkup', 'Dad', '2021-04-27'),
(11, 'Birthday', 'Kumari', '2021-05-12'),
(12, 'Anniversary', 'Teja', '2021-05-25'),
(13, 'Anniversary', 'Gayaytri', '2021-06-14'),
(14, 'Project submission', 'Manager', '2021-06-28'),
(15, 'Birthday', 'Thahi', '2021-07-17'),
(16, 'Anniversary', 'Mona', '2021-07-30'),
(17, 'Project review', 'Manager', '2021-08-02'),
(18, 'Bachelors party', 'Sweety', '2021-08-12'),
(19, 'Birthday', 'Ruby', '2021-08-26'),
(20, 'Anniversary', 'Cathy', '2021-09-02'),
(21, 'Medical checkup', 'Dad', '2021-09-17'),
(22, 'Medical checkup', 'Mom', '2021-09-21'),
(23, 'Anniversary', 'Juli', '2021-10-07'),
(24, 'Birthday', 'Helen', '2021-10-20'),
(25, 'Baby shower', 'Eleven', '2021-10-27'),
(26, 'Haldi', 'Sweety', '2021-11-29'),
(27, 'Birthday', 'Mike', '2021-11-30'),
(28, 'Marriage', 'Sweety', '2021-12-01'),
(29, 'Birthday', 'Gary', '2021-12-12'),
(30, 'Anniversary', 'Fin', '2021-12-25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
