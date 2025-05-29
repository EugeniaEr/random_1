import random

name = input("What's your name?\n ")
print(f"Hi, {name}!")

feel = input("How do you feel? (Normal, Good, Bad, Sad)\n")

normal = [ 'Got it, stability is good too.', 'Better than bad — that’s already a win.',
          '"Normal" isn’t too bad.']
good =[ 'Great, keep it up!', 'Awesome, that’s how it should be!', 'Glad to hear that!' ]
bad = [ 'Hang in there, it’ll get better.', 'Damn, hope it’s just temporary.', 
       'I get it, tough times happen.']
sad = [ 'Wish I could give you a hug.', 'I understand — it happens.', 
       'Hope it gets a little lighter.']

if feel == 'Normal':
    print(random.choice(normal))
elif feel == 'Good':
    print(random.choice(good))
elif feel == 'Bad':
    print(random.choice(bad))
elif feel == 'Sad':
    print(random.choice(sad))
else:
    print('Thanks for the answer!')