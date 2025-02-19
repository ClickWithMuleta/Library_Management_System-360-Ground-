// secure login authentication

document.getElementById("login-form").onsubmit = async function(event) {
    event.preventDefault();

    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let loginBtn = document.getElementById("login-btn");
    let errorMsg = document.getElementById("error-msg");

    // Show loading state
    loginBtn.innerHTML = "Logging in...";
    loginBtn.disabled = true;

    let response = await fetch("/api/method/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ usr: email, pwd: password })
    });

    let result = await response.json();

    // Reset loading state
    loginBtn.innerHTML = "Login";
    loginBtn.disabled = false;

    if (result.message === "Logged In") {
        window.location.href = "/books";
    } else {
        errorMsg.textContent = "Login failed! Check your credentials.";
        errorMsg.classList.remove("hidden");
    }
};

document.getElementById("login-form").onsubmit = async function(event) {
event.preventDefault();

let email = document.getElementById("email").value;
let password = document.getElementById("password").value;
let loginBtn = document.getElementById("login-btn");
let errorMsg = document.getElementById("error-msg");

// Show loading state
loginBtn.innerHTML = "Logging in...";
loginBtn.disabled = true;

let response = await fetch("/api/method/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ usr: email, pwd: password })
});

let result = await response.json();

// Reset loading state
loginBtn.innerHTML = "Login";
loginBtn.disabled = false;

if (result.message === "Logged In") {
    // Fetch user roles
    let roleResponse = await fetch("/api/method/frappe.auth.get_logged_user");
    let user = await roleResponse.json();

    let roleCheck = await fetch(`/api/resource/User/${user.message}`);
    let userData = await roleCheck.json();

    let roles = userData.data.roles.map(role => role.role);

    // Redirect based on role
    if (roles.includes("Administrator")) {
        window.location.href = "/dashboard/admin_dashboard.html";
    } else if (roles.includes("Librarian")) {
        window.location.href = "/Book";
    } else {
        window.location.href = "/books"; // Default member dashboard
    }
} else {
    errorMsg.textContent = " Login failed! Check your credentials.";
    errorMsg.classList.remove("hidden");
}
};

