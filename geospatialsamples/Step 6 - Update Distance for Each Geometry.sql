create or replace variable v_NortonPoint QSYS2.ST_Point;  
create or replace variable v_YorkRdPoint QSYS2.ST_Point;
 
set v_NortonPoint = QSYS2.ST_Point('POINT (-2.175518 53.580182)');
set v_YorkRdPoint = QSYS2.ST_Point('POINT (-0.11596 51.50317)');

update qgpl.person set distance_from_north = round ((qsys2.ST_Distance(qgpl.person.geometry, v_NortonPoint)/1609.34),2), 
distance_from_south = round ((qsys2.ST_Distance(qgpl.person.geometry, v_YorkRdPoint)/1609.34),2);

