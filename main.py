def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

def analyze_word(word):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    num_vowels = sum(1 for char in word.lower() if char in vowels)
    num_consonants = sum(1 for char in word.lower() if char in consonants)

    return {
        "Palavra": word,
        "Palíndromo": "Sim" if is_palindrome(word) else "Não",
        "Número de vogais": num_vowels,
        "Número de consoantes": num_consonants,
        "Palavra ao contrário": word[::-1]
    }

if __name__ == "__main__":
    while True:
        word = input("Digite uma palavra para analisar (ou 'sair' para encerrar): ").strip()
        
        if word.lower() == 'sair':
            print("Saindo do programa... Até logo!")
            break
        
        analysis = analyze_word(word)
        
        print("\nAnálise da palavra:")
        for key, value in analysis.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")
