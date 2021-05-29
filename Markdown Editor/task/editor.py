class Formater():
    def __init__(self):
        self.output_text = ""
        self.command_box = ("plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list", "new-line")

    def run(self):
        while True:
            print('Choose a formatter:', end='')
            user_input = input()
            if user_input == "!help":
                print("Available formatters: plain bold italic header link inline-code new-line\nSpecial commands: !help !done")
            elif user_input in self.command_box:
                self.format_selecter(user_input)
                print(self.output_text)
            elif user_input == "!done":
                self.save_result()
                return False
            else:
                print("Unknown formatting type or command", end='\n')

    def format_selecter(self, user_input):
        if user_input == "plain":
            self.format_plain()
        elif user_input == "bold":
            self.format_bold()
        elif user_input == "italic":
            self.format_italic()
        elif user_input == "inline-code":
            self.format_inlinecode()
        elif user_input == "link":
            self.format_link()
        elif user_input == "header":
            self.format_header()
        elif user_input == "new-line":
            self.format_newline()
        elif user_input == "ordered-list":
            self.format_orderedlist()
        elif user_input == "unordered-list":
            self.format_unorderedlist()

    def save_result(self):
        with open("output.md", "w+") as f:
            f.write(self.output_text)

    def format_plain(self):
        print("Text:", end=" ")
        text = input()
        self.output_text += text

    def format_bold(self):
        print("Text:", end=" ")
        text = input()
        text = f"**{text}**"
        self.output_text += text

    def format_italic(self):
        print("Text:", end=" ")
        text = input()
        text = f"*{text}*"
        self.output_text += text

    def format_inlinecode(self):
        print("Text:", end=" ")
        text = input()
        text = f"`{text}`"
        self.output_text += text

    def format_link(self):
        print("Label:", end=" ")
        label = input()
        print("URL:", end=" ")
        url = input()
        text = f"[{label}]({url})"
        self.output_text += text

    def format_header(self):
        print("Level:", end=" ")
        level = input()
        if 0 < int(level) < 7:
            print("Text:", end=" ")
            text = input()
            new_text = f"{int(level) * '#'} {text}\n"
            self.output_text += new_text
        else:
            print("The level should be within the range of 1 to 6.")

    def format_newline(self):
        self.output_text += "\n"

    def format_orderedlist(self):
        while True:
            print("Number of rows:", end='')
            rows = int(input())
            if rows > 0:
                cnt = 0
                while cnt < rows:
                    print(f"Row #{cnt+1}:", end="")
                    self.output_text += f"{cnt+1}. {input()}\n"
                    cnt += 1
                return False
            else:
                print("The number of rows should be greater than zero")
                continue

    def format_unorderedlist(self):
        while True:
            print("Number of rows:", end='')
            rows = int(input())
            if rows > 0:
                cnt = 0
                while cnt < rows:
                    print(f"Row #{cnt+1}:", end="")
                    self.output_text += f"* {input()}\n"
                    cnt += 1
                return False
            else:
                print("The number of rows should be greater than zero")
                continue


if __name__ == "__main__":
    test = Formater()
    test.run()
