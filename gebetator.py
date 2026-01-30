import secrets

length = int(input("Input key length (bytes): "))
secret_key = secrets.token_hex(length)

print(secret_key)
