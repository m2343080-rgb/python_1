with open("text.txt", "r" , encoding="utf-8") as file:
    content = file.read()
    print(content)
with open("text.txt", "r" , encoding="utf-8") as file:
        file.write("test")