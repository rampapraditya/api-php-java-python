import requests

def send_sum_request(a, b):
    url = "http://localhost/api/index.php"
    payload = {
        "a": a,
        "b": b
    }

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            print(f"Hasil penjumlahan {a} + {b} = {data['result']}")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh pemakaian
if __name__ == "__main__":
    try:
        a = int(input("Masukkan angka a: "))
        b = int(input("Masukkan angka b: "))
        send_sum_request(a, b)
    except ValueError:
        print("Masukkan harus berupa angka!")
