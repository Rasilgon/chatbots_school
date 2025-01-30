def main(missatge_usuari):
    """
    Processa el missatge de l'usuari i retorna una resposta.
    """
    if missatge_usuari.lower() == "com et dius?":
        return "ChatbotPy: Em dic ChatBotPy, un programa creat amb Python!"
    elif missatge_usuari.lower() == "què fas?":
        return "ChatbotPy: Parlar amb tu i aprendre coses noves!"
    elif missatge_usuari.lower() == "adeu":
        return "ChatbotPy: Adéu! Que tinguis un bon dia."
    else:
        return "ChatbotPy: Ho sento, no entenc aquesta pregunta."
