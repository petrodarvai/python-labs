-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `fablabdb` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `fablabdb` ;

-- -----------------------------------------------------
-- Table `fablabdb`.`equipmentsets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`equipmentsets` (
  `SetID` INT NOT NULL AUTO_INCREMENT,
  `SetName` VARCHAR(100) NOT NULL,
  `Description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`SetID`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`equipmentstatus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`equipmentstatus` (
  `StatusID` INT NOT NULL AUTO_INCREMENT,
  `StatusName` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`StatusID`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`equipmenttypes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`equipmenttypes` (
  `TypeID` INT NOT NULL AUTO_INCREMENT,
  `TypeName` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`TypeID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`equipmentitems`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`equipmentitems` (
  `EquipmentID` INT NOT NULL AUTO_INCREMENT,
  `InventoryNumber` VARCHAR(50) NOT NULL,
  `TypeID` INT NOT NULL,
  `SetID` INT NULL DEFAULT NULL,
  `StatusID` INT NOT NULL,
  PRIMARY KEY (`EquipmentID`),
  UNIQUE INDEX `uniq_inv` (`InventoryNumber` ASC) VISIBLE,
  INDEX `FK_equipmentitems_type` (`TypeID` ASC) VISIBLE,
  INDEX `FK_equipmentitems_set` (`SetID` ASC) VISIBLE,
  INDEX `FK_equipmentitems_status` (`StatusID` ASC) VISIBLE,
  CONSTRAINT `FK_equipmentitems_set`
    FOREIGN KEY (`SetID`)
    REFERENCES `fablabdb`.`equipmentsets` (`SetID`),
  CONSTRAINT `FK_equipmentitems_status`
    FOREIGN KEY (`StatusID`)
    REFERENCES `fablabdb`.`equipmentstatus` (`StatusID`),
  CONSTRAINT `FK_equipmentitems_type`
    FOREIGN KEY (`TypeID`)
    REFERENCES `fablabdb`.`equipmenttypes` (`TypeID`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`labsessions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`labsessions` (
  `SessionID` INT NOT NULL AUTO_INCREMENT,
  `SessionDate` DATE NOT NULL,
  `CourseName` VARCHAR(100) NOT NULL,
  `Instructor` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`SessionID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`projects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`projects` (
  `ProjectID` INT NOT NULL AUTO_INCREMENT,
  `ProjectName` VARCHAR(100) NOT NULL,
  `Description` TEXT NULL DEFAULT NULL,
  `StartDate` DATE NULL DEFAULT NULL,
  `EndDate` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`ProjectID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`students` (
  `StudentID` INT NOT NULL AUTO_INCREMENT,
  `FullName` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(100) NULL DEFAULT NULL,
  `GroupName` VARCHAR(50) NULL DEFAULT NULL,
  `Phone` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`StudentID`),
  UNIQUE INDEX `uniq_email` (`Email` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`lasercutterlog`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`lasercutterlog` (
  `LaserLogID` INT NOT NULL AUTO_INCREMENT,
  `StudentID` INT NOT NULL,
  `ProjectID` INT NULL DEFAULT NULL,
  `StartTime` DATETIME NOT NULL,
  `EndTime` DATETIME NOT NULL,
  `DurationMinutes` INT GENERATED ALWAYS AS (timestampdiff(MINUTE,`StartTime`,`EndTime`)) STORED,
  PRIMARY KEY (`LaserLogID`),
  INDEX `FK_lasercutterlog_student` (`StudentID` ASC) VISIBLE,
  INDEX `FK_lasercutterlog_project` (`ProjectID` ASC) VISIBLE,
  CONSTRAINT `FK_lasercutterlog_project`
    FOREIGN KEY (`ProjectID`)
    REFERENCES `fablabdb`.`projects` (`ProjectID`),
  CONSTRAINT `FK_lasercutterlog_student`
    FOREIGN KEY (`StudentID`)
    REFERENCES `fablabdb`.`students` (`StudentID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`staff` (
  `StaffID` INT NOT NULL AUTO_INCREMENT,
  `FullName` VARCHAR(100) NOT NULL,
  `Role` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`StaffID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`maintenancelog`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`maintenancelog` (
  `MaintenanceID` INT NOT NULL AUTO_INCREMENT,
  `EquipmentID` INT NOT NULL,
  `StaffID` INT NOT NULL,
  `StartDate` DATETIME NOT NULL,
  `EndDate` DATETIME NULL DEFAULT NULL,
  `Description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`MaintenanceID`),
  INDEX `FK_maintenancelog_equipment` (`EquipmentID` ASC) VISIBLE,
  INDEX `FK_maintenancelog_staff` (`StaffID` ASC) VISIBLE,
  CONSTRAINT `FK_maintenancelog_equipment`
    FOREIGN KEY (`EquipmentID`)
    REFERENCES `fablabdb`.`equipmentitems` (`EquipmentID`),
  CONSTRAINT `FK_maintenancelog_staff`
    FOREIGN KEY (`StaffID`)
    REFERENCES `fablabdb`.`staff` (`StaffID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`sessionstudents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`sessionstudents` (
  `SessionID` INT NOT NULL,
  `StudentID` INT NOT NULL,
  PRIMARY KEY (`SessionID`, `StudentID`),
  INDEX `FK_sessionstudents_student` (`StudentID` ASC) VISIBLE,
  CONSTRAINT `FK_sessionstudents_session`
    FOREIGN KEY (`SessionID`)
    REFERENCES `fablabdb`.`labsessions` (`SessionID`),
  CONSTRAINT `FK_sessionstudents_student`
    FOREIGN KEY (`StudentID`)
    REFERENCES `fablabdb`.`students` (`StudentID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`studentprojects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`studentprojects` (
  `StudentID` INT NOT NULL,
  `ProjectID` INT NOT NULL,
  PRIMARY KEY (`StudentID`, `ProjectID`),
  INDEX `FK_studentprojects_project` (`ProjectID` ASC) VISIBLE,
  CONSTRAINT `FK_studentprojects_project`
    FOREIGN KEY (`ProjectID`)
    REFERENCES `fablabdb`.`projects` (`ProjectID`),
  CONSTRAINT `FK_studentprojects_student`
    FOREIGN KEY (`StudentID`)
    REFERENCES `fablabdb`.`students` (`StudentID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fablabdb`.`usagelog`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fablabdb`.`usagelog` (
  `UsageID` INT NOT NULL AUTO_INCREMENT,
  `StudentID` INT NOT NULL,
  `EquipmentID` INT NOT NULL,
  `ProjectID` INT NULL DEFAULT NULL,
  `StaffID` INT NOT NULL,
  `CheckOutTime` DATETIME NOT NULL,
  `ReturnTime` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`UsageID`),
  INDEX `FK_usagelog_student` (`StudentID` ASC) VISIBLE,
  INDEX `FK_usagelog_equipment` (`EquipmentID` ASC) VISIBLE,
  INDEX `FK_usagelog_project` (`ProjectID` ASC) VISIBLE,
  INDEX `FK_usagelog_staff` (`StaffID` ASC) VISIBLE,
  CONSTRAINT `FK_usagelog_equipment`
    FOREIGN KEY (`EquipmentID`)
    REFERENCES `fablabdb`.`equipmentitems` (`EquipmentID`),
  CONSTRAINT `FK_usagelog_project`
    FOREIGN KEY (`ProjectID`)
    REFERENCES `fablabdb`.`projects` (`ProjectID`),
  CONSTRAINT `FK_usagelog_staff`
    FOREIGN KEY (`StaffID`)
    REFERENCES `fablabdb`.`staff` (`StaffID`),
  CONSTRAINT `FK_usagelog_student`
    FOREIGN KEY (`StudentID`)
    REFERENCES `fablabdb`.`students` (`StudentID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
