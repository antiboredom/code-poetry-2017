from textblob import TextBlob
from textblob import Word

text = '''
The history of all hitherto existing society is the history of class struggles.

Freeman and slave, patrician and plebeian, lord and serf, guild-master and journeyman, in a word, oppressor and oppressed, stood in constant opposition to one another, carried on an uninterrupted, now hidden, now open fight, a fight that each time ended, either in a revolutionary reconstitution of society at large, or in the common ruin of the contending classes.

In the earlier epochs of history, we find almost everywhere a complicated arrangement of society into various orders, a manifold gradation of social rank. In ancient Rome we have patricians, knights, plebeians, slaves; in the Middle Ages, feudal lords, vassals, guild-masters, journeymen, apprentices, serfs; in almost all of these classes, again, subordinate gradations.

The modern bourgeois society that has sprouted from the ruins of feudal society has not done away with class antagonisms. It has but established new classes, new conditions of oppression, new forms of struggle in place of the old ones.

Our epoch, the epoch of the bourgeoisie, possesses, however, this distinct feature: it has simplified class antagonisms. Society as a whole is more and more splitting up into two great hostile camps, into two great classes directly facing each other - Bourgeoisie and Proletariat.'''


# create a TextBlob object
blob = TextBlob(text)

# extract all the sentences
sentences = blob.sentences
for sentence in sentences:
    print sentence

# extract all the words
sentences = blob.sentences
for sentence in sentences:
    words = sentence.words
    for word in words:
        print word

# get parts of speech
tags = blob.tags
for tag in tags:
    word = tag[0]
    pos = tag[1]
    print word, pos


# get only the nouns
tags = blob.tags
nouns = []
for tag in tags:
    if tag[1] == 'NN':
        nouns.append(tag[0])


# do the same thing but with a list comprehension
nouns = [tag[0] for tag in blob.tags if tag[1]=='NN']

# let's remove duplicates by putting this in a set (just like a list but no duplicates are allowed)
nouns = set(nouns)
print nouns

# get the definitions for each noun
for noun in nouns:
    definitions = Word(noun).definitions
    print definitions


# get most common noun phrases
print blob.np_counts

