import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:\Shiva\FODS\student_data.csv')

cor_mat = df[['Score', 'Hours_Studied ']].corr()
print(cor_mat)

correlation_per_course = df.groupby('Course')[['Hours_Studied ', 'Score']].corr().iloc[0::2, -1].reset_index(level=1, drop=True)
print("Correlation Coefficients for each course:")
print(correlation_per_course)

strongest_corr_course = correlation_per_course.idxmax()
weakest_corr_course = correlation_per_course.idxmin()

print(f"\nCourse with the Strongest Correlation: {strongest_corr_course}")
print(f"Course with the Weakest Correlation: {weakest_corr_course}")

average_scores_hours = df.groupby('Course').agg({'Score': 'mean', 'Hours_Studied ': 'mean'}).reset_index()
print("\nAverage Scores and Hours Studied for each course:")
print(average_scores_hours)
