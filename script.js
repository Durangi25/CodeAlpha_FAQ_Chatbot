const chatWindow = document.getElementById("chatWindow");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const suggestionButtons = document.querySelectorAll(".suggestion-btn");

function addMessage(message, sender, matchedQuestion = "", confidence = "") {
    const messageDiv = document.createElement("div");

    if (sender === "user") {
        messageDiv.className = "user-message message";
        messageDiv.textContent = message;
    } else {
        messageDiv.className = "bot-message message";
        messageDiv.innerHTML = `
            <div>${message}</div>
            ${
                matchedQuestion
                ? `<div class="bot-info">Matched FAQ: ${matchedQuestion}<br>Confidence: ${confidence}%</div>`
                : ""
            }
        `;
    }

    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendQuestion() {
    const question = userInput.value.trim();

    if (question === "") {
        addMessage("Please type a question first.", "bot");
        return;
    }

    addMessage(question, "user");
    userInput.value = "";

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        addMessage(data.answer, "bot", data.matched_question, data.confidence);

    } catch (error) {
        addMessage("Something went wrong. Please try again.", "bot");
    }
}

sendBtn.addEventListener("click", sendQuestion);

userInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendQuestion();
    }
});

suggestionButtons.forEach(button => {
    button.addEventListener("click", () => {
        userInput.value = button.textContent;
        sendQuestion();
    });
});