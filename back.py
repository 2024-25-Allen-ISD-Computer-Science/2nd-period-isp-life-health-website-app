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
    
        main_m = KNeighborsClassifier(n_neighbors=1)
        main_m.fit(vector_descps, titles)
        

        def search_model(ina):
            d_ina = derive([ina])[0] 
            ina_vec = vec.transform([d_ina])
            prediction = main_m.predict(ina_vec)
            return prediction[0]

        final = search_model(insx)
        return final

    return search(insx)
