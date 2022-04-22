-- script that creates a stored procedure
-- that computes and store the average weighted score for all students.
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS U, 
    (SELECT U.id, SUM(score * weight) / SUM(weight) AS w_avg 
    FROM users AS U 
    JOIN corrections ON U.id=corrections.user_id 
    JOIN projects ON corrections.project_id=projects.id 
    GROUP BY U.id)
  AS weighted
  SET U.average_score = weighted.w_avg 
  WHERE U.id=weighted.id;
END;
|
