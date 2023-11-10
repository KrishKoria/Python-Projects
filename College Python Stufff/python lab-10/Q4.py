import re


def extract_strings_between_tags(html_string, tag):
    pattern = f"<{tag}>(.*?)</{tag}>"

    matches = re.findall(pattern, html_string)

    return matches


# Example input
html_input = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'
tag_to_extract = 'b'

result = extract_strings_between_tags(html_input, tag_to_extract)

print(result)
