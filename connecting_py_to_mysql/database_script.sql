
CREATE DATABASE python_db;

CREATE TABLE Hospital(
	Hospital_id INT UNSIGNED NOT NULL,
    Hospital_Name TEXT NOT NULL,
    Bed_Count INT,
    PRIMARY KEY(Hospital_id)
);

INSERT INTO Hospital(Hospital_id, Hospital_Name, Bed_Count)
VALUES
('1', 'Mayo Clinic', 200),
('2', 'Cleveland Clinic', 400),
('3', 'John Hopkins', 1000),
('4', 'UCLA Medical Center', 1500)

CREATE TABLE Doctor(
	Doctor_Id INT UNSIGNED NOT NULL,
    Doctor_Name TEXT NOT NULL,
    Hospital_Id INT NOT NULL,
    Joining_Date DATE NOT NULL,
    Specialty TEXT NULL,
    Salary INT NULL,
    Experience INT NULL,
    PRIMARY KEY(Doctor_Id)
);

INSERT INTO Doctor(Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Specialty, Salary, Experience)
VALUES
	('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
	('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
	('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
	('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
	('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
	('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
	('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
	('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);
    