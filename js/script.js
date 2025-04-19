
window.onload = function() {
    // Fetch the list of challenge directories dynamically
    fetch('/challenges.json')
        .then(response => response.json())
        .then(data => {
            const challengeList = document.getElementById("challenge-list");

            // Loop through each challenge and create a list item
            data.challenges.forEach(challenge => {
                const listItem = document.createElement("li");
                const link = document.createElement("a");
                link.href = `/_challenges/${challenge}/index.html`; // Link to the challenge page
                link.textContent = challenge.replace(/_/g, ' '); // Display challenge name
                listItem.appendChild(link);
                challengeList.appendChild(listItem);
            });
        });
};
