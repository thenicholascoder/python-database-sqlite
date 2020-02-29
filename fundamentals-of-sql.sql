CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
)

INSERT INTO Users (name,email) VALUES ('John Doe','john@doe.com')


DELETE FROM Users WHERE email='john@doe.com'

-- where reduces the row
-- set is the manipulation code
UPDATE Users SET name='John' WHERE email='john@doe.com'

-- select from
SELECT * FROM Users WHERE email='john@doe.com'

SELECT * FROM Users ORDER BY name 