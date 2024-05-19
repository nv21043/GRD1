function sendMessage() {
    var userInput = document.getElementById("userInput").value;
    if (userInput.trim() === "") return;

    var chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += "<p><strong>You:</strong> " + userInput + "</p>";

    document.getElementById("userInput").value = "";

    // Send message to Flask server
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ data: [userInput] }),
    })
    .then((response) => response.json())
    .then((data) => {
        var botReply = data.predictions[0].indexOf(Math.max(...data.predictions[0]));
        chatbox.innerHTML += "<p><strong>Chatbot:</strong> " + botReply + "</p>";
    })
    .catch((error) => {
        console.error("Error:", error);
    });
}
