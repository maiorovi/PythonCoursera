num = 49
tens = num // 10
ones = num % 10;
# print tens,ones

# print 10 * tens + ones


#clock arithmetic
hour = 18
shift = 8

print (hour + shift) % 24


#application - wrap around

width = 800
position = 1000
move = 5

position = (position + move) % width

print( position)