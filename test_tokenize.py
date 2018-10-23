import unittest
import shunting_yard as sy


class TokenizeTest(unittest.TestCase):
    def test_single_operator(self):
        tokens = list(sy.tokenize('1+2'))
        self.assertListEqual(tokens, ['1', '+', '2'])
        
    def test_multiple_operators(self):
        tokens = list(sy.tokenize('1+2+3'))
        self.assertListEqual(tokens,['1','+','2','+','3'])
    
    def test_multiple_different_operators(self):
        tokens = list(sy.tokenize('1+2*3'))
        self.assertListEqual(tokens,['1','+','2','*','3'])

class StackIsEmptyTest(unittest.TestCase):
    def test_empty_stack(self):
        stack = []
        self.assertTrue(sy.stackIsEmpty(stack))
    
    def test_nonempty_stack(self):
        stack = []
        item = "1"
        sy.pushToStack(stack,item)
        self.assertFalse(sy.stackIsEmpty(stack))
        
class PushToStackTest(unittest.TestCase):
    def test_for_empty_stack(self):
        stack = []
        item = "1"
        sy.pushToStack(stack,item)
        self.assertIsNotNone(stack)
        self.assertFalse(sy.stackIsEmpty(stack))
    def test_for_nonempty_stack(self):
        stack = ["1"]
        item = "2"
        self.assertEqual(len(stack),1)
        sy.pushToStack(stack,item)
        self.assertEqual(len(stack),2)
        
    def test_for_multiple_item_stack(self):
        stack = ["1","+"]
        item = "2"
        self.assertEqual(len(stack),2)
        sy.pushToStack(stack,item)
        self.assertEqual(len(stack),3)
        
class PopFromStackTest(unittest.TestCase):
    def test_for_empty_stack(self):
        stack = []
        self.assertRaises(IndexError, lambda: sy.popFromStack(stack))
        
    def test_for_nonempty_stack(self):
        stack = ["1"]
        item = sy.popFromStack(stack)
        self.assertEqual(item,"1")
        self.assertEqual(len(stack),0)
    def test_for_multiple_item_stack(self):
        stack = []
        sy.pushToStack(stack,"1")
        sy.pushToStack(stack,"+")
        sy.pushToStack(stack,"2")
        self.assertEqual(len(stack),3)
        item = sy.popFromStack(stack)
        self.assertEqual(len(stack),2)
        self.assertEqual(item,"2")
        
class PeekAtStackTest(unittest.TestCase):
    def test_for_empty_stack(self):
        stack = []
        self.assertRaises(IndexError,lambda: sy.peekAtStack(stack))
    def test_for_nonempty_stack(self):
        stack = []
        sy.pushToStack(stack,"1")
        self.assertEqual(len(stack),1)
        item = sy.peekAtStack(stack)
        self.assertEqual(item,"1")
        self.assertEqual(len(stack),1)
    def test_for_multiple_item_stack(self):
        stack = []
        sy.pushToStack(stack,"1")
        sy.pushToStack(stack,"+")
        sy.pushToStack(stack,"2")
        self.assertEqual(len(stack),3)
        item = sy.peekAtStack(stack)
        self.assertEqual(len(stack),3)
        self.assertEqual(item,"2")
        
class IsRightBracketTest(unittest.TestCase):
    def test_for_right_bracket(self):
        self.assertTrue(sy.isRightBracket(")"))
        self.assertTrue(sy.isRightBracket("]"))
    def test_for_left_bracket(self):
        self.assertFalse(sy.isRightBracket("("))
        self.assertFalse(sy.isRightBracket("["))
    def test_for_operators(self):
        self.assertFalse(sy.isRightBracket("+"))
        self.assertFalse(sy.isRightBracket("-"))
        self.assertFalse(sy.isRightBracket("*"))
        self.assertFalse(sy.isRightBracket("/"))
    def test_for_number(self):
        self.assertFalse(sy.isRightBracket("1"))

class IsLeftBracketTest(unittest.TestCase):
    def test_for_right_bracket(self):
        self.assertFalse(sy.isLeftBracket(")"))
        self.assertFalse(sy.isLeftBracket("]"))
    def test_for_left_bracket(self):
        self.assertTrue(sy.isLeftBracket("("))
        self.assertTrue(sy.isLeftBracket("["))
    def test_for_operators(self):
        self.assertFalse(sy.isLeftBracket("+"))
        self.assertFalse(sy.isLeftBracket("-"))
        self.assertFalse(sy.isLeftBracket("*"))
        self.assertFalse(sy.isLeftBracket("/"))
    def test_for_number(self):
        self.assertFalse(sy.isLeftBracket("1"))
        
        
class IsOperatorTest(unittest.TestCase):
    def test_for_operators(self):
        self.assertTrue(sy.isOperator("+"))
        self.assertTrue(sy.isOperator("-"))
        self.assertTrue(sy.isOperator("*"))
        self.assertTrue(sy.isOperator("/"))
    def test_for_non_operators(self):
        self.assertFalse(sy.isOperator("1"))
        self.assertFalse(sy.isOperator("("))
        self.assertFalse(sy.isOperator(")"))
        self.assertFalse(sy.isOperator("["))
        self.assertFalse(sy.isOperator("]"))
        self.assertFalse(sy.isOperator("a"))
        self.assertFalse(sy.isOperator("x"))
        self.assertFalse(sy.isOperator("d"))
        self.assertFalse(sy.isOperator("p"))
        self.assertFalse(sy.isOperator("m"))
        self.assertFalse(sy.isOperator("|"))
        self.assertFalse(sy.isOperator("~"))
        self.assertFalse(sy.isOperator("\\"))
        
class IsNumberTest(unittest.TestCase):
    def test_for_numbers(self):
        self.assertTrue(sy.isNumber("1"))
        self.assertTrue(sy.isNumber("12"))
        self.assertTrue(sy.isNumber("11"))
        self.assertTrue(sy.isNumber("123"))
        self.assertTrue(sy.isNumber("1234456"))
        self.assertTrue(sy.isNumber("0"))
        self.assertTrue(sy.isNumber("5674"))
    def test_for_non_numbers(self):
        self.assertFalse(sy.isNumber("a"))
        self.assertFalse(sy.isNumber("12a1"))
        self.assertFalse(sy.isNumber("t1"))
        self.assertFalse(sy.isNumber("q123"))
        self.assertFalse(sy.isNumber("654e"))
        self.assertFalse(sy.isNumber("1a"))
        self.assertFalse(sy.isNumber("one"))
        self.assertFalse(sy.isNumber("+"))
        self.assertFalse(sy.isNumber("("))
        
class IsDigitTest(unittest.TestCase):
    def test_for_numbers(self):
        self.assertTrue(sy.isDigit("0"))
        self.assertTrue(sy.isDigit("1"))
        self.assertTrue(sy.isDigit("2"))
        self.assertTrue(sy.isDigit("3"))
        self.assertTrue(sy.isDigit("4"))
        self.assertTrue(sy.isDigit("5"))
        self.assertTrue(sy.isDigit("6"))
        self.assertTrue(sy.isDigit("7"))
        self.assertTrue(sy.isDigit("8"))
        self.assertTrue(sy.isDigit("9"))
        
    def test_for_non_numbers(self):
        self.assertFalse(sy.isDigit("a"))
        self.assertFalse(sy.isDigit("("))
        self.assertFalse(sy.isDigit(")"))
        self.assertFalse(sy.isDigit("["))
        self.assertFalse(sy.isDigit("]"))
        self.assertFalse(sy.isDigit("+"))
        self.assertFalse(sy.isDigit("-"))
        self.assertFalse(sy.isDigit("*"))
        self.assertFalse(sy.isDigit("/"))
        self.assertFalse(sy.isDigit("~"))
        
class InfixToPostFixTest(unittest.TestCase):
    def test_single_operator(self):
        self.assertEqual("1 2 +",sy.infixToPostfix("1 + 2"))
    def test_multiple_operators(self):
        self.assertEqual("1 2 3 * +",sy.infixToPostfix("1 + 2 * 3"))
    def test_no_operator(self):
        self.assertEqual("1",sy.infixToPostfix("1"))
    def test_nothing(self):
        self.assertEqual("",sy.infixToPostfix(""))
        
class ComparePrecedenceTest(unittest.TestCase):
    def test_low_vs_low(self):
        self.assertEqual(0,sy.comparePrecedence("+","+"))
        self.assertEqual(0,sy.comparePrecedence("-","-"))
        self.assertEqual(0,sy.comparePrecedence("+","-"))
        self.assertEqual(0,sy.comparePrecedence("-","+"))
    def test_high_vs_low(self):
        self.assertEqual(-1,sy.comparePrecedence("+","*"))
        self.assertEqual(-1,sy.comparePrecedence("+","/"))
        self.assertEqual(-1,sy.comparePrecedence("-","*"))
        self.assertEqual(-1,sy.comparePrecedence("-","/"))
        
        self.assertEqual(1,sy.comparePrecedence("*","+"))
        self.assertEqual(1,sy.comparePrecedence("*","-"))
        self.assertEqual(1,sy.comparePrecedence("/","+"))
        self.assertEqual(1,sy.comparePrecedence("/","-"))
    def test_high_vs_high(self):
        self.assertEqual(0,sy.comparePrecedence("*","/"))
        self.assertEqual(0,sy.comparePrecedence("*","*"))
        self.assertEqual(0,sy.comparePrecedence("/","/"))
        self.assertEqual(0,sy.comparePrecedence("/","*"))
        
class AppendToOutputTest(unittest.TestCase):
    def test_append_to_empty_string(self):
        string = ""
        self.assertEqual("1",sy.appendToOutput(string,"1"))
    def test_append_nothing_to_empty_string(self):
        string = ""
        self.assertEqual("",sy.appendToOutput(string,""))
    def test_append_string_to_nonempty_string(self):
        string = "1"
        self.assertEqual("1 +",sy.appendToOutput(string,"+"))
    def test_append_string_to_multiple_nonempty_string(self):
        string = "1 +"
        self.assertEqual("1 + 2",sy.appendToOutput(string,"2"))