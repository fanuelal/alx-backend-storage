-- create table name user
-- With these attributes: id,email,name

CREATE TABLE `users` IF NOT EXISTS (
`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
`email` VARCHAR(255) NOT NULL UNIQUE,
`name` VARCHAR(255)
);