-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema appointments_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema appointments_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `appointments_db` DEFAULT CHARACTER SET utf8 ;
USE `appointments_db` ;

-- -----------------------------------------------------
-- Table `appointments_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appointments_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `appointments_db`.`tasks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appointments_db`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tasks_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_tasks_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `appointments_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
