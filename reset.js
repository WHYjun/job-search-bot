/**
* File reset.js
* Script for resetting the database so that it is ready for a fresh run of 'setup.js'; ALL data will be lost!
* This code is from Data Mechanics at http://datamechanics.org by Andrei Lapets
*/

// Load the configuration file.
var config = JSON.parse(cat("config.json"));

// Drop the repository database.
db = new Mongo().getDB(config.repo.name);
db.dropDatabase();

/* eof */