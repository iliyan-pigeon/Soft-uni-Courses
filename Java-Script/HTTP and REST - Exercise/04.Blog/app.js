function attachEvents() {    
    const POSTS_URL = 'http://localhost:3030/jsonstore/blog/posts/';
    const COMMENTS_URL = 'http://localhost:3030/jsonstore/blog/comments/';

    const loadPostsBtn = document.getElementById('btnLoadPosts');
    const selectElement = document.getElementById('posts');

    const viewPostsBtn = document.getElementById('btnViewPost');
    const postDetailsH1 = document.getElementById('post-title');
    const postContentParagraph = document.getElementById('post-body');
    const commentsUlList = document.getElementById('post-comments');

    loadPostsBtn.addEventListener('click', loadPostsHandler);
    viewPostsBtn.addEventListener('click', viewPostsHandler);

    const postBody = {};

    async function loadPostsHandler() {
        try {
            const postsResponse = await fetch(`${POSTS_URL}`);
            const postsData = await postsResponse.json();

            Object.entries(postsData)
            .forEach(([ postId, postData ]) => {
                const option = document.createElement('option');
                option.value = postId;
                option.textContent = postData.title;
                selectElement.appendChild(option);

                postBody[postId] = {
                    'title': postData.title,
                    'body': postData.body
                };
            });

        } catch {
            console.log('Error');
        }
    }

    async function viewPostsHandler() {
        try {
            const postId = selectElement.value;
            const viewCommentsResponse = await fetch(`${COMMENTS_URL}`);
            const viewCommentsData = await viewCommentsResponse.json();
            const filteredComments = Object.values(viewCommentsData)
            .filter((comment) => comment.postId === postId);

            postDetailsH1.textContent = '';
            postContentParagraph.textContent = '';
            commentsUlList.innerHTML = '';

            postDetailsH1.textContent = postBody[postId].title;
            postContentParagraph.textContent = postBody[postId].body;

            filteredComments.forEach((comment) => {
                const li = document.createElement('li');
                li.textContent = comment.text;
                commentsUlList.appendChild(li);
            });

        } catch {
        console.log('Error');
        }
    }
}

attachEvents();