window.onload = function () {
    fetch('challenges.json')
        .then(response => response.json())
        .then(data => {
            const challengeList = document.getElementById("challenge-list");
            const challengeCount = document.getElementById("challenge-count");

            // Check if challenges are available
            if (Array.isArray(data.challenges) && data.challenges.length > 0) {
                // Update the challenge count display
                challengeCount.textContent = `Total Write-ups: ${data.challenges.length}`;

                // Loop through challenges and create the list items
                data.challenges.forEach(challenge => {
                    const listItem = document.createElement("div");
                    listItem.classList.add("challenge-frame");

                    const link = document.createElement("a");
                    link.href = `challenges/${challenge}/index.html`; // Correct path
                    link.textContent = challenge.replace(/_/g, ' ');  // Replace underscores with spaces
                    
                    listItem.appendChild(link);
                    challengeList.appendChild(listItem);
                });
            } else {
                challengeCount.textContent = "No challenges found.";
            }
        })
        .catch(error => {
            console.error("Failed to load challenges.json:", error);
            document.getElementById("challenge-count").textContent = "Failed to load challenges.";
        });
};
