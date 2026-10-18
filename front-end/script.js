const API_URL = "localhost:8000"

const chatbox = document.getElementById("chatbox-input")
const chatboxForm = document.getElementById("chatbox-form")

const messages = document.getElementById("messages")

function handleSubmit(e) {
    e.preventDefault()
    console.log(chatbox.value)
    const paragraph = document.createElement("p")
    paragraph.innerText = chatbox.value
    messages.append(paragraph)
    fetch(API_URL, {
        method: "POST",
        body: chatbox.value
    })
    chatbox.value = ""
}

chatboxForm.addEventListener("submit", handleSubmit)