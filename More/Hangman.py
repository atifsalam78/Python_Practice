{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53331aad",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "from string import ascii_lowercase\n",
    "from words import get_random_word\n",
    " \n",
    " \n",
    "def get_num_attempts():\n",
    "    \"\"\"Get user-inputted number of incorrect attempts for the game.\"\"\"\n",
    "    while True:\n",
    "        num_attempts = input(\n",
    "            'How many incorrect attempts do you want? [1-25] ')\n",
    "        try:\n",
    "            num_attempts = int(num_attempts)\n",
    "            if 1 <= num_attempts <= 25:\n",
    "                return num_attempts\n",
    "            else:\n",
    "                print('{0} is not between 1 and 25'.format(num_attempts))\n",
    "        except ValueError:\n",
    "            print('{0} is not an integer between 1 and 25'.format(\n",
    "                num_attempts))\n",
    " \n",
    " \n",
    "def get_min_word_length():\n",
    "    \"\"\"Get user-inputted minimum word length for the game.\"\"\"\n",
    "    while True:\n",
    "        min_word_length = input(\n",
    "            'What minimum word length do you want? [4-16] ')\n",
    "        try:\n",
    "            min_word_length = int(min_word_length)\n",
    "            if 4 <= min_word_length <= 16:                 return min_word_length             else:                 print('{0} is not between 4 and 16'.format(min_word_length))         except ValueError:             print('{0} is not an integer between 4 and 16'.format(                 min_word_length)) def get_display_word(word, idxs):     \"\"\"Get the word suitable for display.\"\"\"     if len(word) != len(idxs):         raise ValueError('Word length and indices length are not the same')     displayed_word = ''.join(         [letter if idxs[i] else '*' for i, letter in enumerate(word)])     return displayed_word.strip() def get_next_letter(remaining_letters):     \"\"\"Get the user-inputted next letter.\"\"\"     if len(remaining_letters) == 0:         raise ValueError('There are no remaining letters')     while True:         next_letter = input('Choose the next letter: ').lower()         if len(next_letter) != 1:             print('{0} is not a single character'.format(next_letter))         elif next_letter not in ascii_lowercase:             print('{0} is not a letter'.format(next_letter))         elif next_letter not in remaining_letters:             print('{0} has been guessed before'.format(next_letter))         else:             remaining_letters.remove(next_letter)             return next_letter def play_hangman():     \"\"\"Play a game of hangman.     At the end of the game, returns if the player wants to retry.     \"\"\"     # Let player specify difficulty     print('Starting a game of Hangman...')     attempts_remaining = get_num_attempts()     min_word_length = get_min_word_length()     # Randomly select a word     print('Selecting a word...')     word = get_random_word(min_word_length)     print()     # Initialize game state variables     idxs = [letter not in ascii_lowercase for letter in word]     remaining_letters = set(ascii_lowercase)     wrong_letters = []     word_solved = False     # Main game loop     while attempts_remaining > 0 and not word_solved:\n",
    "        # Print current game state\n",
    "        print('Word: {0}'.format(get_display_word(word, idxs)))\n",
    "        print('Attempts Remaining: {0}'.format(attempts_remaining))\n",
    "        print('Previous Guesses: {0}'.format(' '.join(wrong_letters)))\n",
    " \n",
    "        # Get player's next letter guess\n",
    "        next_letter = get_next_letter(remaining_letters)\n",
    " \n",
    "        # Check if letter guess is in word\n",
    "        if next_letter in word:\n",
    "            # Guessed correctly\n",
    "            print('{0} is in the word!'.format(next_letter))\n",
    " \n",
    "            # Reveal matching letters\n",
    "            for i in range(len(word)):\n",
    "                if word[i] == next_letter:\n",
    "                    idxs[i] = True\n",
    "        else:\n",
    "            # Guessed incorrectly\n",
    "            print('{0} is NOT in the word!'.format(next_letter))\n",
    " \n",
    "            # Decrement num of attempts left and append guess to wrong guesses\n",
    "            attempts_remaining -= 1\n",
    "            wrong_letters.append(next_letter)\n",
    " \n",
    "        # Check if word is completely solved\n",
    "        if False not in idxs:\n",
    "            word_solved = True\n",
    "        print()\n",
    " \n",
    "    # The game is over: reveal the word\n",
    "    print('The word is {0}'.format(word))\n",
    " \n",
    "    # Notify player of victory or defeat\n",
    "    if word_solved:\n",
    "        print('Congratulations! You won!')\n",
    "    else:\n",
    "        print('Try again next time!')\n",
    " \n",
    "    # Ask player if he/she wants to try again\n",
    "    try_again = input('Would you like to try again? [y/Y] ')\n",
    "    return try_again.lower() == 'y'\n",
    " \n",
    " \n",
    "if __name__ == '__main__':\n",
    "    while play_hangman():\n",
    "        print()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}