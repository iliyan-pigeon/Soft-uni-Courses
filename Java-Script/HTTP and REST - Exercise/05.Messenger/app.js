function attachEvents() {
    let textarea = document.getElementById("messages")
    let nameInput = document.querySelector("#controls > div > input[name='author']")
    let contentInput = document.querySelector("#controls > div > input[name='content']")
    let sendButton = document.getElementById("submit")
    let refreshButton = document.getElementById("refresh")
    sendButton.addEventListener("click", sendHandler)
    refreshButton.addEventListener("click", refreshHandler)
    let baseURL = "http://localhost:3030/jsonstore/messenger"

    function sendHandler(){
        let name = nameInput.value
        let content = contentInput.value
        fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify({
                author: name,
                content: content,
            })
        })
          .then((response) => response.json())
          .then((response) => {
            console.log(response);
          })
    }

    function refreshHandler(){
      fetch(baseURL)
        .then((response) => response.json())
        .then((data) => {
            let result = []
            for (let line in data){
              let {author, content} = data[line]
              result.push(`${author}: ${content}`)
            }
            textarea.textContent = result.join("\n")
        })
    }
}

attachEvents();