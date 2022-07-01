package main

import (
	"fmt"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"log"
)

func main() {
	// Write the required code to connect to "chinook.db"
	db, err := ?.?(?.?(?), &gorm.Config{})
	if err != nil {
		log.Fatal(err)
	}

	// DO NOT delete the line below, it checks if a proper connection was made to "chinook.db"
	fmt.Println(checkConnection(db))
}

::footer
func checkConnection(db *gorm.DB) string {
	sqliteDB, err := db.DB()
	if err != nil {
		log.Fatal(err)
	}
	if sqliteDB.Stats().OpenConnections == 0 {
		log.Fatal("There are no open connections to the database")
	}
	return "Successfully established a connection to chinook.db"
}
