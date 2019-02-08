''' მასივში ელემენტის წრფივი ძებნა '''

def array_search(A:list, N:int, x:int):
  """ ახორციელებს x რიცხვის ძებნას A მასივში
      ინდექსით 0-დან N-1-ის ჩათვლით.
      პოვნის შემთხვევაში ფუნქცია აბრუნებს ნაპოვნი რიცხვის ინდექსს,
      წინააღმდეგ შემთხვევაში -1-ს.
      თუ ნაპოვნი რიცხვები რამდენიმეა მასივში,
      მაშინ დააბრუნებს ნაპოვნი პირველი ელემენტის ინდექსს.
  """
  for k in range(N):
    if A[k] == x:
      return k
  
  return -1


# ===> ტესტ ფუნქცია <===
def test_array_search():
  # ------ #test1 ---------
  arr1 = [1, 2, 3, 4, 5]
  index = array_search(arr1, 5, 8)

  if index == -1:
    print("#Test1 – OK")
  else:
    print("#Test1 – FAIL")


  # ------ #test2 ---------
  arr2 = [-1, -2, -3, -4, -5]
  index = array_search(arr2, 5, -4)

  if index == 3:
    print("\n#Test2 – OK")
  else:
    print("\n#Test2 – FAIL")


  # ------ #test2 ---------
  arr3 = [10, 20, 30, 10, 10]
  index = array_search(arr3, 5, 10)

  if index == 0:
    print("\n#Test3 – OK")
  else:
    print("\n#Test3 – FAIL")




# --------------------
test_array_search()




# ------------------
input("\nDone!...")