import numpy as np

student_scores = np.array([[72, 72, 74, 21],  
                           [69, 90, 88, 47],
                           [90, 95, 93, 27],
                           [47, 57, 44, 75],
                           [76, 78, 75, 30],
                           [71, 83, 78, 20],
                           [88, 95, 92, 88],
                           [40, 43, 39, 60],
                           [64, 64, 67, 81],
                           [38, 60, 50, 25],
                           [58, 54, 52, 85], 
                           [40, 52, 43, 62],
                           [65, 81, 73, 41],
                           [78, 72, 70, 42]])

math_scores = student_scores[:,0]
science_scores = student_scores[:,1]
english_scores = student_scores[:,2]
history_scores = student_scores[:,3]

avg_math = np.average(math_scores)
avg_science = np.average(science_scores) 
avg_english = np.average(english_scores)
avg_history = np.average(history_scores)

print("Average Math Score:", avg_math)
print("Average Science Score:", avg_science)
print("Average English Score:", avg_english) 
print("Average History Score:", avg_history)

highest_score_subj = np.argmax([avg_math, avg_science, avg_english, avg_history])

if highest_score_subj == 0:
  print("Math has the highest average score")
elif highest_score_subj == 1:
  print("Science has the highest average score")  
elif highest_score_subj == 2:
  print("English has the highest average score")
else:
  print("History has the highest average score")
