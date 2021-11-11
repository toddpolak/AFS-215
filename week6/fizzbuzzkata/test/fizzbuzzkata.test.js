import { assert } from 'chai'
import fizzbuzz from '../Fizzbuzzkata.js'

describe('Test', () => {
    it('Get 1 when  I pass in 1', () => {
        assert.equal(fizzbuzz(1), '1')
    })
    it('Get 2 when I pass in 2', () => {
        assert.equal(fizzbuzz(2), '2')
    })
    it('Get Fizz when I pass in 3', () => {
        assert.equal(fizzbuzz(3), 'Fizz')
    })
    it('Get Buzz when I pass in 5', () => {
        assert.equal(fizzbuzz(5), 'Buzz')
    })
    it('Get Fizz when I pass in 6 (a multiple of 3)', () => {
        assert.equal(fizzbuzz(6), 'Fizz')
    })
    it('Get Buzz when I pass in 10 (a multiple of 5)', () => {
        assert.equal(fizzbuzz(10), 'Buzz')
    })
    it('Get FizzBuzz when I pass in 15 (a multiple of 3 and 5)', () => {
        assert.equal(fizzbuzz(15), 'FizzBuzz')
    })

    // Should fail:
    it('failing test (this test should fail)', () => {
        assert.equal(fizzbuzz(7), '7')
    })
})