"""
Regras ano bissexto:
1. O ano for divisível por 4, 
2. mas não divisível por 100, 
3. exceto se ele for também divisível por 400.
"""

def ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
        return 'bissexto'
    return 'nao bissexto'

if __name__ == '__main__':
    assert ano_bissexto(2020) == 'bissexto'
    assert ano_bissexto(2019) == 'nao bissexto'
    assert ano_bissexto(2000) == 'bissexto'
    assert ano_bissexto(1900) == 'nao bissexto'
    assert ano_bissexto(1742) == 'nao bissexto'
