window.onload = function () {
    fetch('challenges.json')
        .then(response => response.json())
        .then(data => {
            console.log(data.challenges);  // Check if it logs an array of challenge names

            const challengeList = document.getElementById("challenge-list");

            if (Array.isArray(data.challenges) && data.challenges.length > 0) {
                data.challenges.forEach(challenge => {
                    const challengeFrame = document.createElement("div");
                    challengeFrame.classList.add("challenge-frame");

                    const link = document.createElement("a");
                    link.href = `challenges/${challenge}/index.html`; // Correct path
                    link.textContent = challenge.replace(/_/g, ' ');  // Replace underscores with spaces

                    challengeFrame.appendChild(link);
                    challengeList.appendChild(challengeFrame);
                });
            } else {
                console.log("No challenges found or invalid format.");
            }
        })
        .catch(error => {
            console.error("Failed to load challenges.json:", error);
        });
};
