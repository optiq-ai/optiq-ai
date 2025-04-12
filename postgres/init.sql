CREATE TABLE IF NOT EXISTS blocks (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    code TEXT NOT NULL,
    commentary TEXT,
    llm TEXT,
    status TEXT DEFAULT 'draft'
);
