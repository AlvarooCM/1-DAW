

// Select the database to use.
use('alvarocm');

// Insert a few documents into the sales collection.
db.getCollection('library').insertMany([
        {
          "title": "TCP/IP Illustrated",
          "author": {
            "surname": "Stevens",
            "name": "W."
          },
          "publisher": "Addison-Wesley",
          "price": 65.95
        },
        {
          "title": "Advan Programming for Unix environment",
          "author": {
            "surname": "Stevens",
            "name": "W."
          },
          "publisher": "Addison-Wesley",
          "price": 65.95
        },
        {
          "title": "Data on the Web",
          "author": [
            {
              "surname": "Abiteboul",
              "name": "Serge"
            },
            {
              "surname": "Buneman",
              "name": "Peter"
            },
            {
              "surname": "Suciu",
              "name": "Dan"
            }
          ],
          "publisher": "Morgan Kaufmann publishers",
          "price": 39.95
        },
        {
          "title": "Economics of Technology for Digital TV",
          "editor": {
            "surname": "Gerbarg",
            "name": "Darcy",
            "membership": "CITI"
          },
          "publisher": "Kluwer Academic publishers",
          "price": 129.95
        }
    ])

db.getCollection('library').find({"author.surname":"Stevens"}, {"title":1});

db.getCollection('library').find({"price":{"$gt":20}});

db.getCollection('library').find({"title":/Web/i});

db.getCollection('library').find({
    $or:[
        {"title":/Web/i},
        {"title":/TV/i}
    ]
});

db.getCollection('library').find({"$gt":[{$strLenCP:"title"}, 20]});

db.getCollection('library').find({"price":{$in: [39.95, 65.95, 80.95]}})