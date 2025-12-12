{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4b4d79c3-55b5-4358-a41a-bbba948a0bff",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'functions_week5' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 46\u001b[0m\n\u001b[1;32m     42\u001b[0m             has_special_char \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[1;32m     43\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m has_special_char\n\u001b[0;32m---> 46\u001b[0m functions_week5\u001b[38;5;241m.\u001b[39mpath\n",
      "\u001b[0;31mNameError\u001b[0m: name 'functions_week5' is not defined"
     ]
    }
   ],
   "source": [
    "###required functions###\n",
    "\n",
    "def check_min_len(password, min_len=8):\n",
    "    if len(password) == min_len:\n",
    "        return True \n",
    "    else:\n",
    "        return False\n",
    "\n",
    "def has_upper(password):\n",
    "    for char in password:\n",
    "        if char.isupper():\n",
    "            has_upper = True\n",
    "            break\n",
    "        else :\n",
    "            has_upper = False\n",
    "    return has_upper\n",
    "\n",
    "def has_lower(password):\n",
    "    for char in password:\n",
    "        if char.islower():\n",
    "            has_lower = True\n",
    "            break\n",
    "        else:\n",
    "            has_lower = False\n",
    "    return has_lower\n",
    "\n",
    "def has_digit(password):\n",
    "    for char in password:\n",
    "        if char.isdigit():\n",
    "            has_digit = True\n",
    "            break\n",
    "        else:\n",
    "            has_digit = False\n",
    "    return has_digit\n",
    "\n",
    "def has_special_char(passsword):\n",
    "    for char in password:\n",
    "        if not char.isalnum():\n",
    "            has_special_char = True\n",
    "            break\n",
    "        else: \n",
    "            has_special_char = False\n",
    "    return has_special_char\n",
    "\n",
    "\n",
    "functions_week5.path\n",
    "\n",
    "\n",
    "\n",
    "    \n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cc9f7cf-cb8f-4441-8e5a-2b308f27529e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
