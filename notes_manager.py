# ------------------------------------------------------
# Copyright (c) 2026 Antonis Koukoumelas. All rights reserved.
# Αυτό το project δημιουργήθηκε από Antonis Koukoumelas.
# ------------------------------------------------------

# notes_manager.py
from flask import Flask, request, render_template_string

app = Flask(__name__)
NOTES_FILE = "notes.txt"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        for note in notes:
            f.write(note + "\n")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Notes Manager</title>
</head>
<body>
    <h1>Notes Manager</h1>
    <form method="POST">
        <input type="text" name="note" placeholder="Add new note" required>
        <button type="submit">Add</button>
    </form>
    <h2>My Notes:</h2>
    <ul>
        {% for note in notes %}
        <li>{{ note }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    notes = load_notes()
    if request.method == "POST":
        new_note = request.form["note"]
        notes.append(new_note)
        save_notes(notes)
    return render_template_string(HTML, notes=notes)

if __name__ == "__main__":
    app.run(debug=True)
