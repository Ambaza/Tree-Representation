class RegexNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

def parse_regex(regex):
    if not regex:
        return None

    if '|' in regex:
        return RegexNode('alternation', [parse_regex(part) for part in regex.split('|')])
    elif '*' in regex:
        return RegexNode('repetition', parse_regex(regex[:-1]))
    else:
        return RegexNode('character', regex[0])

def visualize_syntax_tree(node, indent=0):
    if node is None:
        return ""

    result = "  " * indent + f"{node.node_type}"
    if node.value is not None:
        result += f" ({node.value})"
    result += "\n"

    for child in node.children:
        result += visualize_syntax_tree(child, indent + 1)

    return result

# Example usage:
regex = 'a|(bc)*'
syntax_tree = parse_regex(regex)
visualization = visualize_syntax_tree(syntax_tree)
print(visualization)
