score = 0

print('Welcome to my Python quiz game! ')

playing = input('Are you ready to play? ')

if playing.lower() != 'yes':
    quit()

answer = input('What is the capital of France? ')
if answer.lower() == 'paris':
    print('Correct!')
    score = score + 1
    print(f'Your score is {score}')
else:
    print('Incorrect!')

answer = input('Who was the first president of the United States? ')
if answer.lower() == 'george washington':
    print('Correct!')
    score = score + 1
    print(f'Your score is {score}')
else:
    print('Incorrect!')

answer = input('What is the highest mountain in the world? ')
if answer.lower() == 'mount everest':
    print('Correct!')
    score = score + 1
    print(f'Your score is {score}')
else:
    print('Incorrect!')

answer = input('Who painted the famous artwork "The Starry Night"? ')
if answer.lower() == 'vincent van gogh':
    print('Correct!')
    score = score + 1
    print(f'Your score is {score}')
else:
    print('Incorrect!')

answer = input('What is the largest ocean in the world? ')
if answer.lower() == 'the pacific ocean':
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')

print(f'Over! You answered {score} questions correctly!')