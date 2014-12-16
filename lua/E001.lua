E001 = {}

function E001.solution()

    local sum = 0

    for x = 0, 999 do
        if (x % 3 == 0 or x % 5 == 0) then
            sum = sum + x
        end
    end

    return sum
end

return E001