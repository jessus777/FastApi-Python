-- Parte 1: Crear la base de datos si no existe
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'test_database')
BEGIN
    CREATE DATABASE test_database;
END
GO

-- Parte 2: Usar la base de datos
USE test_database;
GO

-- Parte 3: Crear la tabla grimoires si no existe
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'grimoires') AND type in (N'U'))
BEGIN
    CREATE TABLE grimoires
    (
        id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
        name VARCHAR(50) NOT NULL,
        level INT NOT NULL,
        PRIMARY KEY (id)
    );
END
GO

-- Parte 4: Crear la tabla students si no existe
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'students') AND type in (N'U'))
BEGIN
    CREATE TABLE students
    (
        id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        age TINYINT NOT NULL,
        affinity VARCHAR(100) NOT NULL,
        grimoire_id UNIQUEIDENTIFIER,
        PRIMARY KEY (id),
        FOREIGN KEY (grimoire_id) REFERENCES grimoires(id)
    );
END
GO

-- Parte 5: Crear la tabla requests si no existe
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'requests') AND type in (N'U'))
BEGIN
    CREATE TABLE requests
    (
        id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
        student_id UNIQUEIDENTIFIER NOT NULL,
        status VARCHAR(50) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (student_id) REFERENCES students(id)
    );
END
GO
