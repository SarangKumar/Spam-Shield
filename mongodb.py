import pymongo


def get_fields_count():
    # print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    # print(client)
    db = client['hackattack']
    collection = db['spamlist']
    return len(list(collection.find()))

def is_spam(id):
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['hackattack']
    collection = db['spamlist']

    dictionary = {'Number_of_spams':0,'Input':id,'Threat_level':'Low'}
    collection.insert_one(dictionary)

    my_input = collection.find_one({'Input':id})

    collection.delete_many({'Number_of_spams':0})

    if (my_input):
        print("Input: ",my_input)
        spam_count = list(my_input.values())[1]
        print("spam_count = ",spam_count)
        spam_count=int(spam_count)+1
        spam_count = int(spam_count)

        if (spam_count<=5):
            collection.replace_one({'Input':id},
            {
                'Number_of_spams':spam_count,
                'Input':id,
                'Threat_level':'Low'            
            })

        elif (spam_count<=10):
            collection.replace_one({'Input':id},
            {
                'Number_of_spams':spam_count,
                'Input':id,
                'Threat_level':'Medium'
            })

        elif (spam_count>10):
            collection.replace_one({'Input':id},
            {
                'Number_of_spams':spam_count,
                'Input':id,
                'Threat_level':'High'
            })
    
        '''
        collection.replace_one({'Input':id},
        {
            'Number_of_spams':spam_count,
            'Input':id
        })
        '''


print(get_fields_count())