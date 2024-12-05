import tkinter as tk

# making the window
window = tk.Tk()
window.title("health thing")
window.geometry("400x300")  # make the window with 400 x 300 res

window.configure(bg="#eaf7f9") # bg color

# title
title_label = tk.Label(
    window, 
    text="Health Tool!!", 
    font=("Helvetica", 14, "bold"),
    bg="#eaf7f9",
    fg="#003366",
    wraplength=350 # wrapping text in window
)
title_label.pack(pady=10)

# adding a label for input
label = tk.Label(
    window, 
    text="Enter your symptoms below:", 
    font=("Helvetica", 12),
    bg="#eaf7f9",
    fg="#003366"
)
label.pack(pady=5)

# prompt textbox
entry = tk.Entry(window, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry.pack(pady=5)

# this is where our backend function is
def backend(sym):
    # we're gonna do all the machine learning stuff right here
    stuff = [
        ["cancer", "bald, balding, weight loss, fatigue"],
        ["flu", "fever, headache, body aches, chills, sore throat"],
        ["cold", "runny nose, congestion, sneezing, mild cough"],
        ["migraine", "severe headache, nausea, sensitivity to light"],
        ["diabetes", "frequent urination, increased thirst, fatigue, blurred vision"],
        ["allergy", "sneezing, itchy eyes, runny nose, rash"],
        ["covid-19", "fever, cough, loss of taste or smell, fatigue, shortness of breath"],
        ["pneumonia", "chest pain, shortness of breath, fever, coughing"],
        ["anemia", "fatigue, weakness, pale skin, shortness of breath"],
        ["depression", "fatigue, loss of interest, difficulty concentrating, changes in sleep"]
        
    ]

    cond_cond = [i[0] for i in stuff] # this is all of the first values in each array, so all the conditions/diseases
    symp = [i[1] for i in stuff] # this is all of the second values in each array, so all the symptoms

    from sklearn.feature_extraction.text import TfidfVectorizer # alright so this uses a vectorizer which basically converts words into tokens or numbers based on the amount of times the word is used and the relative importance of a word (using something called tf-idf, the amount of times a word is used - a how common/rare a word is in a collection of data, the data in this case being the 2 dimensional array: "stuff")
    from sklearn.neighbors import KNeighborsClassifier # okay, so we know that each word is a token, so what this basically is is distance formula. it calculates the distance from the tokens and finds the closest matches.
    import numpy as np # for better/more optimized arrays and data structs

    v_thing = TfidfVectorizer() # assigning the vectorizer function (defined earlier) to a variable
    TRANS_SYMP = v_thing.fit_transform(symp) # assigns importance to the words using tf-idf and converts the words into numbers/vectors

    main_m = KNeighborsClassifier(n_neighbors=1) # assigns the k neighbor function (defined earlier) with k = 1 so it'll choose the one closest distance
    main_m.fit(TRANS_SYMP, cond_cond) # training the model to match the vectors from TRANS_SYMP to the conditions from the i[1] from the 2d array "stuff"

    def cond_check(user_input):
        user_input_to_vector = v_thing.transform([user_input]) # vectorize this too
        prediction = main_m.predict(user_input_to_vector) # k = 1 so this chooses the one best fitting choice from the cond_cond array or i[0] in 2d array "stuff"
        return prediction[0] # returns the #1 prediction!! if it can't match anything, it will choose the first item in cond_cond, so we have to make sure that that's set accordingly

    cond = cond_check(sym)
    return cond

# return the text from backend into a label thing
def get_text():
    text = entry.get()
    processed_text = backend(text)
    label2 = tk.Label(
        window, 
        text=processed_text, 
        font=("Helvetica", 10), 
        bg="#eaf7f9",
        fg="#003366",
        wraplength=350
    )
    label2.pack(pady=10)

# submit button
button = tk.Button(
    window, 
    text="Submit", 
    font=("Helvetica", 12, "bold"), 
    bg="#006699", 
    fg="white", 
    activebackground="#005580",
    activeforeground="white",
    relief="raised",
    command=get_text
)
button.pack(pady=10)



# actually run the application here
window.mainloop()
