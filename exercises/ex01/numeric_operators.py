"""Learning to use numeric operators."""
__author__ = "730402537"

left_num = input("Left-hand side: ")
right_num = input("Right-hand side: ")
left_num_int = int(left_num)
right_num_int = int(right_num)
exp_product = (left_num_int ** right_num_int)
print((left_num_int), "**", (right_num_int), "is", (exp_product))
quotient = (left_num_int / right_num_int)
print((left_num_int), "/", (right_num_int), "is", (quotient))
int_quotient = (left_num_int // right_num_int)
print((left_num_int), "//", (right_num_int), "is", (int_quotient))
remainder = (left_num_int % right_num_int)
print((left_num_int), "%", (right_num_int), "is", (remainder))