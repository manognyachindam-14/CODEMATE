def highlight_code(code):
    keywords = ['if', 'else', 'while', 'for', 'def', 'class'] # Example list of keywords

    highlighted_code = ""
    current_word = ""
    in_string = False

    for char in code:
        if char in [' ', '\t', '\n']:
            if in_string:
                current_word += char
            else:
                if current_word in keywords:
                    current_word = f"\033[1m{current_word}\033[0m" # Add bold formatting
                highlighted_code += current_word + char
                current_word = ""
        elif char == '"' or char == "'":
            if in_string:
                current_word += char
                highlighted_code += f"\033[32m{current_word}\033[0m" # Add green color for strings
                current_word = ""
                in_string = False
            else:
                if current_word:
                    if current_word in keywords:
                        current_word = f"\033[1m{current_word}\033[0m" # Add bold formatting for keywords
                    highlighted_code += current_word
                current_word = char
                in_string = True
        else:
            current_word += char

    return highlighted_code


# Example usage
def calculate_sum(a, b):
    return a + b

result = calculate_sum(2, 3)
print(result)

highlighted_code = highlight_code(code)
print(highlighted_code)
