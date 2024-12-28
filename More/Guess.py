{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db5af700",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Guess The Number - Code with Harry\n",
    "#!/usr/bin/env python\n",
    "\n",
    "guess_count = 0\n",
    "counter = 0\n",
    "while True:\n",
    "    \n",
    "    num = 18\n",
    "    guess = int(input(\"Guess the Number: \"))\n",
    "    if guess == num:\n",
    "        counter += 1\n",
    "        print(\"Hurrah! You Won!\")\n",
    "        break\n",
    "        \n",
    "    else:\n",
    "        guess_count += 1\n",
    "        if guess < num:\n",
    "            print(\"You have entered less than the actual number\")\n",
    "        if guess > num:\n",
    "            print(\"You have entered greater than the actual Number\")\n",
    "            \n",
    "        print(\"Wrong! Keep Trying\")\n",
    "        print(5-guess_count,\"Guesses Left to Try\\n\")\n",
    "        \n",
    "        if guess_count == 5:\n",
    "            print(\"Game Over!\\n\")     \n",
    "            break\n",
    "            \n",
    "print(counter+guess_count,\"Times You Have Tried to Win\")"
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
