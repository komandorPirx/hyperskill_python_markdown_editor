formatter = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line"]
LOWEST_LEVEL = 6 
HIGEST_LEVEL = 1 
str_out ='' 
def read_text():
    return input("Text: ")

def bold_format():
   text = read_text()
   return "**" + text + "**"

def italic_format():
    text = read_text()
    return "*" + text + "*"

def header_format():
    level = int(input('Level: '))
    while level > LOWEST_LEVEL or level < HIGEST_LEVEL:
        print("The level should be within the range of 1 to 6")
        level = int(input())
    text = read_text() 
    return  '#' * level +  ' ' + text + '\n'

def plain_format():
    return read_text()

def inline_code_format():
    return '`' + read_text() + '`' 

def new_line_format():
    return '\n'

def link_format():
    label = input("Label: ")
    url   = input("URL: ")
    return '[' + label + ']' + '(' + url + ')' 

def lists(type_list):
    while True:
        num_rows = int(input("Number of rows:"))
        if num_rows <= 0:
            print("The number of rows should be greater than zero")
            continue
        else:
            break
    items = []

    for i in range(1, num_rows + 1, 1):
        item_text = input(f"Row #{i}: ")
        items.append(item_text)

    if type_list == 'ordered-list':
        return '\n'.join([f"{i + 1}. {item}" for i, item in enumerate(items)]) + '\n'
    elif type_list == 'unordered-list':
        return str('\n'.join([f"* {item}" for item in items]) + '\n')
    else:
        return ''



while True:
    input_data = input("Choose a formatter:")
    if input_data == '!help':
        print("""Available formatters: plain bold italic header link inline-code  new-line
                 Special commands: !help !done""")
    elif input_data == 'header':
        str_out += header_format()
        print(str_out)
    elif input_data == 'bold':
        str_out += bold_format()
        print(str_out)
    elif input_data == 'italic':
        str_out += italic_format()
        print(str_out)
    elif input_data == 'plain':
        str_out += plain_format()
        print(str_out)
    elif input_data == 'inline-code':
        str_out += inline_code_format()
        print(str_out)
    elif input_data == 'new-line':
        str_out += new_line_format()
        print(str_out)
    elif input_data == 'link':
        str_out += link_format()
        print(str_out)
    elif input_data == 'ordered-list':
        str_out += lists(input_data)
        print(str_out)
    elif input_data == 'unordered-list':
        str_out += lists(input_data)
        print(str_out)
    elif input_data == '!done':
        with open("output.md", "w") as file_out:
            file_out.write(str_out)
        break
    elif input_data not in formatter:
        print("Unknown formatting type or command")


