#!/bin/python3
import math
import os
import random
import re
import sys
size = [int(i) for i in input().split()]
word = [size[ord(c)-97] for c in input()] #select the character height
print(max(word)*len(word))#final Output
