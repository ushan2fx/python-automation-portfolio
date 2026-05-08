"""
Library Management Tool - Portfolio Project 3
Author: Vajira L. (MLIS)
Description: Simple desktop app for small libraries
"""
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Manager - Vajira")
        self.root.geometry("800x500")
        self.conn = sqlite3.connect('library.db')
        self.create_tables()
        self.setup_ui()
        self.load_books()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, status TEXT DEFAULT "Available", added_date TEXT)')
        self.conn.commit()
    
    def setup_ui(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill='x')
        ttk.Label(frame, text="Title:").grid(row=0, column=0)
        self.title_entry = ttk.Entry(frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5)
        ttk.Label(frame, text="Author:").grid(row=0, column=2)
        self.author_entry = ttk.Entry(frame, width=25)
        self.author_entry.grid(row=0, column=3, padx=5)
        ttk.Button(frame, text="Add Book", command=self.add_book).grid(row=0, column=4, padx=10)
        
        columns = ('ID', 'Title', 'Author', 'Status', 'Added')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)
    
    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        if not title:
            messagebox.showwarning("Error", "Title required")
            return
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO books (title, author, added_date) VALUES (?, ?, ?)", (title, author, datetime.now().strftime("%Y-%m-%d")))
        self.conn.commit()
        self.title_entry.delete(0, 'end')
        self.author_entry.delete(0, 'end')
        self.load_books()
    
    def load_books(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, author, status, added_date FROM books ORDER BY id DESC")
        for row in cursor.fetchall():
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
