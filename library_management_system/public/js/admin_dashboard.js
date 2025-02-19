document.addEventListener("DOMContentLoaded", function () {
    fetchDashboardStats();
    renderLoanChart();
});

// Fetch Dashboard Data from API
function fetchDashboardStats() {
    fetch('/api/method/library_management_system.library_management_system.api.get_dashboard_stats')
        .then(response => response.json())
        .then(data => {
            document.getElementById("totalBooks").innerText = data.total_books;
            document.getElementById("availableBooks").innerText = data.available_books;
            document.getElementById("loanedBooks").innerText = data.loaned_books;
            document.getElementById("activeLoans").innerText = data.active_loans;
        })
        .catch(error => console.error("Error fetching stats:", error));
}

// Render Loan Trends Chart
function renderLoanChart() {
    var ctx = document.getElementById('loanChart').getContext('2d');
    fetch('/api/method/library_management_system.library_management_system.api.get_loan_trends')
        .then(response => response.json())
        .then(data => {
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.dates,
                    datasets: [{
                        label: 'Loans Over Time',
                        data: data.counts,
                        borderColor: 'blue',
                        fill: false
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        })
        .catch(error => console.error("Error fetching chart data:", error));
}
