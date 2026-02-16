// ===============================
// 🔐 Registration Function
// ===============================
function register() {

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return;
    }

    if (password.length < 8) {
        alert("Password must be at least 8 characters long.");
        return;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
    }

    // Switch to dashboard
    document.getElementById("login-section").style.display = "none";
    document.getElementById("dashboard-section").style.display = "block";
}


// ===============================
// 🔓 Logout Function
// ===============================
function logout() {
    document.getElementById("dashboard-section").style.display = "none";
    document.getElementById("login-section").style.display = "flex";
}


// ===============================
// 🤖 AI Market Feasibility Analyze
// ===============================
function analyze() {

    const business = document.getElementById("business").value;
    const location = document.getElementById("location").value;
    const budget = document.getElementById("budget").value;
    const target = document.getElementById("target")?.value || "";
    const price = document.getElementById("price")?.value || "";

    if (!business || !location || !budget) {
        alert("Please fill required fields.");
        return;
    }

    const resultDiv = document.getElementById("result");
    const outputDiv = document.getElementById("analysis-output");

    resultDiv.style.display = "block";

    // 🔄 Loading State
    outputDiv.innerHTML = `
        <p>Analyzing market using AI...</p>
        <div style="margin-top:10px;">⏳ Generating feasibility insights...</div>
    `;

    // 🔥 Backend API Call
    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            business: business,
            location: location,
            budget: budget,
            target: target,
            price: price
        })
    })
    .then(response => {

        if (!response.ok) {
            throw new Error("Server error");
        }

        return response.json();
    })
    .then(data => {

        outputDiv.innerHTML = `
            <h3>AI Feasibility Report</h3>

            <p><strong>Market Viability Score:</strong> ${data.viability_score}%</p>

            <hr>

            <pre style="white-space: pre-wrap; line-height:1.6;">
${data.report}
            </pre>
        `;
    })
    .catch(error => {
        console.error("Backend Error:", error);
        outputDiv.innerHTML = "⚠ Error connecting to AI backend. Make sure backend is running.";
    });
}
