''' მასივის კოპირება
======================

    გვაქვს A მასივი N განზომილებით.
    B მასივში დავაკოპიროთ A მასივი (ასლის შექმნა).
    გასაგებია, რომ B მასივიც A მასივის შესაბამისი ზომის უნდა იყოს
'''

N = int(input("Array's size: "))
A = [0] * N
B = [0] * N

print("\nEnter", N, "integer number's:")
for k in range(N):
  A[k] = int(input())

# B მასში ჩავწეროთ A მასივის ასლი
for k in range(N):
  B[k] = A[k]

print()
print("Array A:", A)
print("Array B:", B)

print()

# C = A

# სრული ასლი (დუბლიკატი)
C = list(A)
print("Array C:", C)




# ----------------
input("\nDone!..")