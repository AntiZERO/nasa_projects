import requests
from datetime import datetime, timedelta

def test_nasa_connection():
    """
    Test connection to NASA's API by fetching today's asteroid data
    """
    # NASA's demo API key
    API_KEY = "DEMO_KEY"
    
    # Get today's date
    today = datetime.today().strftime('%Y-%m-%d')
    
    # NASA's Near Earth Object API endpoint
    url = f"https://api.nasa.gov/neo/rest/v1/feed"
    
    # Parameters for the API request
    params = {
        "start_date": today,
        "end_date": today,
        "api_key": API_KEY
    }
    
    print("Connecting to NASA's API...")
    
    try:
        # Make the request
        response = requests.get(url, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            asteroid_count = data['element_count']
            print(f"\nFound {asteroid_count} asteroids for {today}")
            print("\n" + "="*50)  # Separator line
            
            # Get all asteroids for today
            asteroids = data['near_earth_objects'][today]
            
            # Print details for each asteroid
            for i, asteroid in enumerate(asteroids, 1):
                diameter_meters = asteroid['estimated_diameter']['meters']['estimated_diameter_max']
                distance_km = float(asteroid['close_approach_data'][0]['miss_distance']['kilometers'])
                speed_kph = float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
                
                print("-"*50)  # Separator line
                print("-"*50)  # Separator line
                print(f"\nASTEROID {i}:")
                print(f"Name: {asteroid['name']}")
                print(f"Size: {diameter_meters:.6f} meters")
                print(f"Distance: {distance_km:,.9f} km from Earth")
                print(f"Speed: {speed_kph:,.9f} km/h")
                print(f"Potentially hazardous: {asteroid['is_potentially_hazardous_asteroid']}")
                print("-"*50)  # Separator line
                print("-"*50)  # Separator line
            
        else:
            print(f"Error accessing NASA API: Status code {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_nasa_connection()