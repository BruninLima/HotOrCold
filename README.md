# HotOrCold

Wordle with different rules


There are 2 different rulesets for determining wether a letter is hot or cold:
    - Closeness ruleset
    - Height ruleset
    
- Closeness :
    - The letter is hot (resp. cold) if the index of the correct letter is closer than not from the index of the given letter.  
    Example:
    
            If the correct letter is "G". 
        
            The guessed letter was "H". 
            
                It returns 'Hot'. 
                
            The guessed letter was "F":
            
                It returns 'Hot'.
                
            The guessed letter was "Z":
            
                It returns 'Cold'.
- Height:
    - The letter is hot (resp. cold) if the index is higher than the index of the correct letter
    - 
    Example:
    
            If the correct letter is "G". 
        
            The guessed letter was "H". 
            
                It returns 'Hot'. 
                
            The guessed letter was "F":
            
                It returns 'Cold'.
