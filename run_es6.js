var fs = require('fs');
var assert = require('assert');
var helpers = require('./es6/helpers');
var sprintf = require('sprintf').sprintf;

var answers = JSON.parse(fs.readFileSync('./answers.txt', 'utf8'));


for (let i of helpers.ascendingRangeGen(1, 2, 1)) {
    var modname = sprintf("E%03d", i);
    console.log("Solving " + modname);

    console.time(modname);
    var solver = require('./es6/' + modname);
    var answer = solver.solution();
    console.log("Anwser :: " + answer);
    console.timeEnd(modname);


    assert.equal(answer, answers[i -1], "Should have correct answer");
}