-- Define schema for healthcare warehouse
CREATE TABLE patients (
    patient_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    gender VARCHAR(10)
);

CREATE TABLE encounters (
    encounter_id VARCHAR(50) PRIMARY KEY,
    patient_id VARCHAR(50),
    encounter_date DATE,
    type VARCHAR(50),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
