''' მასივის ინვერტირება '''

def invert_array(A:list, N:int):
  """ მასივის შებრუნება (ინვერტირება)
      დიაპაზონი [0, N-1]
  """

  # B = list(A)
  # for k in range(N):
  #   A[k] = B[N-1-k]

  for k in range(N//2):
    A[k], A[N-1-k] = A[N-1-k], A[k]


# ===> ტესტ ფუნქცია <===
def test_invert_array():
# ------ #Test1 ---------
  arr1 = [1, 2, 3, 4, 5]
  print(arr1)
  invert_array(arr1, 5)
  print(arr1)

  if arr1 == [5, 4, 3, 2, 1]:
    print("#Test1 – OK\n")
  else:
    print("#Test1 – FAIL\n")


# ------ #Test2 ---------
  arr2 = [0]*7 + [10]
  print(arr2)
  invert_array(arr2, 8)
  print(arr2)
  
  if arr2 == ([10] + [0]*7):
    print("#Test2 – OK")
  else:
    print("#Test2 – FAIL")



# ------------------
test_invert_array()




# -----------------
input("\nDone!..")
