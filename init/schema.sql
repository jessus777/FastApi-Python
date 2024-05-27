--CREATE DATABASE IF NOT EXISTS test_database;
--
--CREATE TABLE IF NOT EXISTS   `test_database`.`students`
--(
--    id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
--    first_name VARCHAR(20) NOT NULL,
--    last_name VARCHAR(20) NOT NULL,
--    age TINYINT NOT NULL,
--    PRIMARY KEY(id)
--);

-- Parte 1: Crear la base de datos si no existe
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'test_database')
BEGIN
    CREATE DATABASE test_database2;
END
GO

-- Parte 2: Usar la base de datos y crear la tabla si no existe
USE test_database;
GO

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'students') AND type in (N'U'))
BEGIN
    CREATE TABLE students
    (
        id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        age TINYINT NOT NULL,  -- Puedes usar TINYINT en lugar de BIGINT(2) para edades
        PRIMARY KEY (id)
    );
END
GO
