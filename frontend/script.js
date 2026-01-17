// -------------------------------
// Navigation between cards
// -------------------------------
function showSection(id) {
  document.querySelectorAll(".card").forEach(card => {
    card.style.display = "none";
  });
  document.getElementById(id).style.display = "block";
}

// -------------------------------
// Submit data to Flask backend
// -------------------------------
function submitData() {
  const math = document.getElementById("math").value;
  const english = document.getElementById("english").value;
  const science = document.getElementById("science").value;
  const failures = document.getElementById("failures").value || 0;

  if (math === "" || english === "" || science === "") {
    alert("Please fill all fields");
    return;
  }

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      math: Number(math),
      english: Number(english),
      science: Number(science),
      failures: Number(failures)
    })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("stream").innerText =
        "Recommended Stream: " + data.recommended_stream;

      document.getElementById("reason").innerText =
        data.reason;

      showSection("result-card");
    })
    .catch(error => {
      alert("Backend not running. Please start Flask server.");
      console.error(error);
    });
}
