# Tree-Representation
Regular expression engine involves parsing the regex into a syntax tree and then using that tree to match strings. Let's start by implementing a simple regular expression engine that supports alternation (|), concatenation, repetition (*), and matching individual characters. We'll represent the regex as a syntax tree.
The RegexNode class represents a node in the syntax tree, and the parse_regex function takes a regex string and returns the corresponding syntax tree. The visualize_syntax_tree function helps visualize the tree structure.

Next, you would typically use the syntax tree to implement the matching logic. This involves traversing the tree and comparing it against a given input string.

To create a fully functional engine, you would need to handle more complex constructs, such as character classes, grouping, and capturing groups.
