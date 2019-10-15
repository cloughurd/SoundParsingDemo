import wsd_calc

while True:
    f = input('Please enter the name of the file you want to process: ')
    mode = input('Do you want to submit a file for thresholding? y/n: ')
    if mode == 'y':
        id = wsd_calc.post_threshold(f)
        print('The id for that threshold is: {}'.format(id))
    else:
        print('Okay, running WSD calculator then...')
        id = input('Please enter the id to connect this file to its threshold, enter NONE if no id: ')
        num_syllables = input('Please enter the number of syllables in the recorded word: ')
        num_syllables = int(num_syllables)
        wsd = wsd_calc.get_wsd(id, f, num_syllables)
        print('That word has a WSD of {}'.format(wsd))