--CREATE DATABASE ANYS
USE ANYS
GO
CREATE TABLE CHILDRENS(ID INT, NAME NVARCHAR(30))
INSERT INTO CHILDRENS VALUES(1, 'AZIZBEK'),(2,'NOSIRBEK')
SELECT * FROM CHILDRENS

insert into CHILDRENS
select 3,'nodirbek'
insert into CHILDRENS
select 4,'nosirbek'

  
select * from childrens where id=1
