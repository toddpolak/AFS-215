import { expect } from 'chai'
import fizzbuzz from '../Fizzbuzzkata.js'

describe('Test', () => {
    it('returns 1 when pass in a 1', () => {
        expect(fizzbuzz(1)).to.equal('1')
    })
    it('returns 2 when pass in a 2', () => {
        expect(fizzbuzz(2)).to.equal('2')
    })
})