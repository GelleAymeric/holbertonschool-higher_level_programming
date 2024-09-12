#!/usr/bin/python3
"""Module for text_indentation function"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The input text to be processed

    Raises:
    TypeError: If text is not a string

    Returns:
    None: This function prints the formatted text, it doesn't return anything
    """
    # Vérifier si text est une chaîne
    if type(text) != str:
        raise TypeError("text must be a string")

    # Parcourir chaque caractère du texte
    for i in range(len(text)):
        # Imprimer le caractère
        print(text[i], end="")

        # Si le caractère est ., ? ou :, ajouter deux nouvelles lignes
        if text[i] in [".", "?", ":"]:
            print("\n")

        # Si on a imprimé deux nouvelles lignes, ignorer les espaces suivants
        if i < len(text) - 1 and text[i] in [".", "?", ":"] and text[i+1] == " ":
            while i < len(text) - 1 and text[i+1] == " ":
                i += 1
