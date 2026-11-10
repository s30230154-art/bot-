-- SQL script to create tbl_staff table
CREATE TABLE IF NOT EXISTS tbl_staff (
    staff_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(10),
    position VARCHAR(50),
    department VARCHAR(50),
    salary NUMERIC(12, 2) DEFAULT 0.00,
    phone VARCHAR(20),
    email VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE
);
