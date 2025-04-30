

// Select the database to use.
use('alvarocm');

db.getCollection('persons').find({"age":{""$gt":50"}})
