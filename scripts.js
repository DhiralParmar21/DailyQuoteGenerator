// Ensure DOM is fully loaded before executing the scripts
document.addEventListener("DOMContentLoaded", function() {
    
    // Simple form validation for the quote submission form
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function(event) {
            const quoteText = document.querySelector("input[name='text']").value.trim();
            const author = document.querySelector("input[name='author']").value.trim();

            if (!quoteText || !author) {
                event.preventDefault(); // Prevent form submission
                alert("Please fill out both the quote and author fields.");
            }
        });
    }

    // Dynamically update quotes section when filtering
    const filterForm = document.getElementById("filter-form");
    if (filterForm) {
        filterForm.addEventListener("submit", function(event) {
            event.preventDefault();
            const category = document.querySelector("select[name='category']").value;
            const mood = document.querySelector("select[name='mood']").value;
            
            // Example: Send a GET request using fetch API to update the quote section
            fetch(`/filter?category=${category}&mood=${mood}`)
                .then(response => response.json())
                .then(data => {
                    const quoteSection = document.getElementById("filtered-quotes");
                    quoteSection.innerHTML = "";

                    if (data.quotes.length > 0) {
                        const ul = document.createElement("ul");
                        data.quotes.forEach(quote => {
                            const li = document.createElement("li");
                            li.innerHTML = `<blockquote><p>${quote.text}</p><footer>- ${quote.author}</footer></blockquote>`;
                            ul.appendChild(li);
                        });
                        quoteSection.appendChild(ul);
                    } else {
                        quoteSection.innerHTML = "<p>No quotes found for the selected filters.</p>";
                    }
                })
                .catch(error => console.error("Error fetching filtered quotes:", error));
        });
    }
    
});
