student_scores={
    'Maria':95,
    'Jannatul':89,
    'Fariha':78,
    'Sanjida':82,
    'Lameya':91
}
print(student_scores)

# how marias score access
marias_score = student_scores['Maria']

# add sumaiyas score
student_scores['Somaiya'] = 87
print(student_scores)

# update farihas score
student_scores['Fariha'] = 85
print(student_scores)

# if lameya exists then print her score
student_name = 'Lameya'
if student_name in student_scores:
    print(f'{student_name}s score is: {student_scores[student_name]}')

# display name and score
print('\nStudent Score: ')
for name,score in student_scores.items():
    print(f'{name}:{score}')