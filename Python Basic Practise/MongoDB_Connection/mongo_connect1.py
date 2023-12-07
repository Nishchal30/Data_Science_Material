import pymongo

#create a connection with Mongo DB from below codd

client = pymongo.MongoClient("mongodb+srv://Nishchal30:Nishchal30@cluster0.9omin78.mongodb.net/")
db = client.test
# print(db)



db1 = client['mongotest'] # Here we have created a database called Mongotest
collection = db1['test'] # The tables inside the database called as collections, and we have created one collection as test


# records = collection.find() # we can find all the records from that collection using .find() and we can iterrate on it
# for i in records:
#     print(i)

# If we have to find a records with specific value then use below code

records1 = collection.find({"company" : "ineuron"})

# Query to find a value based on conditions like greater than less than
records2 = collection.find({"marks" : {"$gt" : 75}})
for i in records2:
    # print(i)
    pass

data1 = [
    {
    "student" : "abc",
    "subject" : "maths",
    "marks" : 57,
    },

    {
    "student" : "pqr",
    "subject" : "science",
    "marks" : 86,
    },

    {
    "student" : "xyz",
    "subject" : "history",
    "marks" : 47,
    },

    {
    "student" : "def",
    "subject" : "marathi",
    "marks" : 97,
    }
]

# collection.insert_many(data1)

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]


database = client['inventory']
collection = database['table']
# collection.insert_many(data)

# query to fetch the data where status = A 

records2 = collection.find({"status" : "A"})
for i in records2:
    # print(i)
    pass


# query to fetch the data where status = A or Status = P

records2 = collection.find({"status" : {'$in' : ['A', 'P']}})
for i in records2:
    # print(i)
    pass

# query to fetch the data where status > B
records2 = collection.find({"status" : {"$gt" : "B"}})
for i in records2:
    # print(i)
    pass

# query to fetch the data where quantity >= 75
records2 = collection.find({"qty" : {"$gte" : 75}})
for i in records2:
    # print(i)
    pass

# query to fetch the data where item = sketch pad and quantity = 95
records2 = collection.find({"item" : "sketch pad", "qty" : 95})
for i in records2:
    # print(i)
    pass

# query to fetch the data where item = sketch pad and quantity >= 75
records2 = collection.find({"item" : "sketch pad", "qty": {"$gte" : 75}})
for i in records2:
    # print(i)
    pass

# query to fetch the data where item = sketch pad or quantity >= 75
records2 = collection.find({"$or" : [{"item" : "sketch pad"}, {"qty": {"$gte" : 75}}]})
for i in records2:
    # print(i)
    pass


# query to update the data of the collection
collection.update_one({'item': 'canvas'}, {"$set" : {'item': 'pen'}})
d = collection.find()
for i in d:
    # print(i)
    pass

# query to delete the data of the collection based on condition
collection.delete_one({'item' : "paper"})
d = collection.find()
for i in d:
    print(i)