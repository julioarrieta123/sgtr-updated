-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-07-2023 a las 16:56:10
-- Versión del servidor: 10.1.34-MariaDB
-- Versión de PHP: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistemproa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin1`
--

CREATE TABLE `admin1` (
  `id_admin` int(11) NOT NULL,
  `Usuario` varchar(50) NOT NULL,
  `Mail` varchar(50) NOT NULL,
  `Contrasena` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `admin1`
--

INSERT INTO `admin1` (`id_admin`, `Usuario`, `Mail`, `Contrasena`) VALUES
(1, '0', '0', '12345'),
(2, '12', '1234', '12345'),
(3, '0', '0', '0'),
(4, '0', '0', '0'),
(5, '0', '0', '0'),
(6, '0', '0', '0'),
(7, 'juuuuuuuulioooo', 'aaa', 'a1'),
(8, 'julio', 'sfcw', 'wcw'),
(9, 'juliooooooooooooo', 'qwe', 'wew'),
(10, 'Noelia Alessandria', 'noe_alessandria@hotmail.com', 'noe111');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulos`
--

CREATE TABLE `articulos` (
  `id_articulos` int(11) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `talle` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `precio` double NOT NULL,
  `tipo_usuario` varchar(50) NOT NULL,
  `tipo_prenda` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `articulos`
--

INSERT INTO `articulos` (`id_articulos`, `marca`, `talle`, `estado`, `precio`, `tipo_usuario`, `tipo_prenda`) VALUES
(1, 'Adidas', '4', 'Nuevo', 30000, 'adulto', 'buzo'),
(2, 'Ardidas', 'XXXL', 'Nuevo', 5, 'Unicornio', 'Buzoide'),
(3, 'Adidas', '4', 'Nuevo', 10000, 'adulto', 'remera');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Numero_Tel` int(23) NOT NULL,
  `Direccion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `Nombre`, `Apellido`, `Numero_Tel`, `Direccion`) VALUES
(1, 'Rocio Alejandra', 'Gaggino', 3564, 'San Luis 165'),
(2, 'Ariel Nicolas', 'Ladner', 3564, 'Avenida queti porta'),
(3, 'cr', '3ct34t', 3564, 'efcet5q'),
(4, 'Jordi', 'ENP', 2147483647, 'madrid'),
(5, 'Noelia Alessandria', 'Alessandria', 324525, '442345');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `stock`
--

CREATE TABLE `stock` (
  `id_articulo` int(11) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `talle` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `precio` decimal(50,0) NOT NULL,
  `tipo_usuario` varchar(50) NOT NULL,
  `tipo_prenda` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id_ventas` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `prendas_compradas` int(255) NOT NULL,
  `metedo_pago` varchar(50) NOT NULL,
  `cuotas` varchar(50) NOT NULL,
  `total` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id_ventas`, `nombre`, `apellido`, `prendas_compradas`, `metedo_pago`, `cuotas`, `total`) VALUES
(1, 'Julio', 'Arrieta', 2, 'Efectivo', '1 cuota', 20000),
(2, 'Ariel', 'Ladner', 4, 'Tarjeta', '6 cuotas', 30000),
(3, 'Noelia de Lourdes', 'Alessandria', 3, 'Tarjeta', '3 cuotas', 120000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `admin1`
--
ALTER TABLE `admin1`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indices de la tabla `articulos`
--
ALTER TABLE `articulos`
  ADD PRIMARY KEY (`id_articulos`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`id_articulo`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id_ventas`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `admin1`
--
ALTER TABLE `admin1`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `articulos`
--
ALTER TABLE `articulos`
  MODIFY `id_articulos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `stock`
--
ALTER TABLE `stock`
  MODIFY `id_articulo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id_ventas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
