/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/
function rotateStr(str, amnt) {
  let newStr = ""
  for(let i = str.length - (amnt % str.length); i < str.length; i++){
      newStr += str[i]
  }
  for(let i = 0; i < str.length - (amnt % str.length); i++){
      newStr += str[i]
  }
  return newStr

}

const strA1 = "ABCDABCD"; 
const strB1 = "CDAB";
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const expected1 = true;

const strA2 = "ABCD";
const strB2 = "CDBA";
// Explanation: all same letters in 2nd string, but out of order
const expected2 = false;

const strA3 = "ABCD";
const strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const expected3 = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */

function cleverSolution(s1, s2){
  let compareStr = s1 + s1
  return compareStr.includes(s2)
}

function isRotation(s1, s2) {
  if(s1.length !== s2.length){
    return false
  }
  for(let i = 1; i <= s1.length; i++){
    // console.log(i)
    // console.log(rotateStr(s1, i))
    if(rotateStr(s1,i) === s2){
      return true
    }
  }
  return false
}

console.log(isRotation(strA1, strB1))
console.log(isRotation(strA2, strB2))
console.log(isRotation(strA3, strB3))