-- setup
-- depends:

CREATE TYPE STATUS AS ENUM('yes', 'no');

-- module
CREATE TABLE IF NOT EXISTS module (
    id INTEGER UNIQUE PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
    name VARCHAR(100) NOT NULL
);

INSERT INTO
    module (id, name)
VALUES (0, 'camera'),
    (1, 'light'),
    (2, 'people');
-----------------------------------

-- Camera Module
CREATE TABLE IF NOT EXISTS camera (
    id SERIAL UNIQUE PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
    module_id INTEGER NOT NULL REFERENCES module (id) DEFAULT 0,
    present_at VARCHAR(100) NOT NULL,
    url VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS camera_activity (
    id SERIAL UNIQUE PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
    camera_id INTEGER NOT NULL REFERENCES camera (id)
);
-----------------------------------

-- Light Module
CREATE TABLE IF NOT EXISTS light (
    id SERIAL UNIQUE PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
    module_id INTEGER NOT NULL REFERENCES module (id) DEFAULT 1,
    camera_id INTEGER REFERENCES camera (id),
    located_at VARCHAR(100) NOT NULL,
    capture_interval INTEGER DEFAULT 60
);

CREATE TABLE IF NOT EXISTS light_activity (
    id SERIAL UNIQUE PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
    captured_at TIMESTAMP WITH TIME ZONE,
    light_id INTEGER NOT NULL REFERENCES light (id),
    switched_on STATUS NOT NULL
);
-----------------------------------

-- People Module
CREATE TABLE IF NOT EXISTS people (
    id SERIAL UNIQUE PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
    module_id INTEGER NOT NULL REFERENCES module (id) DEFAULT 2,
    present_at VARCHAR(100) NOT NULL,
    capture_interval INTEGER DEFAULT 30
);

CREATE TABLE IF NOT EXISTS people_activity (
    id SERIAL UNIQUE PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC'),
    people_id INTEGER NOT NULL REFERENCES people (id),
    no_of_people INTEGER DEFAULT 0
);
-----------------------------------