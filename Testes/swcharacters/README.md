# StarWars Characters

Olá!

Neste repositório há um arquivo `main.py` com uma classe `Character` e uma função `features_together(a, b)`

A classe e a função tem uma docstring com descrição acompanhada de trechos de sessões de console do Python.

Os trechos de console na documentação da classe e da função exemplificam como é esperado que a classe e função se comportem. Eles também serão usados no teste automatizado para validar a implementação.

## Atividade

Sua tarefa será implementar a classe `Character`.

- Ela deve receber um nome de um personagem da saga Star Wars: `Character("Luke Skywalker")`
- A classe deve proibir tentativas de criar um personagem que não existe, ou com um nome que
pode se referenciar a mais de um personagem
- Uma instância de `Character` chamada `personagem` deve retornar o nome do personagem com o seguinte código: `personagem.name`
- Uma instância de `Character` chamada `personagem` deve retornar a lista de filmes que o personagem aparece, em ordem alfabética, com o seguinte código: `personagem.movies`
- Ao instanciar um `Character` no console Python espera-se que a saída seja um texto copiável que cria um `Character` com o mesmo nome

Para descobrir se um personagem existe no universo Star Wars e em quais filmes aparece, use a biblioteca `requests` e faça requisições na [SWAPI](https://swapi.co/).

Na [documentação da SWAPI](https://swapi.co/documentation) você econtrará informações sobre como buscar determinados personagens, quais atributos eles tem disponíveis e como buscar informações dos filmes da saga.

---

Com a classe `Character` implementada o próximo passo é implementar a função `features_together(a, b)`

Os dois parâmetros devem ser uma instância da classe `Character`, a função deve subir uma exceção se receber algum outro tipo de parâmetro.

A função deve retornar uma lista de filmes, em ordem alfabética, em que os personagens A e B estão presentes. Se os personagens não aparecem num mesmo filme a função deve retornar uma lista vazia.

## Validação

Você pode validar sua solução conforme desenvolve executando o `main.py`, que irá testar os trechos de console para checar se a implementação se comporta como o esperado.

Exemplo:
```
➜  python3 main.py
**********************************************************************
File "main.py", line 50, in __main__.features_together
Failed example:
    features_together(Character("Anakin Skywalker"), Character("Darth Vader"))
Expected:
    ['Revenge of the Sith']
Got:
    []
**********************************************************************
1 items had failures:
   1 of   2 in __main__.features_together
***Test Failed*** 1 failures.
```

Aqui a implementação passou em quase todos os testes, falhou em apenas 1.
Era esperado que o resultado da chamada `features_together(Character("Anakin Skywalker"), Character("Darth Vader"))` fosse `['Revenge of the Sith']` e não `['Revenge of the Sith']`.

Quando sua implementação estiver correta e passar nos 7 testes o script **não** gera uma saída:
```
➜  python3 main.py
➜
```

## Regras

Sua solução deve funcionar com Python 3.6 ou Python 3.7.

Use a biblioteca `requests` para fazer requisições na SWAPI.

Não altere a documentação da classe ou das funções.

## Dica

Não tente resolver tudo de uma vez. Aproveite os testes para tentar resolver 1 problema de cada vez, rode os testes com frequência para verficiar que o que você já resolveu ainda funciona.

Não se preocupe num primeiro momento em fazer uma solução otimizada. Pode refatorar para algo melhor se tiver sobrando tempo.

- [Documentação da requests](https://requests.kennethreitz.org/en/master/)
- [Documentação da SWAPI](https://swapi.co/documentation)
