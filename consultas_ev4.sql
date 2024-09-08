CREATE TABLE CompostMachine (
    id INT PRIMARY KEY AUTO_INCREMENT,
    max_capacity DECIMAL(10, 2) NOT NULL,
    composting_time INT NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    material_amount DECIMAL(10, 2) DEFAULT 0
);

CREATE TABLE CompostingTime (
    id INT PRIMARY KEY AUTO_INCREMENT,
    machine_id INT,
    start_time DATETIME,
    end_time DATETIME,
    initial_amount DECIMAL(10, 2),
    FOREIGN KEY (machine_id) REFERENCES CompostMachine(id)
);

INSERT INTO CompostMachine (max_capacity, composting_time) VALUES 
(100, 60),
(150, 90),
(200, 120),
(75, 45),
(125, 75),
(180, 100),
(90, 55),
(110, 65),
(160, 95),
(140, 85);

SELECT id, max_capacity, composting_time
FROM CompostMachine
ORDER BY max_capacity DESC;

SELECT id, max_capacity
FROM CompostMachine
ORDER BY max_capacity DESC
LIMIT 3;

SELECT 
    AVG(max_capacity) as avg_capacity,
    AVG(composting_time) as avg_composting_time
FROM CompostMachine;

SELECT COUNT(*) as machines_on
FROM CompostMachine
WHERE status = TRUE;

SELECT id, max_capacity, material_amount
FROM CompostMachine
WHERE material_amount > (max_capacity * 0.9)
ORDER BY (material_amount / max_capacity) DESC;