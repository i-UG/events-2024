CREATE or replace FUNCTION wkt_from_postcode(postcode VARCHAR(10))
    RETURNS varchar (50)
            
    LANGUAGE SQL
BEGIN
    DECLARE v_wkt varchar (50);
        SELECT wkt 
    INTO v_wkt 
    FROM JSON_TABLE(
                 SYSTOOLS.HTTPGETCLOB(
                         'https://redbournpostcode.azurewebsites.net/api/LatLong?user='|| 
                         systools.urlencode('YOUR_EMAIL','UTF8') || 
                         '&postcode=' ||
                         systools.urlencode(postcode,'UTF8'), null
                 ), '$'
                     COLUMNS ( wkt varchar(50) PATH '$.wkt')
         ) as x;
    RETURN v_wkt; 
END;