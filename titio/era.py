import requests
from linguagem import traduzir

def orquestrar(query):
    # Tese (Flask - porta 5000)
    try:
        tese = requests.get(f'http://127.0.0.1:5000/perplexity?q={query}').json()
    except:
        tese = {'erro':'Tese não disponível','codigo':traduzir('Tese')}
    
    # Antítese (Express - porta 3000)
    try:
        antitese = requests.get(f'http://127.0.0.1:3000/deepseek?q={query}').json()
    except:
        antitese = {'erro':'Antítese não disponível','codigo':traduzir('Antitese')}
    
    # NLP (porta 4000)
    try:
        nlp = requests.get(f'http://127.0.0.1:4000/nlp?q={query}').json()
    except:
        nlp = {'erro':'NLP não disponível','codigo':traduzir('NLP')}
    
    # ML (porta 6000)
    try:
        ml = requests.get(f'http://127.0.0.1:6000/ml?x=5').json()
    except:
        ml = {'erro':'ML não disponível','codigo':traduzir('ML')}
    
    # Síntese final
    sintese = {
        'tese': tese,
        'antitese': antitese,
        'nlp': nlp,
        'ml': ml,
        'sintese': f'Síntese final integrada para {query}',
        'codigo':traduzir('Sintese')
    }
    return sintese

if __name__ == '__main__':
    resultado = orquestrar('ERA projeto')
    print(resultado)
