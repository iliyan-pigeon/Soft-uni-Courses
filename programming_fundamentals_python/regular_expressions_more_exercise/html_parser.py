import re

html_file = input()
title_pattern = r"(?<=<title>).+(?=\<\/title>)"
body_pattern = r"(?<=\<body\>).+(?=\<\/body\>)"
parasites_pattern = r"\<[a-zA-Z\/\=\"\:\.\/\ ]+\>|\\n"
title = re.findall(title_pattern, html_file)
content = re.findall(body_pattern, html_file)
parasites = re.findall(parasites_pattern, content[0])
for parasite in parasites:
    if parasite == "</a>":
        content[0] = content[0].replace(parasite, " ")
    else:
        content[0] = content[0].replace(parasite, "")
print(f"Title: {title[0]}")
print(f"Content: {content[0]}")





