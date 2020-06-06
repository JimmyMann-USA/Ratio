# Ratio
Ratio functions return value for unknown variable in fraction set equal to a specific ratio.
Can be used to lock aspect ratios. 
Can use functions in different ways: 
(1) ratio_num() --Solve for unknown Numerator for fraction set equal to a specific ratio.
(2) ratio_den()--- Solve for unknown Denominator '' '' 
(3) Solve for unknown variable in list corresponding to fraction set equal to a specific ratio, and determines whether you're solving for numerator or denominator.  

Example Problem: 
Solve for x. 
3/4 = x/100 

Code: 
problem = [3, 4, 'x', 100] 
print(ratio(problem)) 
>>>75 
Alt Code: 
print(ratio_num(3,4,100))

Problem: 
Maintain aspect ratio of 16/9 for video player, regardless of window size. Window Height has been shrunk to 300px. 
Code: 
window_height = 300 
window_width = ratio(16, 9, 'x', window_height)
