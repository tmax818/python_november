/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const num1 = 1234;
const expected1 = 4321;

const num2 = 42;
const expected2 = 24;

const num3 = 8675309;
const expected3 = 9035768;

const num4 = 1;
const expected4 = 1;

/**
 * Reverses the given num.
 * - Time: O(?).
 * - Space: O(?).
 * @param {numing} num numing to be reversed.
 * @returns {numing} The given num reversed.
 */
function reverseNum(num) {
    num_str = num.toString()
    new_num_str = ''
    for(let i = num_str.length -1; i >= 0; i--){
        // console.log(num_str[i])
        new_num_str += num_str[i]
    }
    return (Number(new_num_str))
}

console.log(reverseNum(num1))
console.log(reverseNum(num2))
console.log(reverseNum(num3))
console.log(reverseNum(num4))