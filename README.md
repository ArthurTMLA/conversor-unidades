# Conversor de Unidades em Python

Este é um projeto simples em Python que converte valores em **metros (m)** para outras unidades do sistema métrico:

- Milímetros (mm)  
- Centímetros (cm)  
- Decímetros (dm)  
- Decâmetros (dam)  
- Hectômetros (hm)  
- Quilômetros (km)  

O programa solicita ao usuário:  
1. O valor em metros que deseja converter.  
2. A unidade de medida desejada (usando apenas a sigla, ex: `KM`).  

Se o usuário informar uma unidade inválida, o programa exibirá uma mensagem de erro.

---

## 🖥️ Como executar

1. Certifique-se de ter o **Python 3** instalado.  
2. Baixe o arquivo `conversor_unidades.py`.  
3. No terminal, navegue até a pasta do arquivo e execute:

```bash
python conversor_unidades.py

📌 Exemplo de uso

Entrada:

Qual o tamanho em metros? 2500
Para qual unidade de medida deseja transformar esse valor? (utilize apenas a sigla ex: KM) km

Saída:

A medida de 2500.00 metros corresponde a 2.50 quilômetros.

Entrada inválida:

Qual o tamanho em metros? 2500
Para qual unidade de medida deseja transformar esse valor? (utilize apenas a sigla ex: KM) YY

Saída:

❌ Unidade de medida inválida! Use apenas: KM, HM, DAM, M, DM, CM ou MM.

📚 Aprendizados

Com este projeto, pratiquei:

    Entrada e saída de dados em Python (input() e print())

    Estruturas condicionais (if, elif, else)

    Formatação de números com casas decimais (f-strings)

    Tratamento de entradas inválidas

🚀 Próximos Passos

    Criar uma versão que converte automaticamente para todas as unidades.

    Criar uma interface gráfica com Tkinter ou versão web com Flask.

Feito por Arthur Santos 👩‍💻
