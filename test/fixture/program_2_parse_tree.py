import pytest

@pytest.fixture # type: ignore
def program_example_2_parse_tree() -> str:
  return """Tree(Token('RULE', 'program'), [Tree(Token('RULE', 'definition'), [Tree(Token('RULE', 'function_definition'), [Token('NAME', 'printf'), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'fmt')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x1')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x2')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x3')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x4')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x5')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x6')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x7')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x8')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x9')])])])]), Tree(Token('RULE', 'block_statement'), [Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'extrn_statement'), [Token('NAME', 'printn'), Token('NAME', 'char'), Token('NAME', 'putchar'), Token('TERMINATE', ';'), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'auto_statement'), [Tree('identifier', [Token('NAME', 'adx')]), Tree('identifier', [Token('NAME', 'x')]), Tree('identifier', [Token('NAME', 'c')]), Tree('identifier', [Token('NAME', 'i')]), Tree('identifier', [Token('NAME', 'j')]), Token('TERMINATE', ';'), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'i')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('__ANON_9', '0')])])])])]), Token('TERMINATE', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'adx')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), Tree('and_operator', [])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x1')])])])])]), Token('TERMINATE', ';')])])])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'label_statement'), [Token('__ANON_0', 'loop :'), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'while_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'evaluated_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'c')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'char')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'fmt')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'post_inc_dec_expression'), [Tree('identifier', [Token('NAME', 'i')]), Tree(Token('RULE', 'unary_inc'), [])])])])])])])])])]), Tree('neq_oeprator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '%')])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'block_statement'), [Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'if_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'c')])])]), Tree('eq_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '*'), Token('CHAR', 'e')])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'return_statement'), [None, Token('TERMINATE', ';')])]), None])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'putchar')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'c')])])])])])]), Token('TERMINATE', ';')])])])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'x')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), Tree('mul_operator', [])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'post_inc_dec_expression'), [Tree('identifier', [Token('NAME', 'adx')]), Tree(Token('RULE', 'unary_inc'), [])])])])]), Token('TERMINATE', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'switch_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'c')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'char')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'fmt')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'post_inc_dec_expression'), [Tree('identifier', [Token('NAME', 'i')]), Tree(Token('RULE', 'unary_inc'), [])])])])])])])]), Tree(Token('RULE', 'case_statement'), [Tree('constant_literal', [Token('CHAR', 'd')]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'case_statement'), [Tree('constant_literal', [Token('CHAR', 'o')]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'if_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x')])])]), Tree('lt_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'O')])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'block_statement'), [Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'x')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), Tree('sub_operator', [])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x')])])])])]), Token('TERMINATE', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'putchar')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '-')])])])])])]), Token('TERMINATE', ';')])])])])]), None])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'printn')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'c')])])]), Tree('eq_operator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'ternary_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', 'z')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('__ANON_9', '8')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('number_literal', [Token('__ANON_9', '1'), Token('__ANON_9', '0')])])])])])])])])])]), Token('TERMINATE', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'goto_statement'), [Token('NAME', 'loop'), Token('TERMINATE', ';')])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'case_statement'), [Tree('constant_literal', [Token('CHAR', 'c')]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'putchar')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x')])])])])])]), Token('TERMINATE', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'goto_statement'), [Token('NAME', 'loop'), Token('TERMINATE', ';')])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'case_statement'), [Tree('constant_literal', [Token('CHAR', 's')]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'while_statement'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'assignment_expression'), [Tree('identifier', [Token('NAME', 'c')]), Tree(Token('RULE', 'assignment_operator'), [Token('EQUAL', '='), None]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'relation_expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'char')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'x')])])]), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'post_inc_dec_expression'), [Tree('identifier', [Token('NAME', 'j')]), Tree(Token('RULE', 'unary_inc'), [])])])])])]), Tree('neq_oeprator', []), Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '*'), Token('CHAR', 'e')])])])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'putchar')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'lvalue_expression'), [Tree('identifier', [Token('NAME', 'c')])])])])])]), Token('TERMINATE', ';')])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'goto_statement'), [Token('NAME', 'loop'), Token('TERMINATE', ';')])])])])])])])])])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'rvalue_statement'), [Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'function_expression'), [Tree('identifier', [Token('NAME', 'putchar')]), Tree(Token('RULE', 'parameters'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'constant_expression'), [Tree('constant_literal', [Token('CHAR', '%')])])])])])]), Token('TERMINATE', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'post_inc_dec_expression'), [Tree('identifier', [Token('NAME', 'i')]), Tree(Token('RULE', 'unary_dec'), [])])]), Token('TERMINATE', ';')]), Tree(Token('RULE', 'expression'), [Tree(Token('RULE', 'rvalue'), [Tree(Token('RULE', 'post_inc_dec_expression'), [Tree('identifier', [Token('NAME', 'adx')]), Tree(Token('RULE', 'unary_dec'), [])])]), Token('TERMINATE', ';')])])]), Tree(Token('RULE', 'statement'), [Tree(Token('RULE', 'goto_statement'), [Token('NAME', 'loop'), Token('TERMINATE', ';')])])])])])])])])"""