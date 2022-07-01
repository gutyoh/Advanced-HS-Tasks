package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

const dbFile = "chinook.db"

func main() {
	// DO NOT delete this code block! It creates the database object:
	db, err := sql.Open("sqlite3", dbFile)
	if err != nil {
		log.Fatal()
	}
	defer db.Close()

	// DO NOT delete -- these variables are required to read the data from the DB:
	var GenreId int
	var Name string

	// Write the SELECT query to fetch all rows from the 'genres' table:
	?, err := db.Query("?")
	if err != nil {
		log.Fatal()
	}
	defer rows.Close()

	// Iterate over the rows:
	for ?.Next() {
		// Read the columns in each row into the variables:
		err := ?.Scan(&?, &?)
		if err != nil {
			log.Fatal()
		}
		fmt.Println(GenreId, Name)
	}

	// Check for errors after iterating over the rows
	if ? = ?.Err(); ? != nil {
		log.Fatal()
	}
}
