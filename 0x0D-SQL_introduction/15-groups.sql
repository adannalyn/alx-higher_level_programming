-- list same scores under number
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score;
HAVING COUNT(*) > 1
ORDER BY score, number DESC;
