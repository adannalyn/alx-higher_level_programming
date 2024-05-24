-- list same scores under number
SELECT count(score) AS number
GROUP BY score, number;
