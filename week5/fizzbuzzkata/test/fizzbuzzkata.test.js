import { assert, expect } from 'chai'
import fizzbuzz from '../Fizzbuzzkata.js'

describe('Test', () => {
    it('returns 1 when pass in a 1', () => {
        assert.equal(fizzbuzz(1), '1')
    })
    it('returns 2 when pass in a 2', () => {
        assert.equal(fizzbuzz(2), '2')
    })
    it('returns Incorrect when pass in anything except a 1 or a 2', () => {
        expect(fizzbuzz(3)).to.equal('Incorrect')
    })

    // Should fail:
    it('returns Incorrect when pass in anything except a 1 or a 2', () => {
        expect(fizzbuzz(3)).to.equal('3')
    })
})