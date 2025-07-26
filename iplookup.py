import requests

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()
        print("\n🔍 IP Address Information:")
        print(f"IP       : {data.get('ip')}")
        print(f"City     : {data.get('city')}")
        print(f"Region   : {data.get('region')}")
        print(f"Country  : {data.get('country')}")
        print(f"Location : {data.get('loc')}")
        print(f"Org      : {data.get('org')}")
    except Exception as e:
        print("Error:", e)

ip = input("Enter an IP address (or leave blank for your own IP): ")
get_ip_info(ip.strip() or "")
