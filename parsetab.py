
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CLASS_VAR COLON COMMA DIVIDE DO ELSE END EQ GETS GLOBAL_VAR GT GTE HASHROCKET ID IF INSTANCE_VAR LBRACE LBRACKET LPAREN LT LTE MINUS MINUS_ASSIGN NEQ NUMBER PLUS PLUS_ASSIGN PUTS RBRACE RBRACKET RPAREN STRING TIMES WHILEprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : variable_declaration\n                 | print_statement\n                 | control_structure\n                 | array_declaration\n                 | hash_declaration\n                 | input_statementinput_statement : ID ASSIGN GETSvariable_declaration : ID ASSIGN expressionprint_statement : PUTS LPAREN argument_list RPAREN\n                       | PUTS LPAREN RPAREN\n                       | PUTS STRING\n                       | PUTSargument_list : argument_list COMMA expression\n                     | expressioncontrol_structure : if_statement\n                         | while_statementif_statement : IF expression statement_list ENDwhile_statement : WHILE expression statement_list ENDexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | NUMBER\n                  | STRING\n                  | IDarray_declaration : ID ASSIGN LBRACKET array_elements RBRACKET\n                         | ID ASSIGN LBRACKET RBRACKETarray_elements : array_elements COMMA expression\n                      | expressionhash_declaration : ID ASSIGN LBRACE hash_elements RBRACE\n                        | ID ASSIGN LBRACE RBRACEhash_elements : hash_elements COMMA hash_pair\n                     | hash_pairhash_pair : expression COLON expression\n                 | STRING COLON expression\n                 | expression HASHROCKET expressionempty :'
    
_lr_action_items = {'ID':([0,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,33,34,35,37,40,44,45,46,47,48,49,50,51,52,53,54,55,56,],[10,10,-3,-4,-5,-6,-7,-8,-9,-15,-18,-19,23,23,-2,23,23,-14,10,-24,-25,-26,10,-11,23,23,-10,-13,10,23,23,10,-28,-32,-12,23,-20,-22,-23,-21,-27,23,-31,23,23,23,23,]),'PUTS':([0,2,3,4,5,6,7,8,9,11,12,13,16,19,20,21,22,23,24,25,28,30,32,35,37,40,44,46,47,48,49,50,52,],[11,11,-3,-4,-5,-6,-7,-8,-9,-15,-18,-19,-2,-14,11,-24,-25,-26,11,-11,-10,-13,11,11,-28,-32,-12,-20,-22,-23,-21,-27,-31,]),'IF':([0,2,3,4,5,6,7,8,9,11,12,13,16,19,20,21,22,23,24,25,28,30,32,35,37,40,44,46,47,48,49,50,52,],[14,14,-3,-4,-5,-6,-7,-8,-9,-15,-18,-19,-2,-14,14,-24,-25,-26,14,-11,-10,-13,14,14,-28,-32,-12,-20,-22,-23,-21,-27,-31,]),'WHILE':([0,2,3,4,5,6,7,8,9,11,12,13,16,19,20,21,22,23,24,25,28,30,32,35,37,40,44,46,47,48,49,50,52,],[15,15,-3,-4,-5,-6,-7,-8,-9,-15,-18,-19,-2,-14,15,-24,-25,-26,15,-11,-10,-13,15,15,-28,-32,-12,-20,-22,-23,-21,-27,-31,]),'$end':([1,2,3,4,5,6,7,8,9,11,12,13,16,19,21,22,23,25,28,30,37,40,44,46,47,48,49,50,52,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-15,-18,-19,-2,-14,-24,-25,-26,-11,-10,-13,-28,-32,-12,-20,-22,-23,-21,-27,-31,]),'END':([3,4,5,6,7,8,9,11,12,13,16,19,21,22,23,25,28,30,32,35,37,40,44,46,47,48,49,50,52,],[-3,-4,-5,-6,-7,-8,-9,-15,-18,-19,-2,-14,-24,-25,-26,-11,-10,-13,46,49,-28,-32,-12,-20,-22,-23,-21,-27,-31,]),'ASSIGN':([10,],[17,]),'LPAREN':([11,],[18,]),'STRING':([11,14,15,17,18,26,27,33,34,45,51,53,54,55,56,],[19,22,22,22,22,22,43,22,22,22,22,43,22,22,22,]),'NUMBER':([14,15,17,18,26,27,33,34,45,51,53,54,55,56,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'LBRACKET':([17,],[26,]),'LBRACE':([17,],[27,]),'GETS':([17,],[28,]),'RPAREN':([18,21,22,23,29,31,47,48,57,],[30,-24,-25,-26,44,-17,-22,-23,-16,]),'PLUS':([20,21,22,23,24,25,31,38,42,43,47,48,57,58,60,61,62,],[33,-24,-25,-26,33,33,33,33,33,-25,33,33,33,33,33,33,33,]),'MINUS':([20,21,22,23,24,25,31,38,42,43,47,48,57,58,60,61,62,],[34,-24,-25,-26,34,34,34,34,34,-25,34,34,34,34,34,34,34,]),'COMMA':([21,22,23,29,31,36,38,39,41,47,48,57,58,59,60,61,62,],[-24,-25,-26,45,-17,51,-30,53,-34,-22,-23,-16,-29,-33,-35,-37,-36,]),'RBRACKET':([21,22,23,26,36,38,47,48,58,],[-24,-25,-26,37,50,-30,-22,-23,-29,]),'COLON':([21,22,23,42,43,47,48,],[-24,-25,-26,54,56,-22,-23,]),'HASHROCKET':([21,22,23,42,43,47,48,],[-24,-25,-26,55,-25,-22,-23,]),'RBRACE':([21,22,23,27,39,41,47,48,59,60,61,62,],[-24,-25,-26,40,52,-34,-22,-23,-33,-35,-37,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,20,24,],[2,32,35,]),'statement':([0,2,20,24,32,35,],[3,16,3,3,16,16,]),'variable_declaration':([0,2,20,24,32,35,],[4,4,4,4,4,4,]),'print_statement':([0,2,20,24,32,35,],[5,5,5,5,5,5,]),'control_structure':([0,2,20,24,32,35,],[6,6,6,6,6,6,]),'array_declaration':([0,2,20,24,32,35,],[7,7,7,7,7,7,]),'hash_declaration':([0,2,20,24,32,35,],[8,8,8,8,8,8,]),'input_statement':([0,2,20,24,32,35,],[9,9,9,9,9,9,]),'if_statement':([0,2,20,24,32,35,],[12,12,12,12,12,12,]),'while_statement':([0,2,20,24,32,35,],[13,13,13,13,13,13,]),'expression':([14,15,17,18,26,27,33,34,45,51,53,54,55,56,],[20,24,25,31,38,42,47,48,57,58,42,60,61,62,]),'argument_list':([18,],[29,]),'array_elements':([26,],[36,]),'hash_elements':([27,],[39,]),'hash_pair':([27,53,],[41,59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','analizador_sintactico.py',8),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','analizador_sintactico.py',12),
  ('statement_list -> statement','statement_list',1,'p_statement_list','analizador_sintactico.py',13),
  ('statement -> variable_declaration','statement',1,'p_statement','analizador_sintactico.py',20),
  ('statement -> print_statement','statement',1,'p_statement','analizador_sintactico.py',21),
  ('statement -> control_structure','statement',1,'p_statement','analizador_sintactico.py',22),
  ('statement -> array_declaration','statement',1,'p_statement','analizador_sintactico.py',23),
  ('statement -> hash_declaration','statement',1,'p_statement','analizador_sintactico.py',24),
  ('statement -> input_statement','statement',1,'p_statement','analizador_sintactico.py',25),
  ('input_statement -> ID ASSIGN GETS','input_statement',3,'p_input_statement','analizador_sintactico.py',30),
  ('variable_declaration -> ID ASSIGN expression','variable_declaration',3,'p_variable_declaration','analizador_sintactico.py',35),
  ('print_statement -> PUTS LPAREN argument_list RPAREN','print_statement',4,'p_print_statement','analizador_sintactico.py',40),
  ('print_statement -> PUTS LPAREN RPAREN','print_statement',3,'p_print_statement','analizador_sintactico.py',41),
  ('print_statement -> PUTS STRING','print_statement',2,'p_print_statement','analizador_sintactico.py',42),
  ('print_statement -> PUTS','print_statement',1,'p_print_statement','analizador_sintactico.py',43),
  ('argument_list -> argument_list COMMA expression','argument_list',3,'p_argument_list','analizador_sintactico.py',54),
  ('argument_list -> expression','argument_list',1,'p_argument_list','analizador_sintactico.py',55),
  ('control_structure -> if_statement','control_structure',1,'p_control_structure','analizador_sintactico.py',63),
  ('control_structure -> while_statement','control_structure',1,'p_control_structure','analizador_sintactico.py',64),
  ('if_statement -> IF expression statement_list END','if_statement',4,'p_if_statement','analizador_sintactico.py',68),
  ('while_statement -> WHILE expression statement_list END','while_statement',4,'p_while_statement','analizador_sintactico.py',72),
  ('expression -> expression PLUS expression','expression',3,'p_expression','analizador_sintactico.py',77),
  ('expression -> expression MINUS expression','expression',3,'p_expression','analizador_sintactico.py',78),
  ('expression -> NUMBER','expression',1,'p_expression','analizador_sintactico.py',79),
  ('expression -> STRING','expression',1,'p_expression','analizador_sintactico.py',80),
  ('expression -> ID','expression',1,'p_expression','analizador_sintactico.py',81),
  ('array_declaration -> ID ASSIGN LBRACKET array_elements RBRACKET','array_declaration',5,'p_array_declaration','analizador_sintactico.py',89),
  ('array_declaration -> ID ASSIGN LBRACKET RBRACKET','array_declaration',4,'p_array_declaration','analizador_sintactico.py',90),
  ('array_elements -> array_elements COMMA expression','array_elements',3,'p_array_elements','analizador_sintactico.py',97),
  ('array_elements -> expression','array_elements',1,'p_array_elements','analizador_sintactico.py',98),
  ('hash_declaration -> ID ASSIGN LBRACE hash_elements RBRACE','hash_declaration',5,'p_hash_declaration','analizador_sintactico.py',106),
  ('hash_declaration -> ID ASSIGN LBRACE RBRACE','hash_declaration',4,'p_hash_declaration','analizador_sintactico.py',107),
  ('hash_elements -> hash_elements COMMA hash_pair','hash_elements',3,'p_hash_elements','analizador_sintactico.py',114),
  ('hash_elements -> hash_pair','hash_elements',1,'p_hash_elements','analizador_sintactico.py',115),
  ('hash_pair -> expression COLON expression','hash_pair',3,'p_hash_pair','analizador_sintactico.py',122),
  ('hash_pair -> STRING COLON expression','hash_pair',3,'p_hash_pair','analizador_sintactico.py',123),
  ('hash_pair -> expression HASHROCKET expression','hash_pair',3,'p_hash_pair','analizador_sintactico.py',124),
  ('empty -> <empty>','empty',0,'p_empty','analizador_sintactico.py',132),
]
