##### Task 1 — Generate and Inspect the Data ###

import numpy as np

np.random.seed(42)

scores = np.random.randint(50,101, size=(5,4))
print("Scores:", scores)

#print score of 3rd student, 2nd subject
print("\nScore of 3rd student, 3nd subject:", scores[2,1])

print("\nAll Scores of last 2 students:", scores[-2:,:])

print("\nFirst 3 students, subejctts 2 & 3:", scores[:3,1:3])

#========================================================================#

##### Task 2 — Analyze with Broadcasting ####
col_mean = np.round(scores.mean(axis=0), 2)
print("\n Column-wise mean:", col_mean)

curve = np.array([5,3,7,2])
curved_scores = scores + curve

curved_scores = np.clip(curved_scores, None, 100)
print("\n Curved scores:", curved_scores)

row_max = curved_scores.max(axis=1)
print("\nRow-wise max score per student:", row_max)

#===================================================================#

#### Task 3 — Normalize and Identify ####
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)
print("\nNormalized scores:", normalized)

max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("\nIndex of highest normalized value (student, subject):", max_index)


above_90 = curved_scores[curved_scores > 90]
print("\nScores above 90:", above_90)

