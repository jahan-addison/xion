import pytest

@pytest.fixture # type: ignore
def program_example_1_parse_tree() -> str:
  return """Tree(Token('RULE', 'program'), [Tree(Token('RULE', 'definition'), [Tree(Token('RULE', 'function_definition'), [Token('NAME', 'main'), Tree(Token('RULE', 'parameters'), [None]), Tree(Token('RULE', 'block_statement'), [Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'auto_statement'), [Tree('identifier', [Token('NAME', 'j')]), Tree('vector_identifier', [Tree('identifier', [Token('NAME', 's')]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '20')])])])]), Tree('vector_identifier', [Tree('identifier', [Token('NAME', 't')]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '20')])])])]), Token('SEMI_COLON', ';')])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'reread')]), Tree(Token('RULE', 'parameters'), [None])])]), Token('SEMI_COLON', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'getstr')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 's')])])])])])]), Token('SEMI_COLON', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'j')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'getarg')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 't')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 's')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '0')])])])])])])])]), Token('SEMI_COLON', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'j')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'getarg')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 't')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 's')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'j')])])])])])])])]), Token('SEMI_COLON', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'openr')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '5')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 't')])])])])])]), Token('SEMI_COLON', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'getarg')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 't')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 's')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'j')])])])])])]), Token('SEMI_COLON', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'openw')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '6')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 't')])])])])])]), Token('SEMI_COLON', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'while_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'putchar')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'getchar')]), Tree(Token('RULE', 'parameters'), [None])])])])])]), Tree('neq_oeprator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '*'), Token('CHAR', 'e')])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Token('SEMI_COLON', ';')])])])])])])])]), Tree(Token('RULE', 'definition'), [Tree(Token('RULE', 'function_definition'), [Token('NAME', 'convert'), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 's')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'v')])])])]), Tree(Token('RULE', 'block_statement'), [Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'auto_statement'), [Tree('identifier', [Token('NAME', 'm')]), Tree('identifier', [Token('NAME', 'i')]), Tree('identifier', [Token('NAME', 'j')]), Tree('identifier', [Token('NAME', 'c')]), Tree('identifier', [Token('NAME', 'sign')]), Token('SEMI_COLON', ';')])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'i')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'O')])])])])]), Token('SEMI_COLON', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'j')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), Tree('sub_operator', [])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '1')])])])])]), Token('SEMI_COLON', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'label_statement'), [Token('__ANON_0', 'init:')])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'm')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '0')])])])])]), Token('SEMI_COLON', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'sign')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '0')])])])])]), Token('SEMI_COLON', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'label_statement'), [Token('__ANON_0', 'loop:')])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'switch_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'C')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'char')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 's')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'pre_inc_dec_expression'), [Tree(Token('RULE', 'unary_inc'), []), Tree('identifier', [Token('NAME', 'j')])])])])])])])]), Tree(Token('RULE', 'case_statement'), [Tree('constant_literal', [Token('CHAR', '-')]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'if_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'sign')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'goto_statement'), [Token('NAME', 'syntax'), Token('SEMI_COLON', ';')])]), None])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 's')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '1')])])])])]), Token('SEMI_COLON', ';')])])])]), Tree(Token('RULE', 'case_statement'), [Tree('constant_literal', [Token('__ANON_9', "' '")]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'goto_statement'), [Token('NAME', 'loop'), Token('SEMI_COLON', ';')])])]), Tree(Token('RULE', 'case_statement'), [Tree('constant_literal', [Token('CHAR', '*'), Token('CHAR', 'e')])]), Tree(Token('RULE', 'case_statement'), [Tree('constant_literal', [Token('CHAR', ',')]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('vector_identifier', [Tree('identifier', [Token('NAME', 'v')]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'post_inc_dec_expression'), [Tree('identifier', [Token('NAME', 'i')]), Tree(Token('RULE', 'unary_inc'), [])])])]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'ternary_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'sign')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'evaluated_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'unary_expression'), [Tree(Token('RULE', 'unary_minus'), []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'm')])])])])])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'm')])])])])])])]), Token('SEMI_COLON', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'if_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'c')])])]), Tree('eq_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '*'), Token('CHAR', 'e')])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'return_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'i')])])]), Token('SEMI_COLON', ';')])]), None])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'goto_statement'), [Token('NAME', 'init'), Token('SEMI_COLON', ';')])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'if_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '0')])])]), Tree('lte_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'c')])])]), Tree('and_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'c')])])]), Tree('lte_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '9')])])])])])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'block_statement'), [Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'm')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '10')])])]), Tree('mul_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'm')])])]), Tree('add_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'c')])])]), Tree('sub_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '0')])])])])])])])])])])]), Token('SEMI_COLON', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'goto_statement'), [Token('NAME', 'loop'), Token('SEMI_COLON', ';')])])])]), None])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'label_statement'), [Token('__ANON_0', 'syntax:')])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'printf')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('string_literal', [Token('ESCAPED_STRING', '"bad syntax*n"')])])])])])]), Token('SEMI_COLON', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'return_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'unary_expression'), [Tree(Token('RULE', 'unary_minus'), []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('INT', '1')])])])])]), Token('SEMI_COLON', ';')])])])])])])"""