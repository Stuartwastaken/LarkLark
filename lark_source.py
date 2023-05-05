source_code = """
    chirr init_fib(i) {
        screech i == 0 mew {
            tweet a = 0
        }
        screech i == 1 mew {
            tweet a = 1
        }
        chirp a
    }


    chirr fib(n) {
        tweet a = hoot init_fib(0)
        tweet b = hoot init_fib(1)
        caw i squack n {
            tweet temp = a + b
            tweet a = b
            tweet b = temp
        }
        chirp a
    }


    tweet x = 5
    chirp x
    caw i squack 10 {
        chirp i
        hoot fib(i)
    }

chirr add(a, b) {
    tweet result = a + b
    chirp result
}
    hoot add(3, 4)
"""