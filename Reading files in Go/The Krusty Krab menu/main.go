package main

import (
    "fmt"
    "io/ioutil"
    "log"
)

func main() {
    file, err := ? // open the file here with the ioutil.ReadFile() function
    if err != nil {
        log.Fatal(err) // exit if we have an unexpected error
    }
    // print the contents of the file here as a string
}