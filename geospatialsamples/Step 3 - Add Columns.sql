ALTER TABLE qgpl.person
ADD column WKT varchar(50)
ADD column Geometry qsys2.st_point 
ADD column Distance_From_North numeric(9,2)
ADD column Distance_From_South numeric(9,2)
;