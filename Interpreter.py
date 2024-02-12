OPERATORS = {'+', '-', '*', '/'}

class AbstractExpression:
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        if self.value in context:
            return context[self.value]
        else:
            return None

class NonTerminalExpression(AbstractExpression):
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret(self, context):
        left_result = self.left_expression.interpret(context)
        right_result = self.right_expression.interpret(context)

        if left_result is not None and right_result is not None:
            return left_result + right_result
        else:
            return None


class Client:
    def __init__(self):
        self.expression_tree = None

    def parse(self, expression):
        self.expression_tree = self.create_expression_tree(expression)

    def evaluate(self):
        return self.expression_tree.interpret({})

    def create_expression_tree(self, expression):
        # Split the expression into tokens
        tokens = expression.split(' ')

        # Create a stack to store the expressions
        stack = []
        # Create a stack to store the operators
        operator_stack = []

        # Operator precedence dictionary
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        # Iterate over the tokens
        for token in tokens:
            if token in OPERATORS:
                # Handle operator precedence
                while operator_stack and precedence[operator_stack[-1]] >= precedence[token]:
                    right_expression = stack.pop()
                    left_expression = stack.pop()
                    operator = operator_stack.pop()
                    binary_expression = NonTerminalExpression(left_expression, right_expression)
                    stack.append(binary_expression)

                operator_stack.append(token)
            else:
                constant_expression = TerminalExpression(token)
                stack.append(constant_expression)

        # Process remaining operators in the stack
        while operator_stack:
            right_expression = stack.pop()
            left_expression = stack.pop()
            operator = operator_stack.pop()
            binary_expression = NonTerminalExpression(left_expression, right_expression)
            stack.append(binary_expression)

        # The expression tree is the top of the stack
        if len(stack) == 1:
            return stack.pop()
        else:
            raise ValueError("Invalid expression: Too many operands.")
        
        
client = Client()
client.parse('1 + 2 * 3')
result = client.evaluate()
print(result)
