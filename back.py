def backend(insx, titles, descps):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.neighbors import KNeighborsClassifier
    from nltk.stem import WordNetLemmatizer 
    from nltk.corpus import wordnet 
    import nltk

    nltk.download("wordnet")
    nltk.download("omw-1.4")

    def derive(texts):
        lem = WordNetLemmatizer()
        devd = []
        for text in texts:
            words = text.split()
            combined = " ".join(
                lem.lemmatize(word.lower(), pos=wordnet.VERB) + " " +
                lem.lemmatize(word.lower(), pos=wordnet.NOUN)
                for word in words
            )
            devd.append(combined)
        return devd

    def search(inn):

        derive_descps = derive(descps)
        
        vec = TfidfVectorizer()
        vector_descps = vec.fit_transform(derive_descps)
    
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
