import  requests
from bs4 import BeautifulSoup

url = 'https://quizlet.com/583845418/se_ky-1_ssl101c-flash-cards/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=headers)
print(r.status_code)

soup = BeautifulSoup(r.content, "html.parser")

question = []
answer = []

for text in soup.find_all('a', {'class' : 'SetPageTerm-definitionText'}): 
    getText = text.getText()
    getAllQuestion = getText.split("?")
    getQuestion = getAllQuestion[0].split(", ", 1)
    question.append(getQuestion)

for text in soup.find_all('a', {'class' : 'SetPageTerm-wordText'}): 
    count = 0
    getText = text.getText()
    answer.append(getText)

def action(input):
    for i in range(len(question)):  
        if str(input) == str(question[i][0]):
            return answer[i]
        
