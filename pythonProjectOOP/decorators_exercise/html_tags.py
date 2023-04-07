def tags(html_tag):

    def decorator(function):

        def wrapped(*args):
            return f"<{html_tag}>{function(*args)}</{html_tag}>"

        return wrapped

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))