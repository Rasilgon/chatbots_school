import random

RESPUESTA_CHANTEO = """\033[1mAl parecer quieres hablar de chanteo.\033[0m
El chanteo es un concepto muy importante dentro del trap y el reguetón en el contexto del fronteo. 
Se refiere a un estilo de rap o letra que transmite confianza, arrogancia, y superioridad. Los artistas que hacen chanteo generalmente hablan de su éxito, su riqueza, su poder, y su capacidad para dominar la escena. 
También se puede referir a la forma en que un artista se vende a sí mismo como el más grande, usando una actitud desafiante que dice soy el mejor o soy imparable🐙🔥.\n
"""

RESPUESTA_FRONTEO = """\033[1mAl parecer quieres hablar de fronteo.\033[0m
El fronteo es uno de los términos más representativos del género urbano, especialmente dentro del trap, el reguetón, y la música de la calle. 
Se trata de una actitud, una forma de ser y una cultura que va más allá de lo musical. Es una manifestación de poder, estatus y dominancia sobre otros. 
A diferencia del chanteo, que se refiere más a las letras con actitud desafiante, el fronteo abarca todo lo que tiene que ver con la demostración de lo que uno tiene o puede hacer, sobre todo en el contexto de la calle y el éxito🏰😎.\n
"""

RESPUESTA_GENERO_URBANO = """\033[1mAl parecer quieres hablar de género urbano.\033[0m
El género urbano es una categoría musical que engloba una variedad de estilos y subgéneros, todos influenciados por las culturas urbanas y las experiencias de vida en las ciudades, particularmente en contextos de estratificación social y lucha. 
Es un término amplio que abarca estilos musicales originados principalmente en Latinoamérica y los Estados Unidos, influenciados por los ritmos y sonidos africanos, latinos y caribeños, y que se ha transformado y fusionado con otros géneros como el rap, el reguetón, el trap, la salsa, el dancehall, y el hip-hop🎵🔥.\n
"""

RESPUESTA_ARTISTAS_CHANTEO = """\033[1mArtistas destacados del chanteo:\033[0m
·Bad Bunny: Aunque tiene muchas facetas, una de las más fuertes de Bad Bunny es su capacidad para crear letras llenas de chanteo, celebrando su éxito y su superioridad.
·Anuel AA: Famoso por su estilo de chanteo agresivo, hablando de su dominancia en la industria y en la calle.
·Eladio Carrión: Su flow agresivo y sus letras de chanteo lo han consolidado como uno de los grandes del trap.
·Myke Towers: Aunque su estilo tiene más suavidad, también se caracteriza por el chanteo, mostrando su ascenso y superioridad.
·Arcángel: El Jefe siempre ha sido uno de los pioneros del chanteo, con letras que reflejan poder y estatus🎶.\n
"""

RESPUESTA_ARTISTAS_FRONTEO = """\033[1mArtistas destacados del fronteo:\033[0m
·Anuel AA: Es uno de los grandes exponentes del fronteo. Su actitud de "yo soy el más duro" y sus líricas agresivas sobre su vida de lujo y superioridad son claves en su carrera.
·Yovngchimi: Es un joven que se ha ido haciendo un nombre por su actitud de fronteo, con letras que hablan de cómo ha llegado hasta donde está y de superar a los demás.
·Ovi: Representa la mezcla del fronteo con el chanteo, demostrando cómo superó la calle y mostrando lo que ha ganado, pero con una actitud de humildad y orgullo al mismo tiempo.
·Hades66: Representa el fronteo más puro y crudo, siempre mostrando que tiene todo lo que otros desean. Con sus letras llenas de confianza y provocación, no duda en demostrar que está a otro nivel🤑.\n
"""
 
RESPUESTA_ARTISTAS_GENERO_URBANO = """\033[1mLíderes del género urbano:\033[0m
·Bad Bunny: Siempre a la vanguardia del género, Bad Bunny es un líder indiscutido, fusionando trap, reguetón y otros estilos.
·Anuel AA: Uno de los grandes exponentes del trap y el fronteo.
·J Balvin: Un ícono del reguetón y la cultura urbana global.
·Karol G: La reina del reguetón femenino sigue marcando la pauta con su estilo.
·Ozuna: Ha consolidado su imperio urbano con música que mezcla trap, reguetón y R&B😎.\n
"""

RESPUESTA_FUTUROS_CHANTEO = """\033[1mMi prediccion sobre futuros artistas del chanteo es que serán:\033[0m
·Dei V: Joven talento con un estilo fresco de chanteo y letras de autoafirmación.
·Clarent: Con letras de superioridad y un flow potente, está ganando fuerza en la escena.
·Yan Block es un artista emergente del chanteo y trap, destacado por su flow agresivo y letras de poder, ganando popularidad rápidamente.
Mi prediccion puede ser erronea pero apostaria por que eston seran los futuros artistas🌟🔥.\n
"""

RESPUESTA_FUTUROS_FRONTEO = """\033[1mMi prediccion sobre futuros artistas del fronteo es que serán:\033[0m
·Yovngchimi: Con su flow melódico y letras de poder, se perfila como una estrella emergente.
·Hades66: Mezcla de trap y fronteo, con letras poderosas y actitud desafiante.
·Ovi: Con un flow agresivo y letras de realismo callejero, está marcando tendencia.
Mi prediccion puede ser erronea pero apostaria por que eston seran los futuros artistas🎵🌟.\n
"""

RESPUESTA_FUTUROS_GENERO_URBANO = """\033[1mMi prediccion sobre futuros artistas del genero urbano es que serán:\033[0m
·Dei V: Joven talento del trap y chanteo, conocido por su estilo fresco y letras de autoafirmación.
·Eladio Carrión: es un influyente artista del trap, fronteo y reguetón, conocido por su capacidad de evolucionar y dominar la escena urbana.
·Yan Block es un artista emergente del chanteo y trap, destacado por su flow agresivo y letras de poder, ganando popularidad rápidamente.
Mi prediccion puede ser erronea pero apostaria por que eston seran los futuros artistas🔥🌟.\n
"""

RESPUESTA_RAP = """\033[1mVeo que quieres saber que es el rap, pero antes dejame decirte que no me especializo en ese medio.\033[0m
El rap es un estilo musical que nace como parte de la cultura hip-hop en los años 70 en Estados Unidos, caracterizado por su forma de expresión rítmica y poética hablada, conocida como rima o chanteo. Se fundamenta en tres elementos principales: el flow (ritmo y cadencia de las palabras), las letras (contenido lírico que puede ser personal, social o narrativo) y el beat (la base instrumental que marca el ritmo)🎤.\n
"""

RESPUESTA_REGUETON = """\033[1mVeo que quieres saber que es el regueton, pero antes dejame decirte que no me especializo en ese medio.\033[0m
El reguetón es un género musical originado en Puerto Rico en los años 90, que combina influencias del dancehall, hip-hop y cumbia, con un énfasis en el ritmo y las bases electrónicas. Su sonido distintivo está marcado por el característico dem-bow, un ritmo repetitivo que proviene de la música dancehall jamaicana.🕺\n
"""
RESPUESTA_DEMBOW = """\033[1mVeo que quieres saber que es el dembow, pero antes dejame decirte que no me especializo en ese medio.\033[0m
El dembow es un género musical nacido en la República Dominicana, caracterizado por su ritmo acelerado, repetitivo y altamente bailable. Surge como una evolución del dancehall jamaicano, mezclado con influencias del reguetón, el hip-hop y la música urbana dominicana. Es conocido por su energía intensa y letras que suelen ser pegajosas, humorísticas o con temas sociales🕺.\n
"""


respuestas = { 
    "prediccion artistas del chanteo": RESPUESTA_FUTUROS_CHANTEO, 
    "prediccion artistas del fronteo": RESPUESTA_FUTUROS_FRONTEO, 
    "prediccion artistas del género urbano": RESPUESTA_FUTUROS_GENERO_URBANO,
    "futuros artistas del chanteo": RESPUESTA_FUTUROS_CHANTEO,
    "futuros artistas del fronteo": RESPUESTA_FUTUROS_FRONTEO,
    "futuros artistas del género urbano": RESPUESTA_FUTUROS_GENERO_URBANO,
    "artistas del chanteo": RESPUESTA_ARTISTAS_CHANTEO,
    "artistas del fronteo": RESPUESTA_ARTISTAS_FRONTEO,
    "artistas del género urbano": RESPUESTA_ARTISTAS_GENERO_URBANO,
    "chanteo": RESPUESTA_CHANTEO,
    "fronteo": RESPUESTA_FRONTEO,
    "genero urbano": RESPUESTA_GENERO_URBANO,
    "rap": RESPUESTA_RAP,
    "reguetón": RESPUESTA_REGUETON,
    "dembow": RESPUESTA_DEMBOW
}

def reconocer_palabras_clave(texto):
    texto = texto.lower() 
    for clave, respuesta in respuestas.items():
        if clave in texto: 
            return respuesta 
    return "Lo siento, no tengo información sobre ese tema. Intenta hablar de chanteo, fronteo, género urbano o artistas relacionados, lo lamento 😥."# Si no se encuentra ninguna clave dice que no tiene información sobre ese tema
        

def nombre_saludar():
    nombre = input("Yo me llamo GlizzyBot💰, y soy el encargado de estar al tanto de todo lo que ocurre en el mundo de la música urbana.\033[1mSi quieres saber mas sobre lo que puedo hacer preguntamelo. ej(que puedes hacer?)\033[0m\n ¿Por cierto, tú cómo te llamas? \n").strip()
    while not nombre:  
        nombre = input("Por favor, dime tu nombre para poder continuar 🙏.\n").strip()
    
    print(f"¡Perfecto, {nombre}!")
    return nombre

def continuar_conversacion(nombre):  
    """Continúa la conversación con el usuario."""
    while True:
    
        frases = [
            f"{nombre}, ¿Qué más querrías saber? (Escribe 'no' para terminar): ", 
            f"{nombre}, ¿De qué más te gustaría hablar? (Escribe 'no' para terminar): ", 
            f"{nombre}, ¿De qué te gustaría hablar? (Escribe 'no' para terminar): "
        ]
        pregunta = random.choice(frases)  
        tema = input(pregunta).strip()  

        if tema.lower() in [
            "que haces?", "que haces", "que puedes hacer?", "que puedes hacer", 
            "que sabes hacer?", "que sabes hacer", "en que te enfocas?", "en que te enfocas"
        ]:
            print(
                "Soy GlizzyBot, el rey del fronteo🔥. Estoy aquí para proporcionarte información "
                "sobre chanteo, fronteo y todo lo relacionado con el género urbano. "
                "Puedo darte información sobre artistas, predecir quiénes serán las futuras estrellas "
                "y ofrecer datos sobre géneros que no domino tanto🌟. ¡Espero poder ayudarte!\n"
            )
            continue  

        if tema.lower() == "no":
            print("Estuviste hablando con el rey del fronteo🔥. Espero que hayas aprendido algo nuevo. ¡Nos vemos, chau!👋")
            break 
        if not tema:
            print("Por favor, escribe algo válido.")
            continue 

       
        respuesta = reconocer_palabras_clave(tema)
        print(respuesta)

def main():
    nom = nombre_saludar()
    continuar_conversacion(nom)
