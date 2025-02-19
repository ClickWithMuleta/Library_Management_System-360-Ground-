// delete book js

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            let bookName = this.getAttribute("data-name");

            if (confirm(`Are you sure you want to delete '${bookName}'? This action cannot be undone.`)) {
                fetch("/api/method/library_management_system.library_management_system.api.delete_book", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-Frappe-CSRF-Token": frappe.csrf_token  //  CSRF Protection
                    },
                    body: JSON.stringify({ name: bookName })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.message === "success") {
                        alert("Book deleted successfully!");
                        location.reload(); // Refresh the page to update the book list
                    } 
                    location.reload(); // Refresh the page to update the book list

                })
                .catch(error => console.error("Delete request failed", error));
            }
        });
    });
});

