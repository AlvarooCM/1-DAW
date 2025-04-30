

// Select the database to use.
use('alvarocm');

db.getCollection('persons').find();

db.getCollection('persons').find({"first-name":"Francisco"});

