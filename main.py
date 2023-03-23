import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import mongodb
import pickle
from csv import writer

def append_to_csv(csvpath, data):
    with open(csvpath, 'a') as appendObj:
        append = writer(appendObj)
        append.writerow(data)

def spam_detector(id, content, consent):
    data = pd.read_csv('static/dataset/spam.csv',encoding="latin-1")
    data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    data['v1']=data['v1'].map({'ham':0, 'spam':1})
    cv=CountVectorizer()
    x=data['v2'] #message is v2
    y=data['v1'] #spam or ham flag is v1
    x=cv.fit_transform(x)

    #CONVERTING DATA INTO TRAIN TAKS FORMAT
    x_train , x_test , y_train ,y_test = train_test_split(x,y,test_size=0.2)

    model=MultinomialNB()
    model.fit(x_train,y_train)
    
    result=model.score(x_test,y_test)
    result*100

    pickle.dump(model,open("spam.pkl","wb"))
    pickle.dump(cv,open("vectorizer.pkl","wb"))

    clf=pickle.load(open("spam.pkl","rb"))

    # code for database
    #if consent == 1:
        #mongodb1.my_insert(id)

    #-----------------------------------------------------



    test_msg=content
    data=[test_msg]
    vect=cv.transform(data).toarray()
    result=model.predict(vect)
    print(result)

    ans = 'spam' if result == [1] else 'ham'
    append_to_csv('./static/dataset/spam.csv', [ans, content,'','',''])


    if result==1:
        if (consent==1):
            mongodb.is_spam(id)
        return 1
    else:
        return 0

def csv_data():
    data = pd.read_csv('static/dataset/spam.csv',encoding="latin-1")
    return data.shape[0]

if __name__ == '__main__':
    print('this is the main function')