CREATE DATABASE a24alvarocm_ejemplosalterdrop;
USE a24alvarocm_ejemplosalterdrop;

--> AÑADIR COLUMNA NUEVA

CREATE TABLE tabla_ejemplo(nuevo1 tinyint);

SELECT * FROM tabla_ejemplo;

ALTER TABLE tabla_ejemplo
   ADD nuevo2 tinyint CONSTRAINT valores_validos CHECK (nuevo2>10);

SELECT * FROM tabla_ejemplo;
 
ALTER TABLE tabla_ejemplo
   ADD nuevo3 char(2) CONSTRAINT valor_no  DEFAULT ('NO');

SELECT * FROM tabla_ejemplo;
 
ALTER TABLE tabla_ejemplo
   ADD nuevo4 char(2) CONSTRAINT valor_no4  DEFAULT ('NO') WITH VALUES;

SELECT * FROM tabla_ejemplo;

--> ELIMINAR COLUMNA

ALTER TABLE tabla_ejemplo
    DROP COLUMN nuevo1;

SELECT * FROM tabla_ejemplo;
-- La vuelvo a añadir, fijaros que la añade al final de la tabla

ALTER TABLE tabla_ejemplo
   ADD nuevo1 tinyint ;

select * from tabla_ejemplo;
 
--> AÑADIR UNA RESTRICCION

ALTER TABLE tabla_ejemplo
    ADD CONSTRAINT res1 CHECK (nuevo2 BETWEEN 1 AND 100);

ALTER TABLE tabla_ejemplo WITH NOCHECK
    ADD CONSTRAINT res2 CHECK (nuevo3 > 100);

--> ELIMINAR UNA RESTRICCION

-- Si se definió una restricción UNIQUE y se quiere eliminar

ALTER TABLE tabla_ejemplo
    ADD CONSTRAINT nuevo2_unique UNIQUE (nuevo2);

	select * from tabla_ejemplo

ALTER TABLE tabla_ejemplo
    DROP nuevo2_unique;

--> CAMBIO DE TIPO DE DATOS 

ALTER TABLE Tabla_Ejemplo
    ALTER COLUMN nuevo1 varchar(40);

--> OBSERVACIONES

ALTER TABLE tabla_ejemplo
   ADD nuevo5  INT  CONSTRAINT chequeo                                                          
   CHECK (nuevo5 <100 AND nuevo5 >100);

--> SENTENCIA DROP-ELIMINAR



