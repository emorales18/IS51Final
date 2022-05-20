"""
input: the test scores
initiate a iterator (counter) and accumulator (sum) and set it to zero
loop through the list test scores
add all the test scores
increment the counter by one
once the loop ends, there are no more scores to add
divide the accumulator (sum) by counter
display the output to the user
output: print the average of the class scores
"""

"""
scores
iterator, accumulator = 0
loop through scores
    accumulator = accumulator + scores 
    iterator = iterator + 1
output = accumulator / total score
print output
"""

def calculate_average(scores):
    iterator = 0
    accumulator = 0
    student_count = len(scores)
    while iterator < len(scores):
        accumulator = accumulator + scores[iterator]
        iterator = iterator + 1
    average = accumulator / student_count
    return average

output = calculate_average(
    [78, 67, 56, 99, 80, 83, 82, 91, 94, 95, 77, 88, 85, 92, 91, 79, 88, 82, 81, 86, 94, 93, 92, 45])
print("The average of total scores in the class is:", output)