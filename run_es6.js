var fs = require('fs');
var util = require('util');
var helpers = require('./es6/helpers');

var answers = JSON.parse(fs.readFileSync('./answers.txt', 'utf8'));
//console.log(answers);


for (let i of helpers.ascendingRangeGen(1, 2, 1)) {
    console.log(util.format("%03d", i));
}