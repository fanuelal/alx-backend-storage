-- script that creates a function SafeDiv
--  that divides (and returns) the first by the second number

DELIMITER |
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
DECLARE res FLOAT;
IF b = 0 THEN
 SET res = 0;
ELSE
 SET res = a / b;
END IF;
RETURN res;
END;
|
