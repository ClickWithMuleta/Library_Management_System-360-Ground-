//  JavaScript to Show Messages -->
document.getElementById("create-member-form").onsubmit = function(event) {
    event.preventDefault(); // Prevent default form submission

    var formData = new FormData(this);

    fetch(this.action, {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        var messageContainer = document.getElementById("message-container");
        messageContainer.innerHTML = "";

        var alertDiv = document.createElement("div");
        alertDiv.className = "alert mt-3";

        if (data.message) {
            alertDiv.classList.add("alert-success");
            alertDiv.innerHTML = "<strong> Member Added Successfully!</strong> ";
        } else if (data.error) {
            alertDiv.classList.add("alert-danger");
            alertDiv.innerHTML = "<strong>Error!</strong> " + data.error;
        } else {
            alertDiv.classList.add("alert-warning");
            alertDiv.innerHTML = "<strong>Warning!</strong> Something unexpected happened.";
        }

        messageContainer.appendChild(alertDiv);

        // Clear the form if success
        if (data.message) {
            document.getElementById("create-member-form").reset();
        }
    })
    .catch(error => {
        var messageContainer = document.getElementById("message-container");
        messageContainer.innerHTML = `<div class="alert alert-danger mt-3"><strong>Error!</strong> Failed to connect to the server.</div>`;
    });
};
