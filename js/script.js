window.onload = function () {
    fetch('BurstMirror/challenges.json')  // Try the relative path first
        .then(response => {
            if (!response.ok) {
                throw new Error('Relative path failed, trying absolute path...');
            }
            return response.json();
        })
        .then(data => {
            console.log(data.challenges);  // Log the challenges array

            const challengeList = document.getElementById("challenge-list");
            
            if (Array.isArray(data.challenges) && data.challenges.length > 0) {
                data.challenges.forEach(challenge => {
                    const listItem = document.createElement("li");
                    const link = document.createElement("a");
                    link.href = `/challenges/${challenge}/index.html`;  // Path to the challenge page
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
            // Fallback to absolute path if relative path fails
            fetch('https://johnnnathan.github.io/BurstMirror/challenges.json')  // Absolute path
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Absolute path also failed');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data.challenges);

                    const challengeList = document.getElementById("challenge-list");

                    if (Array.isArray(data.challenges) && data.challenges.length > 0) {
                        data.challenges.forEach(challenge => {
                            const listItem = document.createElement("li");
                            const link = document.createElement("a");
                            link.href = `/challenges/${challenge}/index.html`;  // Path to the challenge page
                            link.textContent = challenge.replace(/_/g, ' ');  // Replace underscores with spaces
                            listItem.appendChild(link);
                            challengeList.appendChild(listItem);
                        });
                    } else {
                        console.log("No challenges found or invalid format.");
                    }
                })
                .catch(error => {
                    console.error("Both relative and absolute fetch failed:", error);
                });
        });
};
