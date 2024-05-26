import re


def get_tags(content):
    tags = re.findall(r'#(\w+)', content)
    lowercased_tags = []
    for tag in tags:
        tag = re.sub('([a-z0-9])([A-Z])', r'\1-\2', tag).lower()
        lowercased_tags.append(tag)
    return lowercased_tags
