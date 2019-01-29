-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 10, 2018 at 06:58 PM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `homomorphic`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbldec`
--

CREATE TABLE IF NOT EXISTS `tbldec` (
  `username` varchar(50) NOT NULL,
  `accno` double NOT NULL,
  `balance` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbldec`
--

INSERT INTO `tbldec` (`username`, `accno`, `balance`) VALUES
('aa', 3, 0),
('nsd', 5, 0),
('mangesh', 1, 0),
('praju', 10, 0),
('nik', 50, 0),
('chuda', 100, 0),
('prajakta', 104, 0),
('nikhi', 500, 0),
('mangesh', 1, 0),
('asd', 1, 0),
('nikhil', 9, 0),
('abc', 55, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tblreg`
--

CREATE TABLE IF NOT EXISTS `tblreg` (
  `username` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `acno` double NOT NULL,
  `balance` double NOT NULL,
  `p` int(11) NOT NULL,
  `q` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblreg`
--

INSERT INTO `tblreg` (`username`, `fname`, `lname`, `password`, `email`, `gender`, `acno`, `balance`, `p`, `q`) VALUES
('mangesh', 'Mangesh', 'Wagle', 'mangesh', 'mangesh@gmail.com', 'Male', 475848436, 49180062, 131, 173),
('asd', 'asd', 'ads', 'asd', 'ads@asd.com', 'Male', 304006699, 1459182022, 199, 223),
('nikhil', 'Nikhil', 'N', '123', 'n@gmail.com', 'Male', 1306876278, 124485723, 149, 251),
('abc', 'abc', 'a', 'abc', 'n@gmail.com', 'Male', 360912160, 8819734, 149, 167);
