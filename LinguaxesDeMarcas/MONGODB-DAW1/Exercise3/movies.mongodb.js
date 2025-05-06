// Select the database to use.
use('alvarocm');

// db.createCollection('movies');

db.getCollection('movies').find({});

db.getCollection('movies').find({"writer":"J.R.R Tolkien"});

db.getCollection('movies').find({"actors":"Brad Pitt"});

db.getCollection('movies').find({"franchise":"The Lord of the Rings"});

db.getCollection('movies').find({"year":{"$gt":1989,"$lt":2000}});

db.getCollection('movies').find({
    $or:[
        {"year":{"$lt":2000}},
        {"year":{"$gt":2010}}
    ]
})
