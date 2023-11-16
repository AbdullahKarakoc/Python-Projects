def is_sparse(num):
    prev_bit = 0
    while num > 0:
        current_bit = num & 1
        if prev_bit == 1 and current_bit == 1:
            return False
        prev_bit = current_bit
        num >>= 1
    return True

def solution(N):
    for i in range(N // 2, 0, -1):
        if is_sparse(i) and is_sparse(N - i):
            return i
    return -1

# Kullanıcıdan giriş al
N = int(input("Bir sayı girin: "))
result = solution(N)
if result != -1:
    print(f"Sparse decomposition: {result} + {N - result}")
else:
    print("Bu sayının sparse decomposition yok.")
