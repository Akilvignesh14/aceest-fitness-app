import pytest
import tkinter as tk
from app import ACEestApp

def test_app_initialization():
    root = tk.Tk()
    app = ACEestApp(root)
    assert app is not None
    root.destroy()