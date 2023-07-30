import tkinter as tk
import pyshorteners
from tkinter import messagebox

def shorten_url():
    url = entry.get()
    if url:
        shortener = pyshorteners.Shortener()
        try:
            shortened_url = shortener.tinyurl.short(url)
            result_label.config(text=shortened_url)
        except pyshorteners.exceptions.ShorteningErrorException:
            messagebox.showerror("Error", "Unable to shorten URL. Please try again.")

def copy_to_clipboard():
    shortened_url = result_label.cget("text")
    if shortened_url:
        window.clipboard_clear()
        window.clipboard_append(shortened_url)
        messagebox.showinfo("Success", "Shortened URL copied to clipboard.")

window = tk.Tk()
window.title("URL Shortener")

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

button_shorten = tk.Button(window, text="Shorten", command=shorten_url)
button_shorten.pack(side=tk.LEFT, padx=5)

button_copy = tk.Button(window, text="Copy", command=copy_to_clipboard)
button_copy.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
