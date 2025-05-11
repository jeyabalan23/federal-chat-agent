CREATE TABLE IF NOT EXISTS federal_docs (
    id VARCHAR(64) PRIMARY KEY,
    title TEXT,
    agency TEXT,
    summary TEXT,
    date DATE
);
