"""Learning to apply and use relational operators."""
__author__ = "730402537"

left_num = input("Left-hand side: ")
right_num = input("Right-hand side: ")
left_num_int = int(left_num)
right_num_int = int(right_num)
less_than = (bool(left_num_int < right_num_int))
print((left_num_int), "<", (right_num_int), "is", (less_than))
greater_equal = bool(left_num_int >= right_num_int)
print((left_num_int), ">=", (right_num_int), "is", (greater_equal))
equal = bool(left_num_int == right_num_int)
print((left_num_int), "==", (right_num_int), "is", (equal))
not_equal = bool(left_num_int != right_num_int)
print((left_num_int), "!=", (right_num_int), "is", (not_equal))