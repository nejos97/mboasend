-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mer 20 Septembre 2017 à 21:26
-- Version du serveur :  10.1.19-MariaDB
-- Version de PHP :  5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `dofBase`
--

--
-- Contenu de la table `users`
--

INSERT INTO `users` (`id`, `email`, `userName`, `password`, `role`, `isLogged`, `isActive`, `token`, `lastLogin`, `dateCreation`) VALUES
(1, 'jonathannenba@gmail.com', 'nejos97', 'abcc27dc97b2fdf224854691f947c87c', 'user', '', '1', 'e27884ceddd48ae1cf3c07f19dc721fe1f24fe90ad217f4fcfffc97a33e2fd4d49eefde8179fa0e4', '2017-08-29 14:08:08', '2017-08-27 17:26:15'),
(2, 'devoffuture@gmail.com', 'yagami', '158e49b395d266a87e7b2df58c7f5131', 'user', '', '1', '1a6d4c0391790a36aa5333b1a9f121dc6f92a12f1f30bf565cd06caa57126aafa70f7429c3c6b2d4', '2017-08-28 23:08:59', '2017-08-27 18:58:11');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
