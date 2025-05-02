const database="alvarocm";
const collection="personstest"
let person2={"name":"Ana","surname":"Riveiro Coello"};
// Select the database to use.
use('alvarocm');

db.getCollection(collection).drop();
db.getCollection(collection);
db.getCollection(collection).insertOne(
    {"name":"Alejandro Jesús"}
);
db.getCollection(collection).insertOne(person2);
