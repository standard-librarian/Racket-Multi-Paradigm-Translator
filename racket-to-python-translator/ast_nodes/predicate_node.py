from .ast_node import ASTNode


class PredicateNode(ASTNode):
    def __init__(self, predicate, value):
        self.predicate = predicate
        self.value = value

    def __repr__(self):
        return f"PredicateNode(predicate={self.predicate}, value={self.value})"

    def generate_python_code(self):
        python_predicates = {
            'number?': 'isinstance({}, (int, float))',
            'positive?': 'all_gt({}, 0)',
            'negative?': 'all_lt({}, 0)',
            'zero?': 'all_eq({}, 0)',
            'odd?': 'not(all_eq({} % 2, 0))',
            'even?': 'all_eq({} % 2, 0)',
            'list?': 'isinstance({}, list)',
            'eq?': 'all_eq({}, {})',
            'greater?': 'all_gt({}, {})',
            'less?': 'all_lt({}, {})',
            'greater-equal?': 'all_ge({}, {})',
            'less-equal?': 'all_le({}, {})',
            'string?': 'isinstance({}, str)',
            'boolean?': 'isinstance({}, bool)',
            'null?': '{} is None',
            'symbol?': 'isinstance({}, str) and {}.isidentifier()',
            'pair?': 'isinstance({}, (list, tuple)) and len({}) == 2',
            'char?': 'isinstance({}, str) and len({}) == 1',
            'empty?': 'all_eq({}, [])',
            'not-empty?': 'not(all_eq({}, []))',
            'false?': '{} is False',
            'true?': '{} is True',
            # Add more predicates as needed
        }
        if self.predicate not in python_predicates:
            raise Exception(f"Unsupported predicate: {self.predicate}")

        if self.predicate in {'eq?', 'greater?', 'less?', 'greater-equal?', 'less-equal?', 'symbol-eq?', 'symbol-neq?', 'char-eq?', 'char-neq?'}:
            return python_predicates[self.predicate].format(self.value[0].generate_python_code(), self.value[1].generate_python_code())
        else:
            return python_predicates[self.predicate].format(self.value[0].generate_python_code())
