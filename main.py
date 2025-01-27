import sys

def backend(insx, titles, descps):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.neighbors import KNeighborsClassifier
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import wordnet
    import nltk

    nltk.download("wordnet")
    nltk.download("omw-1.4")

    def derive(texts):
        lem = WordNetLemmatizer() # this word lemmatizer function just gets the deriviatives of the word using the databases downloaded earlier
        devd = []
        for text in texts:
            words = text.split()
            combined = " ".join(
                lem.lemmatize(word.lower(), pos=wordnet.VERB) + " " + # for verbs
                lem.lemmatize(word.lower(), pos=wordnet.NOUN) # and nouns
                for word in words
            )
            devd.append(combined)
        return devd

    def search(inn):

        derive_descps = derive(descps) # using the derive function

        vec = TfidfVectorizer() # converting the words into numbers/vectors/tokens using an importance algorithm that conisders how many times a word is used, the uniqueness of the word, etc.
        vector_descps = vec.fit_transform(derive_descps) # fitting the vectors to the words

        main_m = KNeighborsClassifier(n_neighbors=1) # modified complex distance formula to find distance between vectors and choose the closest one
        main_m.fit(vector_descps, titles) # assign the vectorized descriptions to the titles


        def search_model(ina):
            d_ina = derive([ina])[0] # derive input nouns and verbs
            ina_vec = vec.transform([d_ina]) # vectorize derived input
            prediction = main_m.predict(ina_vec) # use the distance formula neighbor algorithm to find the closest matching titles based on descriptions
            return prediction[0]

        final = search_model(insx)
        return final

    return search(insx)

stuff = [  # defining 2d array
    
    ["unknown", "qeoruqldnajksnvkxcm"],
    ["cancer", "bald, balding, weight loss, fatigue"],
    ["flu", "fever, headache, body aches, chills, sore throat"],
    ["cold", "runny nose, congestion, sneezing, mild cough"],
    ["migraine", "severe headache, nausea, sensitivity to light"],
    ["diabetes", "frequent urination, increased thirst, fatigue, blurred vision"],
    ["allergy", "sneezing, itchy eyes, runny nose, rash"],
    ["covid-19", "fever, cough, loss of taste or smell, fatigue, shortness of breath"],
    ["pneumonia", "chest pain, shortness of breath, fever, coughing"],
    ["anemia", "fatigue, weakness, pale skin, shortness of breath"],
    ["depression", "fatigue, loss of interest, difficulty concentrating, changes in sleep"],
    ["asthma", "wheezing, shortness of breath, chest tightness, coughing"],
    ["hypertension", "headaches, shortness of breath, nosebleeds, dizziness"]
]


cond = [i[0] for i in stuff] # spllitting the 2d array into the conditions i[0] the first option
symp = [i[1] for i in stuff] # and i[1] the second one with the descriptions for everything



def main():
    try:
        with open('user_input.txt', 'r') as input_file:
            user_input = input_file.readline().strip()

        with open('output.txt', 'w') as output_file:
            oop = backend(user_input, cond, symp)
            output_file.write(oop)

    except Exception as e:
        with open('output.txt', 'w') as output_file:
            output_file.write(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
