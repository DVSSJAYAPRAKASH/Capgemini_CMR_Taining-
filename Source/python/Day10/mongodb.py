from pymongo import MongoClient

# Replace the uri string with your MongoDB deployment's connection string.
client = MongoClient("mongodb://localhost:27017/")

# Access a specific database
db = client['mydatabase']

# Access a specific collection
collection = db['mycollection']

# Example: Insert a document into the collection
document = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(document)

print("Connected to MongoDB and inserted a document.")