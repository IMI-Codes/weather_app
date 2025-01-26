import customtkinter as ctk

# Initialize the customtkinter app
app = ctk.CTk()
app.title("CustomTkinter Button Example")
app.geometry("400x300")


# Define the function to be called when the button is clicked
def on_button_click():
    text_label.configure(text="Button was clicked!")


# Create a button
button = ctk.CTkButton(master=app, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Create a label to display text after the button is clicked
text_label = ctk.CTkLabel(master=app, text="")
text_label.pack(pady=10)

# Run the app
app.mainloop()
