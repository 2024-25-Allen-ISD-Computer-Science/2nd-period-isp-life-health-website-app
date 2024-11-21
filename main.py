import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Health Self-Diagnosis Tool")
window.geometry("400x300")  # Adjust the size of the window

# Set a background color
window.configure(bg="#eaf7f9")

# Add a title label
title_label = tk.Label(
    window, 
    text="Welcome to the Health Self-Diagnosis Tool", 
    font=("Helvetica", 14, "bold"),
    bg="#eaf7f9",
    fg="#003366",
    wraplength=350
)
title_label.pack(pady=10)

# Add a label for the symptoms input
label = tk.Label(
    window, 
    text="Enter your symptoms below:", 
    font=("Helvetica", 12),
    bg="#eaf7f9",
    fg="#003366"
)
label.pack(pady=5)

# Add an entry widget for symptoms input
entry = tk.Entry(window, font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry.pack(pady=5)

# Define the backend function (placeholder for the OpenAI API call)
def backend(sym):
    # Here you could integrate the OpenAI API or any other functionality
    return f"Processing symptoms: {sym}"

# Define the function to handle button click
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

# Add a submit button
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



# Run the application
window.mainloop()
