// Select the database to use.
use('alvarocm');

db.getCollection('bookstore').find({},{"title":1});

db.getCollection('bookstore').find({"price":{"lt":30}});

db.getCollection('bookstore').find({"price":{"lt":30}},{"title":1});

db.getCollection('bookstore').find({"price":{"gt":30}}).sort();

db.getCollection('bookstore').find({"year":{"$gte":2003, "$lte":2004}});





