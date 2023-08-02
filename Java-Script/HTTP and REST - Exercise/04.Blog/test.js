function attachEvents() {
    let btnLoadPosts = document.getElementById("btnLoadPosts")
    let btnViewPost = document.getElementById("btnViewPost")
    let select = document.getElementById("posts")
    let postTitle = document.getElementById("post-title")
    let postBody = document.getElementById("post-body")
    let postComments = document.getElementById("post-comments")
    let postsURL = "http://localhost:3030/jsonstore/blog/posts"
    let commentsURL = "http://localhost:3030/jsonstore/blog/comments"
    btnLoadPosts.addEventListener("click", loadPostsHandler)
    btnViewPost.addEventListener("click", viewPostHandler)
    let postObject = {}

    function loadPostsHandler(){
        fetch(postsURL)
          .then((response) => response.json())
          .then((data) => {
            for (let line in data){
              let option = document.createElement("option")
              option.value = line
              option.textContent = data[line]["title"]
              select.appendChild(option)
              title = data[line]["title"]
              body = data[line]["body"]
              Id = data[line]["id"]
              postObject[Id] = {
                'title': title,
                'body': body
              }
            }
          })
    }

    function viewPostHandler(){
        let postID = select.options[select.selectedIndex].value
        fetch(`${postsURL}/${postID}`)
          .then((response) => response.json())
          .then((data) => {
            title = data["title"]
            body = data["body"]
            postTitle.textContent = title
            postBody.textContent = body
          })
          console.log(postObject);
          
        fetch(commentsURL)
          .then((response) => response.json())
          .then((data) => {
            postComments.innerHTML = ""
            for (let i in postObject){
                if(i === data[line]["postId"]){
                    postTitle.textContent = postObject[i]["title"]
                    postBody.textContent = postObject[i]["body"]
                }
            }
            for (let line in data){
                if (postID === data[line]["postId"]){
                    let liComment = document.createElement("li")
                    liComment.textContent = data[line]["text"]
                    postComments.appendChild(liComment)
                }
            }
          })  
    }
}

attachEvents();