-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tech4good
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tech4good
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tech4good` DEFAULT CHARACTER SET utf8 ;
USE `tech4good` ;

-- -----------------------------------------------------
-- Table `PRODUCER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PRODUCER` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NAME` VARCHAR(100) NULL,
  `AGE` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DATE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DATE` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `DATE` DATE NULL,
  `DAY` INT NULL,
  `MONTH` INT NULL,
  `YEAR` INT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ITEM`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ITEM` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NAME` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LOCATION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LOCATION` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `CITY` VARCHAR(100) NULL,
  `UF` VARCHAR(2) NULL,
  `LOCATION` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FACTPRODUCTION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FACTPRODUCTION` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `DATE_ID` INT NOT NULL,
  `ITEM_ID` INT NOT NULL,
  `PRODUCER_ID` INT NOT NULL,
  `LOCATION_ID` INT NOT NULL,
  `QTD_PRODUCT` INT NULL DEFAULT 0,
  `QTD_EXCESS` INT NULL DEFAULT 0,
  PRIMARY KEY (`ID`),
  INDEX `fk_FACT PRODUCTION_DATE_idx` (`DATE_ID` ASC),
  INDEX `fk_FACT PRODUCTION_PRODUCT1_idx` (`ITEM_ID` ASC),
  INDEX `fk_FACT PRODUCTION_PRODUCER1_idx` (`PRODUCER_ID` ASC),
  INDEX `fk_FACT PRODUCTION_LOCATION1_idx` (`LOCATION_ID` ASC),
  CONSTRAINT `fk_FACT PRODUCTION_DATE`
    FOREIGN KEY (`DATE_ID`)
    REFERENCES `DATE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT PRODUCTION_PRODUCT1`
    FOREIGN KEY (`ITEM_ID`)
    REFERENCES `ITEM` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT PRODUCTION_PRODUCER1`
    FOREIGN KEY (`PRODUCER_ID`)
    REFERENCES `PRODUCER` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT PRODUCTION_LOCATION1`
    FOREIGN KEY (`LOCATION_ID`)
    REFERENCES `LOCATION` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;