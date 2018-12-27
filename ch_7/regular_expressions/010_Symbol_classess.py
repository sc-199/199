'''
  სიმბოლური კლასები
  ==================

  \d აღნიშნავს ერთ სიმბოლურ ციფრს [0-9] დიაპაზონში.
  ამრიგად \d არის (0|1|2|3|4|5|6|7|8|9) რეგულარული გამოსახულების შემოკლებული სახე.
  ასეთივე შემოკლებული სახეები არსებობს სხვა სიმბოლური კლასებისთვისაც.
  
  \d    ნებისმიერი ციფრი 0-დან 9-მდე
  \D    ნებისმიერი სიმბოლო ციფრების გარდა
  \w    ნებისმიერი ასო, ციფრი ან ქვედა ტირე (_) (ე.წ. „ანბანური“ სიმბოლოები)
  \W    ნებისმიერი სიმბოლო, რომელიც არ არის ასო, ციფრი ან ქვედა ტირე (_)
  \s    სიმბოლოები: ინტერვალის, ტაბულაციის ან ახალ ხაზზე გადასვლის (ENTER) (ე.წ. „ინტერვალის“ სიმბოლოები)
  \S    ნებისმიერი სიმბოლო, რომელიც არ არის ინტერვალის, ტაბულაციის ან ახალ ხაზზე გადასვლის (ENTER).

  სიმბოლური კლასების გამოყენება მოსახერხებელია რეგულარული გამოსახულებების კომპაქტურად ჩასაწერად.
  [0-5] სიმბოლოების კლასს შეესაბამება ნებისმიერი ერთი ციფრი 0-დან 5-ის ჩათვლით.
  [0-5] ჩაწერა უფრო მარტივია ვიდრე 0|1|2|3|4|5 ჩანაწერი.
'''

import re

text = "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans,\n\
6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge."

xmas_regex = re.compile(r"\d+\s\w+")
mo = xmas_regex.findall(text)
print(mo)




# -------------------
input("\nDone!..")