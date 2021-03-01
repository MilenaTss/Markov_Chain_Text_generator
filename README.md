This is a text generator based on Markov chains. In this project, I use chains of length 2 and length 3, this is written in two different files. 
Accordingly, the generator based on chains of length 3 works much better. 
You can submit any file to the generator, on the basis of which it will create new sentences. 
It also needs to tell the number of messages that you want to see.
The program uses the nltk library, which helps to break text into tokens in some specific way. 
In this case, we only split using whitespaces using the WhitespaceTokenizer.
This program also uses the Counter data type from the connections module, which helps you count the number of word combinations.
So I use the random.choices function, which uses additional data to help me choose the next word in a sentence in an optimized way.
As a result, we get sentences that also have to comply with certain rules in order to look like real ones. The sentence should start with a capital letter and not be too short.