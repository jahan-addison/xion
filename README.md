# xion

![img](docs/xion.png)


## Library

### A Compiler Frontend (Lexer, Parser) for the B Language.

Xion provides a LALR(1) grammar and parser generator (via [Lark](https://github.com/lark-parser/lark)). Check out [language details on the B language](https://www.bell-labs.com/usr/dmr/www/btut.pdf), [and syntax here](https://www.bell-labs.com/usr/dmr/www/kbman.html). You can find a link to my grammar [here](https://github.com/jahan-addison/xion/blob/master/xion/grammar.lark).

This project was primarily created for [roxas](https://github.com/jahan-addison/roxas) as an easy-to-use first-pass frontend.

Xion additionally provides factory methods for the parse tree as an AST with json, strings, and `Lark.tree`:

* `parse_source_program(source_program: str, debug=True) -> Lark.Tree`
* `parse_source_program_as_string(source_program: str, pretty: bool = True, debug=True) -> str`

* `get_source_program_as_ast(source_program: str, meta=False, debug=True) -> AST_Node`
* `get_source_program_ast_as_string(source_program: str, meta=False, debug=True) -> str`
* `get_source_program_ast_as_json(source_program: str, meta=False, debug=True) -> JSON`


Symbol table construction passes are also available as factory methods:
* `get_source_program_symbol_table(source_program: str, debug=True) -> Symbol_Table`
* `get_source_program_symbol_table_as_json(source_program: str, debug=True) -> JSON`


### Details

The AST type is structured as follows:

```python

T = TypeVar('T', bound='AST_Node')
Node = Union[List[T], T]

class _Meta(TypedDict):
    line: Union[int, None]
    type: NotRequired[str]
    column: Union[int, None]
    start_pos: Union[int, None]
    end_pos: Union[int, None]
    end_column: Union[int, None]


class AST_Node(TypedDict):
    """The AST data structure"""
    node: Node_Type
    root: Node_Root
    left: NotRequired[Node]
    right: NotRequired[Node]
    _meta: NotRequired[_Meta]
```

and a Symbol Table which contains idenfitier, function definition, and vector definition lvalues:

```python

Symbol_Table = Dict[str, _Meta]
```

#### Usage Example

```python
from xion import parser
with open(path_to_b_source_program) as file:
    print(parser.get_source_program_ast_as_json(file.read()))
```

## Dependencies

`xion` uses `poetry` for dependency management. Simply run `poetry install` to install dependencies.

## Tests

**Xion has 90% code coverage.** Note that tests of ast nodes are proofs of correction to the grammar.

* Use `make run` to run the parser on the first B program example
* Use `make test` to run the test suite and verify grammar correctness


## License

Apache 2 License.


![img2](docs/axel-roxas-and-xion-looking-to-the-left-in-kingdom-hearts-3.png)