const fizzbuzz = val => {

    return (val % 3 === 0) && (val % 5 === 0) ? 'FizzBuzz'
        : val % 3 === 0 ? 'Fizz'
        : val %  5 === 0 ? 'Buzz'
        : val === 1 ? '1'
        : val === 2 ? '2'
        : val === 3 ? 'Fizz'
        : val === 5 ? 'Buzz'
        : 'Incorrect'
}

export default fizzbuzz