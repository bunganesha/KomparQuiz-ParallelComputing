import threading

data = [12, 7, 25, 3, 18, 5, 30]
def calculate_average():
    print("Task 1: Menghitung rata-rata")
    avg = sum(data) / len(data)
    print("Rata-rata:", avg)

def sum_odd_numbers():
    print("Task 2: Menjumlahkan angka ganjil")
    odd_numbers = [x for x in data if x % 2 != 0]
    total = sum(odd_numbers)
    print("Jumlah angka ganjil:", total)

def find_multiples_of_three():
    print("Task 3: Mencari kelipatan 3")
    multiples = [x for x in data if x % 3 == 0]
    print("Kelipatan 3:", multiples)

# Fork → membuat thread
t1 = threading.Thread(target=calculate_average)
t2 = threading.Thread(target=sum_odd_numbers)
t3 = threading.Thread(target=find_multiples_of_three)

# Parallel execution
t1.start()
t2.start()
t3.start()

# Join → menunggu semua selesai
t1.join()
t2.join()
t3.join()
print("Semua task selesai diproses")