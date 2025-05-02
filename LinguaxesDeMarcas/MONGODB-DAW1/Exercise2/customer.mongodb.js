
// Select the database to use.
use('alvarocm');

db.getCollection('transactions').drop();

db.createCollection('transactions');

db.getCollection('transactions').find({"Name":"Tom"});

db.getCollection('transactions').find({"Payment.Total":{"$eq":400}});

db.getCollection('transactions').find({"Transaction.price":{"$gt":400}});

db.getCollection('transactions').find({
    $or: [
        {"Note": null},
        {"Note":{$exists: false}}
    ]})


