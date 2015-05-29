

def strip_html(html):
    tag = False
    quote = False
    stripped_html = ''

    for character in html:
        if character == '<' and not quote:
            tag = True
        elif character == '>' and not quote:
            tag = False
        elif character == '"' or character == "'" and tag:
            quote = not quote
        elif not tag:
            stripped_html += character
    return stripped_html

print(strip_html('"<b>bold</b>"'))
