import random

whenlist = ['Once upon a time', 'Long ago', 'Last Tuesday', 'On December 22nd', 'After the superbowl']
who1list = ['Mickey Mouse', 'Batman', 'Bob', 'Beyonce', 'Cinderella']
who2list = ['Robert', 'Scooby-Doo', 'Optimus Prime', 'Johnny Test', 'President Biden']
wherelist = ['the market', 'the Essence Festival', 'Tampa, Florida', 'Disney World', 'Bob\'s house']
action1list = ['sitting on the porch', 'volunteering at the soup kitchen', 'driving to Walmart', 'studying for Calculus', 'listening to Frank Ocean']
action2list = ['eat ice cream', 'fight aliens', 'learn karate', 'walk to the Great Wall of China', 'start a business']

when = random.choice(whenlist)
who1 = random.choice(who1list)
who2 = random.choice(who2list)
where = random.choice(wherelist)
action1 = random.choice(action1list)
action2 = random.choice(action2list)

print(f'{when}, {who1} was {action1} when {who1} decided to go to {where}. At {where}, {who1} met {who2}. The two instantly became friends, and they decided that they wanted to {action2}. {who1} and {who2} went to {action2}, and they lived happily ever after.')