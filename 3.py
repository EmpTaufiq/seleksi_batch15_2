import numpy as np

def count_vowels ( input_string ) :
    counter_vowels = 0
    for i in range (len ( input_string )) :
        if ( np.any ( input_string [i] == 'a' or input_string [i] == 'i' or input_string [i] == 'u' or input_string [i] == 'e' or input_string [i] == 'o' ) ) :
            counter_vowels = counter_vowels + 1
    print(counter_vowels)