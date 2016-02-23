"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import codeskulptor


#codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    #find all distinct values in hand
    eachvalue = set(hand)
    eachvalue = list(eachvalue)
    numberofeach = []
    for n_dumb in eachvalue:
        numberofeach.append(0)
    ##tally each for each
    for value_ in hand:
        for n_dumb in range(0,len(eachvalue)):
            if value_ == eachvalue[n_dumb]:
                numberofeach[n_dumb] += 1
    
    
    #find highest combo
    highest = 0
    
    for n_dumb in range(0,len(eachvalue)):
        if eachvalue[n_dumb] * numberofeach[n_dumb] > highest:
            highest = eachvalue[n_dumb] * numberofeach[n_dumb]
            
    
    return highest

      


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    held_dice = tuple(held_dice)
    sequences = gen_all_sequences(range(1,(num_die_sides+1)), num_free_dice)
    
    expected = 0
    for seq_ in sequences:
        
        seq_ = seq_
        
        temp_seq = held_dice+seq_
        
        
        
        expected+=score(temp_seq)
    #print expected_value
    #print (len(sequences)+1)
    expected = float(expected)/(len(sequences))
    
    
    return expected



def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    ans = [[]]
    for x_dumb in hand:
        ans = ans + [y_dumb + [x_dumb] for y_dumb in ans]
    
    ans_ = []
    for x_dumb in ans:
        ans_.append(tuple(x_dumb))
    
    return set(ans_)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    
    all_holds = gen_all_holds(hand)
   
    max_hold = 0
    pass_hold = []
    for hold_ in all_holds:
        
        
        
        current_value = expected_value(hold_, num_die_sides, (len(hand)-len(hold_)))
        
        if max_hold < current_value:
            max_hold = current_value
            pass_hold = hold_
            
    return (max_hold, pass_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()




#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



