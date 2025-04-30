

// Select the database to use.
use('alvarocm');

db.getCollection('persons').find({},{"_id":0, "first-name":1, "surnames":1});
