11;rgb:0000/0000/0000-- list same scores under number
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score;
ORDER BY score, number DESC;
