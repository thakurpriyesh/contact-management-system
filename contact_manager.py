import tkinter as tk
from tkinter import messagebox

class ContactManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Contact Manager")

        self.contacts = []

        self.add_contact_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack()

        self.view_contacts_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_contacts_button.pack()

        self.edit_contact_button = tk.Button(master, text="Edit Contact", command=self.edit_contact)
        self.edit_contact_button.pack()

        self.delete_contact_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_contact_button.pack()

        self.save_contacts_button = tk.Button(master, text="Save Contacts", command=self.save_contacts)
        self.save_contacts_button.pack()

    def add_contact(self):
        new_contact = tk.Toplevel(self.master)
        new_contact.title("Add Contact")

        name_label = tk.Label(new_contact, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(new_contact)
        self.name_entry.pack()

        phone_label = tk.Label(new_contact, text="Phone:")
        phone_label.pack()
        self.phone_entry = tk.Entry(new_contact)
        self.phone_entry.pack()

        email_label = tk.Label(new_contact, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(new_contact)
        self.email_entry.pack()

        add_button = tk.Button(new_contact, text="Add", command=self.add_new_contact)
        add_button.pack()

    def add_new_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)

        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contact_list = "Contact List:\n"
        for i, contact in enumerate(self.contacts):
            contact_list += f"{i+1}. {contact['name']} - {contact['phone']} - {contact['email']}\n"
        messagebox.showinfo("Contact List", contact_list)

    def edit_contact(self):
        edit_contact_window = tk.Toplevel(self.master)
        edit_contact_window.title("Edit Contact")

        name_label = tk.Label(edit_contact_window, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(edit_contact_window)
        self.name_entry.pack()

        phone_label = tk.Label(edit_contact_window, text="Phone:")
        phone_label.pack()
        self.phone_entry = tk.Entry(edit_contact_window)
        self.phone_entry.pack()

        email_label = tk.Label(edit_contact_window, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(edit_contact_window)
        self.email_entry.pack()

        edit_button = tk.Button(edit_contact_window, text="Edit", command=self.edit_existing_contact)
        edit_button.pack()

    def edit_existing_contact(self):
        name = self.name_entry.get()

        for contact in self.contacts:
            if contact["name"] == name:
                contact["phone"] = self.phone_entry.get()
                contact["email"] = self.email_entry.get()

                messagebox.showinfo("Success", "Contact updated successfully!")
                return

        messagebox.showerror("Error", "Contact not found!")

    def delete_contact(self):
        delete_contact_window = tk.Toplevel(self.master)
        delete_contact_window.title("Delete Contact")

        name_label = tk.Label(delete_contact_window, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(delete_contact_window)
        self.name_entry.pack()

        delete_button = tk.Button(delete_contact_window, text="Delete", command=self.delete_existing_contact)
        delete_button.pack()

    def delete_existing_contact(self):
        name = self.name_entry.get()

        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)

                messagebox.showinfo("Success", "Contact deleted successfully!")
                return

        messagebox.showerror("Error", "Contact not found!")

    def save_contacts(self):
        with open("contacts.txt", "w") as f:
            for contact in self.contacts:
                f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")
        messagebox.showinfo("Success", "Contacts saved to file!")

root = tk.Tk()
my_gui = ContactManagerGUI(root)
root.mainloop()