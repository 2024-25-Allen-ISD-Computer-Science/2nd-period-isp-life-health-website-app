import tkinter as tk
import back

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
    return back.backend(sym)

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
