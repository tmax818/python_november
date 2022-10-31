/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
// function acronymize(str) {
//   let str_array = str.split(" ")
//   // console.log(str_array)
//   let new_str = ""
//   for(let i = 0; i < str_array.length; i++){
//       // console.log(!!str_array[i][0])
//       if(str_array[i][0]){
//         new_str += str_array[i][0]
//       }
//   }

  function acronymize(str) {
  let new_str = ""
  for(let i = 0; i < str.length; i++){
    // console.log(str[i])
    // if i is a character and it's first character or (||)there is a space immediately before it 
    if(str[i] !== " " && (i === 0 || str[i - 1] === " ")){
      new_str += str[i]
    }
  }
  return(new_str.toUpperCase())
}

console.log(acronymize(str1))
console.log(acronymize(str2))
console.log(acronymize(str3))
console.log(acronymize(str4))