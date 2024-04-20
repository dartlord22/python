//remove blanks
function removeBlanks(string) {
    let result = '';
    for (let i = 0; i < string.length; i++) {
        if (string[i] !== ' ') {
            result += string[i];
        }
    }
    return result;
}
console.log(removeBlanks(" Pl ayTha tF u nkyM usi c ")); // should return "PlayThatFunkyMusic"

//get digits
function getDigits(string) {
    let result = '';
    for (let i = 0; i < sstringtr.length; i++) {
        if (!isNaN(string[i]) && string[i] !== ' ') {
            result += string[i];
        }
    }
    return Number(result);
}
console.log(getDigits("abc8c0d1ngd0j0!8")); //should return 801008

//acronyms
function acronyms(string) {
    let words = string.split(' ');
    let result = '';
    for (let i = 0; i < words.length; i++) {
        if (words[i].length > 0) {
            result += words[i][0].toUpperCase();
        }
    }
    return result;
}
console.log(acronym(" there's no free lunch - gotta pay yer way. ")); //"TNFL-GPYW"

//count non-spaces
function countNonSpaces(string) {
    let count = 0;
    for (let i = 0; i < string.length; i++) {
        if (string[i] !== ' ') {
            count++;
        }
    }
    return count;
}
console.log(countNonSpaces("Honey pie, you are driving me crazy")); //should return 29

//remove shorter strings
function removeShorterStrings(array, value) {
    let result = [];
    for (let i = 0; i < array.length; i++) {
        if (array[i].length >= value) {
            result.push(array[i]);
        }
    }
    return result;
}
console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)); //removes the word 'the'