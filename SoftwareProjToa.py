import tkinter as tk
from tkinter import messagebox

class CFGParser:
    def __init__(self, input_str):
        self.tokens = list(input_str.replace(' ', ''))
        self.pos = 0

    def parse(self):
        try:
            node = self.E()
            if self.pos != len(self.tokens):
                raise SyntaxError("Unexpected characters at end")
            return node
        except Exception as e:
            return str(e)

    def E(self):
        node = self.T()
        while self.current_token() in ('+', '-'):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.T()
            node = (op, node, right)
        return node

    def T(self):
        node = self.F()
        while self.current_token() in ('*', '/'):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.F()
            node = (op, node, right)
        return node

    def F(self):
        token = self.current_token()
        if token == '(':
            self.pos += 1
            node = self.E()
            if self.current_token() != ')':
                raise SyntaxError("Missing closing parenthesis")
            self.pos += 1
            return node
        elif token.isalnum():
            self.pos += 1
            return token
        raise SyntaxError(f"Unexpected token: {token}")

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

class CFGParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CFG Parser for Arithmetic Expressions")

        self.label = tk.Label(root, text="Enter arithmetic expression:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        self.parse_button = tk.Button(root, text="Parse", command=self.parse_expression)
        self.parse_button.pack(pady=5)

        self.output = tk.Text(root, width=50, height=15, wrap='word')
        self.output.pack(pady=5)

    def parse_expression(self):
        expression = self.entry.get()
        parser = CFGParser(expression)
        result = parser.parse()
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f"Parse Result:\n{result}")

if __name__ == '__main__':
    root = tk.Tk()
    app = CFGParserGUI(root)
    root.mainloop()
