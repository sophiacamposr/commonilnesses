import requests
from bs4 import BeautifulSoup

def scrape_the_facts(url):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to get the webpage: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all symptoms or disease names from <h3> tags
        symptoms_list = soup.find_all('h3')
        symptoms = [item.text.strip() for item in symptoms_list]

        return symptoms
         
    except Exception as e:
        print(f"An error has occurred: {e}")
        return []

def scrape_prevention(url):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to get the webpage: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        prevention_tips = []

        # Find paragraphs with prevention tips
        for paragraph in soup.find_all('p'):
            strong_tag = paragraph.find('strong')
            if strong_tag and 'tips to prevent' in strong_tag.text.lower():
                prevention_tips.append(paragraph.text.strip())

        return prevention_tips
    except Exception as e:
        print(f"An error has occurred: {e}")
        return []

def display_symptoms(symptoms):
    print("List of Diseases:")
    for index, symptom in enumerate(symptoms, start=1):
        print(f"{symptom}")

def display_prevention_tips(prevention_tips):
    print("\nPrevention Tips:")
    for index, tip in enumerate(prevention_tips, start=1):
        print(f"{index}. {tip}")

def main():
    url = "https://www.careinsurance.com/blog/health-insurance-articles/most-common-diseases-in-summer-season"

    # Scrape symptoms and prevention tips
    symptoms = scrape_the_facts(url)
    prevention_tips = scrape_prevention(url)

    # Display the results
    if symptoms:
        display_symptoms(symptoms)
    else:
        print("No diseases found.")



    # Check if both lists are of equal length before prompting
    if symptoms and prevention_tips and len(symptoms) == len(prevention_tips):
        while True:
            try:
                # Ask the user to pick a number corresponding to the disease
                choice = int(input(f"\nSelect the number corresponding to the disease (1-{len(symptoms)}): "))
                
                # Validate the choice
                if 1 <= choice <= len(symptoms):
                    # Print the corresponding prevention tip
                    print(f"\nYou selected: {symptoms[choice - 1]}")
                    print(f"Prevention Tip: {prevention_tips[choice - 1]}")
                    break
                else:
                    print(f"Please enter a number between 1 and {len(symptoms)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:
        print("The number of diseases does not match the number of prevention tips.")

if __name__ == "__main__":
    main()
