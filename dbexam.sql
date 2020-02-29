
-- create a table
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

-- Then make sure the table is empty by deleting any rows that you previously inserted, 
DELETE FROM Ages;

-- insert these rows and only these rows with the following commands:
INSERT INTO Ages (name, age) VALUES ('Kallin', 19);
INSERT INTO Ages (name, age) VALUES ('Cristina', 18);
INSERT INTO Ages (name, age) VALUES ('Alissa', 34);
INSERT INTO Ages (name, age) VALUES ('Malaika', 40);
INSERT INTO Ages (name, age) VALUES ('Ayan', 35);
INSERT INTO Ages (name, age) VALUES ('Hala', 40);

-- Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X

-- Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.

-- 416C697373613334