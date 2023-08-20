# The purpose of this program is to take Latitude and Longitude values and
# return more data about the given coordinates

# the program works but completely does not.
# It runs with errors that tell the request was not approved from the geocoders import.

from geopy.geocoders import Nominatim


# Get Geolocation Data
def GeoD(latitude, longitude):
    geolocator = Nominatim(user_agent="geolocation_app")
    location = geolocator.reverse(f"{latitude}, {longitude}")

    if location is not None:
        address = location.address
        return latitude, longitude, address
    else:
        return None

# User inter latitude and longitude data
def main():
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    geodata = GeoD(latitude, longitude)
    # Retrieve
    if geodata is not None:
        if geodata is not None:
            print("Geolocation data:")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Address: {geodata[2]}")
        else:
            print("Unable to retrieve geolocation data.")


if __name__ == "__main__":
    main()
