-- This SQL script creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_weighted_score INT;
    DECLARE total_weight INT;
    
    -- Declare a cursor for iterating over users
    DECLARE user_cursor CURSOR FOR 
        SELECT id FROM users;

    -- Declare a handler for the cursor end
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET user_id = NULL;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        
        -- Exit loop if no more users
        IF user_id IS NULL THEN
            LEAVE read_loop;
        END IF;
        
        -- Calculate the total weighted score for the user
        SELECT SUM(corrections.score * projects.weight) INTO total_weighted_score
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
        
        -- Calculate the total weight for the user
        SELECT SUM(projects.weight) INTO total_weight
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Update the average_score for the user
        IF total_weight = 0 THEN
            UPDATE users SET average_score = 0 WHERE id = user_id;
        ELSE
            UPDATE users SET average_score = total_weighted_score / total_weight WHERE id = user_id;
        END IF;
    END LOOP;

    CLOSE user_cursor;
END $$

DELIMITER ;