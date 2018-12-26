'''
  ძებნის ძუნწი და არაწუნწი მაგალითები
  miser - ძუნწი
  greedy - ხარბი
'''

import re

# ძებნის ძუნწი მაგალითი
greedy_ha_regex = re.compile(r"(Ha){3,5}")
mo = greedy_ha_regex.search("HaHaHaHaHa")
print(mo.group())

# ძებნის არაძუნწი მაგალითი
nongreedy_ha_regex = re.compile(r"(Ha){3,5}?")
mo = nongreedy_ha_regex.search("HaHaHaHaHa")
print(mo.group())



# ------------------
input("\nDone!..")