CREATE TABLE IF NOT EXISTS settings (
    GuildID INTEGER PRIMARY KEY NOT NULL,
    AdminEnabled INTEGER DEFAULT 0,
    DebugEnabled INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS registrations (
    DUID INT PRIMARY KEY,
    Handle VARCHAR(50) NOT NULL,
    Avatar_URL VARCHAR(250) NOT NULL,
    RegDate DATE,
    SteamFC INT
);

CREATE TABLE IF NOT EXISTS managers (
    DUID INT PRIMARY KEY
);