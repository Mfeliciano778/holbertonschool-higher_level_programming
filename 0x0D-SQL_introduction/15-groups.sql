-- list number of records w/ same score in
-- second table
SELECT score, count(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
