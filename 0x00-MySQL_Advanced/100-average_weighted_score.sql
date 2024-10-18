-- This SQL script creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_weighted_score DECIMAL(10, 2);

    -- Calculate the weighted average
    SELECT SUM(c.score * p.weight) / NULLIF(SUM(p.weight), 0) INTO average_weighted_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = average_weighted_score
    WHERE id = user_id;
END$$

DELIMITER ;