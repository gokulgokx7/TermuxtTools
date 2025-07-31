import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def track_number(number):
    try:
        parsed_number = phonenumbers.parse(number)
        
        # Validity check
        if not phonenumbers.is_valid_number(parsed_number):
            print("❌ Invalid phone number.")
            return

        print("✅ Valid number")
        print("🌍 Country/Region:", geocoder.description_for_number(parsed_number, 'en'))
        print("📞 Carrier:", carrier.name_for_number(parsed_number, 'en'))
        print("⏰ Timezone(s):", timezone.time_zones_for_number(parsed_number))
    except Exception as e:
        print("⚠️ Error:", e)

if __name__ == "__main__":
    number = input("📱 Enter phone number with country code (e.g. +919876543210): ")
    track_number(number)
