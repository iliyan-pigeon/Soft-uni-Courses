article_title = input()
article_content = input()
print(f"<h1>\n    {article_title}\n</h1>")
print(f"<article>\n    {article_content}\n</article>")
comment = input()
while comment != "end of comments":
    print(f"<div>\n    {comment}\n</div>")
    comment = input()
