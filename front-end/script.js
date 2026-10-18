const chatbox = document.getElementById("chatbox-input")
const chatboxForm = document.getElementById("chatbox-form")

const messages = document.getElementById("messages")

function appendMessage(message) {
    const p = document.createElement("p")
    p.innerText = message
    messages.append(p)
}

async function handleSubmit(e) {
    // Prevents full page refresh
    e.preventDefault()

    // At this point, the chatbox's input is sent to the messages container and displayed onto the screen.
    appendMessage(chatbox.value)

    // We send the input to the backend (URL which is /chat) 
    const response = await fetch("/chat", {
        method: "POST",
        body: chatbox.value
    })

    // When we get the response, it is also sent to the messages container and displayed on the screen.
    appendMessage(await response.text())

    // This clears the chat input box once the user hits "submit"
    chatbox.value = ""
}

// Listens for form submission and calls "handleSubmit"
chatboxForm.addEventListener("submit", handleSubmit)