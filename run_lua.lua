require "luarocks.loader"
socket = require "socket"
cjson = require "cjson"

f = io.open('answers.txt', "r")

answers_text = f:read("*all")
answers = cjson.decode(answers_text)

f:close()

for x = 1, 1 do

    local modname = string.format("lua.E%03d", "" .. x)

    local start_time = socket.gettime()
    local solver = require(modname)
    local answer = solver:solution()
    local end_time = socket.gettime()

    print(string.format("Answer to %s is :: %s", modname, answer))
    print(1000 * (end_time - start_time) .. " ms")
    assert(answer == answers[x], answer .. " should equal " .. answers[x])
end
