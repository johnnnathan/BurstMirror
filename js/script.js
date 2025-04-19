window.onload = function () {
    fetch('challenges.json')
        .then(response => response.json())
        .then(data => {
            console.log(data.challenges);  // Check if it logs an array of challenge names

            const challengeList = document.getElementById("challenge-list");

            // Set the base path for the challenges directory (BurstMirror)
            const basePath = '/BurstMirror/';  // This assumes the file is inside the BurstMirror directory
            
            if (Array.isArray(data.challenges) && data.challenges.length > 0) {
                data.challenges.forEach(challenge => {
                    const listItem = document.createElement("li");
                    const link = document.createElement("a");
                    
                    // Update link to include the correct path
                    link.href = `${basePath}challenges/${challenge}/index.html`; // Correct path
                    link.textContent = challenge.replace(/_/g, ' ');  // Replace underscores with spaces
                    listItem.appendChild(link);
                    challengeList.appendChild(listItem);
                });
            } else {
                console.log("No challenges found or invalid format.");
            }
        })
        .catch(error => {
            console.error("Failed to load challenges.json:", error);
        });
};
