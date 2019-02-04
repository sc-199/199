''' მაქსიმუმის პოვნა '''

def max2(x, y):
  if x > y:
    return x
  else:
    return y
  
  # if x > y:
  #   return x
  
  # return y


def max3(x, y, z):
  return max2(x, max2(y,z))



# ------------------
print(max2(4, 9))
print(max3(5, 2, 7))
print(max3(4.69, 5.41, 1.02))
print(max3(4.69, 5.41, 17))
print(max3("ab", "abc", "abd"))       # Duck typing
                                      # იხვისებრი პოლიმორფიზმი, იხვისებრი ტიპიზაცია
                                      # თუ რაღაც ჰგავს იხვს, ცურავს როგორც იხვი,
                                      # ხმას გამოსცემს როგორც იხვი, მაშინ ის იხვია.



# ----------------
input("\nDone!..")