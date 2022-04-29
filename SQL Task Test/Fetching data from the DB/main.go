package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

const dbFile = "chinook.db"

func main() {
	db, err := sql.Open("sqlite3", dbFile)
	if err != nil {
		log.Fatal()
	}
	defer db.Close()

	var GenreId int
	var Name string

	// Write the SELECT query to fetch all rows from the 'genres' table:
	rows, err := db.Query("SELECT * FROM genres")
	if err != nil {
		log.Fatal()
	}
	defer rows.Close()

	// Iterate over the rows:
	for rows.Next() {
		// Read the columns in each row into the variables:
		err := rows.Scan(&GenreId, &Name)
		if err != nil {
			log.Fatal()
		}
		fmt.Println(GenreId, Name)
	}

	// Check for errors after iterating over the rows
	if err = rows.Err(); err != nil {
		log.Fatal()
	}
}
