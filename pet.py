import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Base Pet class
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"

# Dog class
class Dog(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.color = color

    def display_info(self):
        return (super().display_info() +
                f", Breed: {self.breed}, Color: {self.color}, "
                f"Care: {pet_preferences['Dog']}")

# Cat class
class Cat(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Cat", age)
        self.breed = breed
        self.color = color

    def display_info(self):
        return (super().display_info() +
                f", Breed: {self.breed}, Color: {self.color}, "
                f"Care: {pet_preferences['Cat']}")

# Pet preferences
pet_preferences = {
    "Dog": ("Bones", "Walk"),
    "Cat": ("Fish", "Nap")
}

# Dictionary to store pets
pets = {}

# Unique ID generator
def generate_pet_id():
    while True:
        pet_id = random.randint(1, 99)
        if pet_id not in pets:
            return pet_id

# GUI Setup
root = tk.Tk()
root.title("Pet Adoption System")
root.geometry("500x500")

# Add Pet
def add_pet():
    species = simpledialog.askstring("Species", "Enter species (Dog/Cat):")
    if not species:
        return
    species = species.capitalize()

    if species not in ["Dog", "Cat"]:
        messagebox.showerror("Error", "Only Dog or Cat allowed.")
        return

    name = simpledialog.askstring("Name", "Enter pet name:")
    age = simpledialog.askinteger("Age", "Enter age:")
    breed = simpledialog.askstring("Breed", "Enter breed:")
    color = simpledialog.askstring("Color", "Enter color:")

    if not all([name, age, breed, color]):
        messagebox.showwarning("Incomplete", "All fields are required.")
        return

    pet_id = generate_pet_id()
    if species == "Dog":
        pet = Dog(name, age, breed, color)
    else:
        pet = Cat(name, age, breed, color)

    pets[pet_id] = pet
    messagebox.showinfo("Success", f"{species} added with ID: {pet_id}")

# View Pets
def view_pets():
    if not pets:
        messagebox.showinfo("No Pets", "No pets available.")
        return

    view_window = tk.Toplevel(root)
    view_window.title("Available Pets")
    view_window.geometry("400x400")

    text = tk.Text(view_window, wrap="word")
    text.pack(expand=True, fill="both")

    for pet_id, pet in pets.items():
        text.insert(tk.END, f"ID: {pet_id} -> {pet.display_info()}\n\n")

# Adopt Pet
def adopt_pet():
    if not pets:
        messagebox.showinfo("No Pets", "No pets to adopt.")
        return

    try:
        pet_id = int(simpledialog.askstring("Adopt Pet", "Enter Pet ID to adopt:"))
    except (TypeError, ValueError):
        return

    if pet_id in pets:
        pet_name = pets[pet_id].name
        del pets[pet_id]
        messagebox.showinfo("Adopted", f"You have adopted {pet_name}!")
    else:
        messagebox.showerror("Error", "Invalid Pet ID")

# Buttons
tk.Label(root, text="Welcome to the Pet Adoption System", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Add Pet", width=20, command=add_pet).pack(pady=10)
tk.Button(root, text="View Pets", width=20, command=view_pets).pack(pady=10)
tk.Button(root, text="Adopt Pet", width=20, command=adopt_pet).pack(pady=10)
tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=20)

root.mainloop()
