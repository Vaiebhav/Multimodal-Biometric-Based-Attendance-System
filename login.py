import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import PIL.Image

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1920x1080")
        self.master.title("Login Page")

        # Set up background image
        img = Image.open("image.jpg")
        img = img.resize((1920,1080), Image.ANTIALIAS)
        self.background_img = ImageTk.PhotoImage(img)
        self.background_label = tk.Label(self.master, image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add a heading
        self.heading = tk.Label(self.master, text="LOGIN PAGE", font=("Josefin Sans",70,"bold","underline"), bg="white", fg="black")
        self.heading.grid(row=0, column=0, columnspan=3, padx=0, pady=0)
        self.heading.place(x=720, y=180,anchor="center")

        # Set up login form
        self.username_label = tk.Label(self.master, text="Username:", font=("Arial", 30), fg="Black", bg="White")
        self.username_entry = tk.Entry(self.master, font=("Arial", 30), bg="gainsboro", fg="Black")
        self.password_label = tk.Label(self.master, text="Password:", font=("Arial", 30), fg="Black", bg="White")
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 30), bg="gainsboro", fg="Black")
        self.login_button = tk.Button(self.master, text="Login", font=("Arial", 30), bg="Orange", fg="black", command=self.login)

        # Position the widgets using the grid layout
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        self.login_button.grid(row=2, column=1, padx=10, pady=10)

        # self.login_label.place(relx=0.5, rely=0.2, anchor="center")
        self.username_label.place(relx=0.5, rely=0.4, anchor="center")
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")
        self.password_label.place(relx=0.5, rely=0.55, anchor="center")
        self.password_entry.place(relx=0.5, rely=0.6, anchor="center")
        self.login_button.place(relx=0.5, rely=0.7, anchor="center")

    def login(self):
        # Check if username and password are correct
        if self.username_entry.get() == "admin" and self.password_entry.get() == "password":
            # Display success message and close the window
            tk.messagebox.showinfo("Login Successful", "Welcome Back, Admin!")
            self.master.destroy()
        else:
            # Display error message and clear the password field
            tk.messagebox.showerror("Login Error", "Invalid Username or Password.")
            self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()

       
