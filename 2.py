# Even Fibonacci = every third Fibonacci
# …FOUR MILLION? Forget math!

def fibonacci():
	a = 1
	b = 2

	while True:
		yield a
		a, b = b, a + b

def under(n, seq):
	for x in seq:
		if x >= n: break
		yield x

print(sum(under(4000000, (x for x in fibonacci() if x % 2 == 0))))
