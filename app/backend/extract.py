import re

def extract_items(lines):
    items = []

    price_regex = r"([0-9]{2,4})"   # prix typique : 60–500 TWD
    for line in lines:
        match = re.search(price_regex, line)
        if match:
            price = match.group(0)
            name = line.replace(price, "").strip(" .:-")
            items.append({"name": name, "price": price})
    return items
