
import pymongo

def is_spam(id):
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['hackattack']
    collection = db['spamlist']

    dictionary = {'Number_of_spams':0,'email_id':id}
    collection.insert_one(dictionary)

    email = collection.find_one({'email_id':id})

    if (email):
        print(email)
        spam_count = list(email.values())[1]
        #print("spam_count = ",spam_count)
        spam_count=spam_count+1
        #filter = {'email_id':id}
        #newvalues = {'Number_of_spams':spam_count}
        collection.replace_one({'email_id':id},
        {
            'email_id':id,
            'Number_of_spams':spam_count
        })

    
    
    



#is_spam("hi@gmail.com")



