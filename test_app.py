import pytest
import tkinter as tk
from app import ACEestApp

def test_app_initialization():
    root = tk.Tk()
    # This line tells the window to close itself after 2000ms (2 seconds)
    root.after(2000, root.destroy) 
    app = ACEestApp(root)
    assert app is not None
    root.mainloop() # This starts the app logic