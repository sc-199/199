'''
  \d\d\d  ===> \d{3}
  \d\d\d\d\d  ===> \d{5}
  (Ha){3}   ===> (Ha)(Ha)(Ha)
  Ha{3,5}   ===> ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
'''

import re

ha_regex = re.compile(r"(Ha){3}")
mo = ha_regex.search("HaHa, Paata HaHaHa, Nana, Teona, HaHaHa")
print(mo.group())

mo = ha_regex.search(r"Ha")
print(mo)



# ---------------------
input("\nDone!..")