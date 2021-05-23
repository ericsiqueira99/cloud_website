CREATE TABLE user (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(255),
    password varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE iten (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    image varchar(255),
    description varchar(255),
    price float,
    PRIMARY KEY (id)
);

CREATE TABLE purchases (
    id int NOT NULL AUTO_INCREMENT,
    user_id int,
    iten_name varchar(255),
    quantity int,
    price float,
    PRIMARY KEY (id)
);



