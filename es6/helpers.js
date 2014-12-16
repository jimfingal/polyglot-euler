
function ascendingRange(start, stop, step) {

    var current = start;
    var range = [];

    while (current < stop) {
        range.push(current);
        current += step;
    }
    return range
}


function* ascendingRangeGen(start, stop, step) {

    var current = start;

    while (current < stop) {
        yield current;
        current += step;
    }
}

/*
var descendingRangeGen = function*(start, stop, step) {

    var current = start;

    while (current > stop) {
        yield current;
        current -= step;
    }
}
*/

//exports.descendingRangeGen = descendingRangeGen

exports.ascendingRange = ascendingRange
exports.ascendingRangeGen = ascendingRangeGen
