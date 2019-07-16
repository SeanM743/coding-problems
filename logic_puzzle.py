"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

 1. The person who arrived on Wednesday bought the laptop.
  2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
 4. The writer is not Minsky.
  5. Neither Knuth nor the person who bought the tablet is the manager.
  6. Knuth arrived the day after Simon.
   7. The person who arrived on Thursday is not the designer.
   8. The person who arrived on Friday didn't buy the tablet.
    9. The designer didn't buy the droid.
   10. Knuth arrived the day after the manager.
    11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
import itertools
def logic_puzzle():
    
    (mon,tue,wed,thur,fri) = (1,2,3,4,5)

    for (Hamming,Knuth,Minksy,Simon,Wilkes) in itertools.permutations([1,2,3,4,5]):
        if Knuth == Simon +1:
            for (laptop,droid,tablet,iphone,_) in itertools.permutations([1,2,3,4,5]):
                if laptop == wed and Knuth != tablet and (iphone == tue or tablet == tue):
                    for (programmer,manager,designer,writer,_) in itertools.permutations([1,2,3,4,5]):
                        if (Knuth == manager +1 and  programmer != Wilkes  and writer != Minksy and 
                        manager != tablet and designer != thur and fri != tablet
                        and designer != droid and (set([laptop,Wilkes]) == set([mon,writer])) and (set([programmer,droid]) ==
                        set([Wilkes,Hamming]))):
                            return (Hamming,Knuth,Minksy,Simon,Wilkes)

print(logic_puzzle())
