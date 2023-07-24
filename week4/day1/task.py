html_input = "<ul><li>Jabłko</li><li>Gruszka</li><li>Pomarańcza</li></ul>"
result = (
    html_input.removeprefix("<ul>")
    .removesuffix("</ul>")
    .replace("<li>", "")
    .split("</li>")[:-1]
)
print(result)
