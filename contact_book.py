import tkinter as tk
from tkinter import messagebox

# List to store contacts as tuples (name, phone)
contacts = []

# Function to display contacts in the listbox
def display_contacts(filtered_contacts=None):
    contact_listbox.delete(0, tk.END)  # Clear the current listbox
    to_display = filtered_contacts if filtered_contacts else contacts
    if not to_display:
        messagebox.showinfo("No Contacts", "No contacts available.")
    else:
        for name, phone in to_display:
            contact_listbox.insert(tk.END, f"Name: {name}, Phone: {phone}")

# Function to add a new contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()

    if name and phone:
        contacts.append((name, phone))
        name_entry.delete(0, tk.END)  # Clear entry fields
        phone_entry.delete(0, tk.END)
        display_contacts()
    else:
        messagebox.showerror("Input Error", "Both name and phone number are required.")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        contact_details = contact_listbox.get(selected_contact)
        name = contact_details.split(",")[0].split(":")[1].strip()
        for contact in contacts:
            if contact[0] == name:
                contacts.remove(contact)
                display_contacts()
                return
        messagebox.showerror("Delete Error", "Contact not found.")
    else:
        messagebox.showerror("Selection Error", "Please select a contact to delete.")

# Function to search for a contact
def search_contact():
    query = search_entry.get().strip().lower()
    if query:
        filtered_contacts = [contact for contact in contacts if query in contact[0].lower() or query in contact[1]]
        display_contacts(filtered_contacts)
        if not filtered_contacts:
            messagebox.showinfo("Search Result", "No contact found.")
    else:
        display_contacts()

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Frame for adding contacts
add_contact_frame = tk.Frame(root)
add_contact_frame.pack(pady=10)

name_label = tk.Label(add_contact_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5)
name_entry = tk.Entry(add_contact_frame)
name_entry.grid(row=0, column=1, padx=5)

phone_label = tk.Label(add_contact_frame, text="Phone:")
phone_label.grid(row=1, column=0, padx=5)
phone_entry = tk.Entry(add_contact_frame)
phone_entry.grid(row=1, column=1, padx=5)

add_button = tk.Button(add_contact_frame, text="Add Contact", command=add_contact)
add_button.grid(row=2, columnspan=2, pady=10)

# Search bar
search_label = tk.Label(root, text="Search Contacts:")
search_label.pack(pady=5)
search_entry = tk.Entry(root)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack(pady=5)

# Listbox for displaying contacts
contact_listbox = tk.Listbox(root, width=50, height=10)
contact_listbox.pack(pady=10)

# Buttons for delete and display all
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

# Display all contacts on start
display_contacts()

# Run the application
root.mainloop()