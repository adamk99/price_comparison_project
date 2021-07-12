BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "books" (
	"bookID"	INTEGER NOT NULL UNIQUE,
	"isbn10"	INTEGER,
	"isbn13"	INTEGER,
	"bookTitle"	TEXT NOT NULL,
	"authorName"	TEXT NOT NULL,
	"publisherName"	TEXT,
	"publishedYear"	INTEGER,
	"genre"	TEXT,
	"edition"	INTEGER,
	"bestSeller"	NUMERIC,
	"bookCover"	BLOB,
	PRIMARY KEY("bookID")
);
CREATE TABLE IF NOT EXISTS "retailers" (
	"retailerID"	INTEGER NOT NULL UNIQUE,
	"retailerName"	TEXT NOT NULL UNIQUE,
	"retailerSite"	TEXT UNIQUE,
	"retailerLogo"	BLOB,
	PRIMARY KEY("retailerID")
);
CREATE TABLE IF NOT EXISTS "price" (
	"bookID"	INTEGER NOT NULL,
	"bookName"	TEXT,
	"priceAma"	INTEGER,
	"priceTar"	INTEGER,
	"priceWal"	INTEGER,
	"priceChg"	INTEGER,
	"priceTfb"	INTEGER,
	PRIMARY KEY("bookID" AUTOINCREMENT)
);
COMMIT;
