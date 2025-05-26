"""
5.Un algoritmo que dados cinco números los muestre ordenados de mayor a menor.
"""
print("De mayor a menor")
nums = [int(input(f"Número {i+1}: ")) for i in range(5)]
nums.sort(reverse=True)
print("Ordenados de mayor a menor:", nums)