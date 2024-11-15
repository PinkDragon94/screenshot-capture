# screenshot_capture.py
import requests
from api_keys import API_KEY

base_url = 'https://api.apiflash.com/v1/urltoimage'

def capture_screenshot(url='http://google.com'):
    params = {
        'access_key': API_KEY,
        'url': url
    }
    
    try:
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            image_data = response.content
            
            with open('screenshots/screenshot.png', 'wb') as file:
                file.write(image_data)
            print("Screenshot saved successfully.")
            return True
        else:
            print('Error: Request failed with status code', response.status_code)
            return False
            
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return False

# Example usage:
capture_screenshot('http://google.com')