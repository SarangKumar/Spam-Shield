
from pymongo import MongoClient

def is_spam(id):
    print("Welcome to pyMongo")
    client = MongoClient("mongodb+srv://<username>:<password>@newcluster.usro4ck.mongodb.net/?retryWrites=true&w=majority")
    print(client)
    db = client['hackattack']
    collection = db['spamlist']

    dictionary = {'Number_of_spams':0,'Input':id}
    collection.insert_one(dictionary)

    my_input = collection.find_one({'Input':id})

    if (my_input):
        print(my_input)
        spam_count = list(my_input.values())[1]
        print("spam_count = ",spam_count)
        spam_count=int(spam_count)+1
        spam_count = int(spam_count)
        #filter = {'email_id':id}
        #newvalues = {'Number_of_spams':spam_count}
        collection.replace_one({'Input':id},
        {
            'Number_of_spams':spam_count,
            'Input':id
            
        })

    
    
    



#is_spam("hi@gmail.com")



