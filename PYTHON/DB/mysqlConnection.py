import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

def get_connection():  # for connection to mysql
    try:
        return mysql.connector.connect(
            host='127.0.0.1',
            user='student',
            password='Student@123',
            database='test_db'  
        )
    except Error as e:
        messagebox.showerror("Connection Error", f"Failed to connect to database: {str(e)}")
        raise  # Re-raise to stop execution if connection fails

def fetch_contacts():  # fetch existing data
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, name, email, phone FROM contacts ORDER BY id")  # retrieve data from table
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Error as e:
        messagebox.showerror("Database Error", str(e))
        return []

def add_contact(name, email, phone):  # add contact
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)",
                    (name, email, phone))  # insert Record in table
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Error as e:
        messagebox.showerror("Database Error", str(e))
        return False

def update_contact(contact_id, name, email, phone):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE contacts SET name=%s, email=%s, phone=%s WHERE id=%s", (name, email, phone, contact_id))  # update record
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Error as e:
        messagebox.showerror("Database Error", str(e))
        return False

def delete_contact(contact_id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))  # delete record from table
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Error as e:
        messagebox.showerror("Database Error", str(e))
        return False

class ContactsApp:
    def __init__(self, root):
        self.root = root
        root.title("Contacts Manager - MySQL + Tkinter")
        # Form
        frm = tk.Frame(root, padx=10, pady=10)
        frm.pack(fill=tk.X)
        tk.Label(frm, text="Name").grid(row=0, column=0, sticky=tk.W)
        self.name_var = tk.StringVar()
        tk.Entry(frm, textvariable=self.name_var, width=30).grid(row=0, column=1, padx=5)
        tk.Label(frm, text="Email").grid(row=1, column=0, sticky=tk.W)
        self.email_var = tk.StringVar()
        tk.Entry(frm, textvariable=self.email_var, width=30).grid(row=1, column=1, padx=5)
        tk.Label(frm, text="Phone").grid(row=2, column=0, sticky=tk.W)
        self.phone_var = tk.StringVar()
        tk.Entry(frm, textvariable=self.phone_var, width=30).grid(row=2, column=1, padx=5)
        # Buttons
        btn_frame = tk.Frame(root, pady=5)
        btn_frame.pack(fill=tk.X)
        tk.Button(btn_frame, text="Add", command=self.add).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Update", command=self.update).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Refresh", command=self.load_contacts).pack(side=tk.RIGHT, padx=5)
        # Treeview (table)
        self.tree = ttk.Treeview(root, columns=("id", "name", "email", "phone"), show='headings')
        self.tree.heading("id", text="ID")
        self.tree.column("id", width=40, anchor=tk.CENTER)
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("phone", text="Phone")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.load_contacts()

    def load_contacts(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        rows = fetch_contacts()
        print(f"Debug: Fetched {len(rows)} rows from database.")  # Debug print
        for row in rows:
            print(f"Debug: Processing row: {row}")  # Debug print
            try:
                self.tree.insert("", tk.END, values=(row['id'], row['name'], row['email'], row['phone']))
            except KeyError as e:
                print(f"Debug: KeyError in row: {e}, available keys: {list(row.keys())}")  # Debug print
                messagebox.showerror("Data Error", f"Missing key in database row: {e}")

    def on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        item = self.tree.item(sel[0])
        id_, name, email, phone = item['values']
        self.selected_id = id_
        self.name_var.set(name)
        self.email_var.set(email)
        self.phone_var.set(phone)

    def add(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showwarning("Validation", "Name is required")
            return
        if add_contact(name, self.email_var.get().strip(), self.phone_var.get().strip()):
            messagebox.showinfo("Success", "Contact added")
            self.clear_form()
            self.load_contacts()

    def update(self):
        if not hasattr(self, 'selected_id'):
            messagebox.showwarning("Selection", "Select a contact to update")
            return
        if update_contact(self.selected_id, self.name_var.get().strip(), self.email_var.get().strip(), self.phone_var.get().strip()):
            messagebox.showinfo("Success", "Contact updated")
            self.clear_form()
            self.load_contacts()

    def delete(self):
        if not hasattr(self, 'selected_id'):
            messagebox.showwarning("Selection", "Select a contact to delete")
            return
        if messagebox.askyesno("Confirm", "Delete selected contact?"):
            if delete_contact(self.selected_id):
                messagebox.showinfo("Success", "Contact deleted")
                self.clear_form()
                self.load_contacts()

    def clear_form(self):
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        if hasattr(self, 'selected_id'):
            delattr(self, 'selected_id')

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactsApp(root)
    root.geometry("600x400")
    root.mainloop()