function [checkedtimes] = checktimes(input)
% Checks whether there is a significant point that correlates with a
% manually found significant point in the interval of +- 2 seconds. Returns
% the final accuracy vector for every manually found point (1 if it is
% generated by the program, 0 otherwise).
checkedtimes = zeros(1, length(input)/5);
k = 1;
disp("INPUT!");
disp(input);
index = 1;
while index < length(input)
    for jindex = index:index + 4
        if input(jindex) == 1
            checkedtimes(k) = 1;
        end
    end
    k = k + 1;
    index = index + 5;
end
end
