source_code = """
tweet x = 5
chirp x
caw i squack 10 {
    chirp i
}
chirr add(a, b) {
    tweet result = a + b
    chirp result
}
hoot add(3, 4)

chirr factorial(n) {
    screech n == 1 mew {
        chirp 1
    }
    tweet f = hoot factorial(n - 1)
    chirp n * f
}
tweet n = 5
chirp hoot factorial(n)

chirr greet(name) {
    tweet message = "Hello, " + name + "!"
    chirp message
}
tweet user_name = quack "What's your name?"
hoot greet(user_name)
"""
