

// Select the database to use.
use('alvarocm');

db.getCollection('persons').distinct("first-name").sort();

