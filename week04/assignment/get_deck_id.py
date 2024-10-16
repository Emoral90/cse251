import requests
import json

def print_dict(dict, title=''):
    """ Display a dictionary in a structured format """
    if title != '':
        print(f'Dictionary: {title}')
    print(json.dumps(dict, indent=3))
    
if __name__ == '__main__':

    response = requests.get(r'https://deckofcardsapi.com/api/deck/new/')

    # Check the status code to see if the request succeeded.
    if response.status_code == 200:
        data = response.json()

        print_dict(data)

        if 'success' in data:
            if data['success'] == True:
                print(data['deck_id'])
            else:
                print('Error in requesting ID')
        else:
            print('Error in requesting ID')
    else:
        print('Error in requesting ID')

