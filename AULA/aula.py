import requests
import sys

#os.makedirs ('./book')
def texto():
    try:    
        url = "https://www.gutenberg.org/cache/epub/73169/pg73169.txt"

        response = requests.get(url)

        if response.status_code == 200:
            
            with open ('book\download_file.txt', 'w', encoding='utf-8') as f:
                f.write(response.text)
                print("correct")
            
        else:
            print("Não funcionou")
        
    except :
        print (sys.exc_info()[0])
        
    
texto()