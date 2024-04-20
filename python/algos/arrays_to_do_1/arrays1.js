
//push front
function pushFront(array, value) {
    for (let i = array.length; i > 0; i--) {
        array[i] = array[i - 1];
    }
    array[0] = value;
    return array;
}

//pop front
function popFront(array) {
    const removedValue = array[0];
    for (let i = 0; i < array.length - 1; i++) {
        array[i] = array[i - 1];
    }
    array.length = array.length - 1;
    return removedValue;
}

//insert at 
function insertAt(array, index, value) {
    for (let i = array.length; i > index; i--) {
        array[i] = array[i - 1];
    }
    array[index] = value;
    return array;
}