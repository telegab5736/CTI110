#CTI-110
#P3LAB-Debugging
#Brian Telega
#18June2020

#pseudocode
#if the score is greater than or equal to 90 then its an A.
#else, if the score is greater than or equal to 80 then its a B
#else, if the score is greater than or equal to 70 then its a C
#else, if the score is greater than or equal to 60 the its a D
#else, the grade is a F


if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B')
    else:
        if score >= C_SCORE:
            print('Your grade is C')
        else:
            if score >= D_SCORE:
                print('Your grade is D')
            else:
                print('Your grade is F')
