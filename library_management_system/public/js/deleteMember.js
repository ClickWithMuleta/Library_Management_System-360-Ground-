document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            let membershipId = this.getAttribute("data-member_id"); // Fetch membership_id

            // Debugging output
            console.log("Deleting Member with ID:", membershipId);

            if (!membershipId) {
                alert("Error: Membership ID is missing. Please try again.");
                return;
            }

            if (confirm(`Are you sure you want to delete member with ID '${membershipId}'? This action cannot be undone.`)) {
                fetch(`/api/method/library_management_system.library_management_system.api.delete_member`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-Frappe-CSRF-Token": frappe.csrf_token || document.cookie.match(/XSRF-TOKEN=([^;]+)/)?.[1]
                    },
                    body: JSON.stringify({ name: membershipId })  // Send membership_id instead of name
                })
                .then(response => response.json())
                .then(data => {
                    console.log("API Response:", data);
                    if (data.message === "Member Deleted Successfully") {
                        alert("Member deleted successfully!");
                        location.reload();
                    } else {
                        alert("Error: " + (data.error || "Failed to delete member."));
                    }
                })
                .catch(error => console.error("Delete request failed", error));
            }
        });
    });
});
