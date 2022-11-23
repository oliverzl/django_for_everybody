CREATE TABLE "Users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "name" TEXT, 
    "email" TEXT
);

.tables
.schema Users

INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu')
INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu')
INSERT INTO Users (name, email) VALUES ('Colleen', 'cv@umich.edu')
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu')
INSERT INTO Users (name, email) VALUES ('Sally', 'al@umich.edu')


SELECT * FROM USERS;

SELECT FROM USERS WHERE email='csev@umich.edu;

DELETE FROM Users WHERE email='ted@umich.edu';

DROP TABLE USERS

.quit



$ python manage.py makemigrations: 
making migration scripts for different database 'types'

$ python manage.py migrate
reads migrations and changes the databases


