
async function fetchDashboardData() {
    try {
        let booksResponse = await fetch('/api/resource/Book?fields=["name"]');
        let usersResponse = await fetch('/api/resource/User?fields=["name"]');
        let loansResponse = await fetch('/api/resource/Loan?fields=["name", "creation", "book", "user"]');
        let overdueResponse = await fetch('/api/resource/Loan?filters=[["due_date","<",new Date().toISOString().split("T")[0]],["status","=","Loaned"]]');

        let books = await booksResponse.json();
        let users = await usersResponse.json();
        let loans = await loansResponse.json();
        let overdueLoans = await overdueResponse.json();

        document.getElementById("total-books").textContent = books.data.length;
        document.getElementById("total-users").textContent = users.data.length;
        document.getElementById("total-loans").textContent = loans.data.length;
        document.getElementById("overdue-loans").textContent = overdueLoans.data.length;

        let recentLoans = loans.data.slice(0, 5).map(loan => 
            `<tr class="border-t"><td class="p-2">${loan.book}</td><td class="p-2">${loan.user}</td><td class="p-2">${loan.creation.split(" ")[0]}</td></tr>`
        ).join("");
        document.getElementById("recent-loans").innerHTML = recentLoans || `<tr><td colspan="3" class="text-center p-4 text-gray-500">No recent activity</td></tr>`;

    } catch (error) {
        console.error("Error fetching data:", error);
    }
}


function toggleDarkMode() {
    document.body.classList.toggle("bg-gray-900");
    document.body.classList.toggle("text-white");
}

function logout() {
    if (confirm("Are you sure you want to logout?")) {
        window.location.href = "/logout";
    }
}

fetchDashboardData();
renderLoanChart();

