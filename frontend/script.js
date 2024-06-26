async function storeNote() {
  const note = document.getElementById("noteInput").value;
  if (!note) {
    alert("Please enter a note.");
    return;
  }

  try {
    clearStoredNote();

    const response = await fetch("http://127.0.0.1:5000/store_note", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ note: note }),
    });

    if (response.ok) {
      const data = await response.json();
      showMessage(data.message);
    } else {
      const errorData = await response.json();
      showMessage(errorData.error || "An error occurred.", true);
    }
  } catch (error) {
    showMessage("Failed to store the note.", true);
  }
}

async function getNote() {
  try {
    const response = await fetch("http://127.0.0.1:5000/get_note");

    if (response.ok) {
      const data = await response.json();
      showStoredNote(data.note);
    } else {
      showStoredNote("Failed to retrieve the note.");
    }
  } catch (error) {
    showStoredNote("Failed to retrieve the note.");
  }
}

function showMessage(message, isError = false) {
  const messageElement = document.getElementById("message");
  messageElement.innerText = message;
  messageElement.className = isError ? "error" : "";
  messageElement.style.display = "block";
}

function showStoredNote(note) {
  const storedNoteContainer = document.getElementById("storedNote");
  storedNoteContainer.innerText = note || "No note stored.";
  storedNoteContainer.style.display = "block";
}

function clearStoredNote() {
  const storedNoteContainer = document.getElementById("storedNote");
  storedNoteContainer.innerText = "";
  storedNoteContainer.style.display = "none";
}
