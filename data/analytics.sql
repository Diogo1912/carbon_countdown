CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT UNIQUE NOT NULL,
    session_start DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS Devices (
    device_id INTEGER PRIMARY KEY AUTOINCREMENT,
    browser TEXT NOT NULL,
    os TEXT NOT NULL,
    UNIQUE(browser, os)
);

CREATE TABLE IF NOT EXISTS PageViews (
    pageview_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    device_id INTEGER NOT NULL,
    page TEXT NOT NULL,
    view_time DATETIME NOT NULL,
    load_time REAL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (device_id) REFERENCES Devices(device_id)
);