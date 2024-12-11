from lark import Lark, Tree, Transformer
from typing import Optional
import logging

# Initialize logging for lark.
logging.basicConfig(level=logging.DEBUG)


class Parser:
    """Parser and adapter with lark.

    Build and transform a parse tree for syntax-directed translation of
    a source program. Initializes with the provided LALR(1) lark grammar.

    Args:
        source_program: The source B program.
        transformer: Syntax-directed transformer.
        debug: Debug flag in Lark.
        grammar: Optional alternative LALR(1) grammar that passes to lark.

    Attributes:
        source_program: The source program.
        transformer: Syntax-directed transformer.
        parser: Lark LALR(1) parser instance.
        grammar: LALR(1) grammar that passes to lark.
        tree: Parse tree.

    """
    def __init__(self, source_program: str, transformer=None, debug=True, grammar='xion/grammar.lark') -> None:
        self.source: str = source_program
        self.transformer: Optional[Transformer] = transformer
        self._read_grammar(grammar)
        self.parser = Lark(
            self.grammar,
            start='program',
            parser='lalr',
            transformer=self.transformer,
            debug=True)
        self._tree = self.parser.parse(self.source)

    def __str__(self) -> str:
        """The parse tree as formatted string """
        return self._tree.pretty()

    def get_parse_tree(self) -> Tree:
        """Get the current parse tree.

        Returns:
            The current state of the parse tree.

        """
        return self._tree

    def print_parse_tree(self, pretty=False, file=None) -> None:
        """Print parse tree.

        Print the parse tree to a text stream.

        Args:
            pretty: Print as formatted string
            file: text stream
        """
        if pretty is True:
            print(self._tree.pretty(), file=file)
        else:
            print(self.get_parse_tree(), file=file)

    def _read_grammar(self, location: str) -> None:
        """Read source grammar.

        Read a grammar from location on disk.

        Args:
            grammar: The source LALR(1) grammar.

        """
        with open(location) as file:
            self.grammar = file.read()


def parse_source_program(source_program: str, debug=True) -> Tree:
    """ Get parse tree of B program as serializable tree (Lark.Tree)

    Args:
        source_program: The source B program as a string
        debug: debug flag

    Returns:
        Serializable parse tree

    """
    return Parser(source_program, debug=debug).get_parse_tree()


def parse_source_program_as_string(source_program: str, debug=True) -> str:
    """ Get parse tree of B program as serializable tree (Lark.Tree)

    Args:
        source_program: The source B program as a string
        debug: debug flag

    Returns:
        Parse tree as string

    """
    return parse_source_program(source_program, debug).pretty()
