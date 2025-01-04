from model import *
from tokens import *
from utils import *

###############################################################################
# Constants for different runtime value types
###############################################################################
TYPE_NUMBER = 'TYPE_NUMBER'  # Default to 64-bit float
TYPE_STRING = 'TYPE_STRING'  # String managed by the host language
TYPE_BOOL   = 'TYPE_BOOL'    # true | false

class Compiler:
  def __init__(self):
    self.code = []

  def emit(self, instruction):
    self.code.append(instruction)

  def compile(self, node):
    if isinstance(node, Integer):
      value = (TYPE_NUMBER, float(node.value))
      self.emit(('PUSH', value))

    elif isinstance(node, Float):
      value = (TYPE_NUMBER, float(node.value))
      self.emit(('PUSH', value))

    elif isinstance(node, Bool):
      value = (TYPE_BOOL, True if node.value == True or node.value == 'true' else False)
      self.emit(('PUSH', value))

    elif isinstance(node, String):
      value = (TYPE_STRING, stringify(node.value))
      self.emit(('PUSH', value))

    elif isinstance(node, BinOp):
      self.compile(node.left)
      self.compile(node.right)
      if node.op.token_type == TOK_PLUS:
        self.emit(('ADD',))
      elif node.op.token_type == TOK_MINUS:
        self.emit(('SUB',))
      elif node.op.token_type == TOK_STAR:
        self.emit(('MUL',))
      elif node.op.token_type == TOK_SLASH:
        self.emit(('DIV',))
      elif node.op.token_type == TOK_CARET:
        self.emit(('EXP',))
      elif node.op.token_type == TOK_MOD:
        self.emit(('MOD',))
      elif node.op.token_type == TOK_LT:
        self.emit(('LT',))
      elif node.op.token_type == TOK_GT:
        self.emit(('GT',))
      elif node.op.token_type == TOK_LE:
        self.emit(('LE',))
      elif node.op.token_type == TOK_GE:
        self.emit(('GE',))
      elif node.op.token_type == TOK_EQ:
        self.emit(('EQ',))
      elif node.op.token_type == TOK_NE:
        self.emit(('NE',))

    elif isinstance(node, PrintStmt):
      self.compile(node.value)
      if node.end == '':
        self.emit(('PRINT',))
      else:
        self.emit(('PRINTLN',))

    elif isinstance(node, Stmts):
      for stmt in node.stmts:
        self.compile(stmt)

  def generate_code(self, node):
    self.emit(('LABEL', 'START'))
    self.compile(node)
    self.emit(('HALT',))
    return self.code
