﻿select 'The person who travelled the furthest as the crow flies to be here today is ' || Title, Forename, Surname, Distance_From_South as Answer from qgpl.person where Distance_From_South = (select max(Distance_From_South) from qgpl.person);