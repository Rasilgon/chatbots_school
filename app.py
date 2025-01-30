import importlib
import os
import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# **Llista de chatbots disponibles**
CHATBOTS_DIR = "chatbots"
chatbots_disponibles = {f[:-3]: f[:-3] for f in os.listdir(CHATBOTS_DIR) if f.endswith(".py")}

# **Crear aplicació Dash**
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # ✨ Necessari per Render

app.layout = html.Div([
    html.H1("Els chatbots de Vinyes Velles", style={'textAlign': 'center'}),

    html.Label("Selecciona un chatbot:"),
    dcc.Dropdown(
        id='chatbot-dropdown',
        options=[{'label': name, 'value': name} for name in chatbots_disponibles.keys()],
        value=list(chatbots_disponibles.keys())[0],  
        clearable=False
    ),

    html.Hr(),

    html.H3("Interacció amb el chatbot:"),
    dcc.Textarea(
        id='chat-input',
        placeholder="Escriu el teu missatge aquí...",
        style={'width': '100%', 'height': '100px'}
    ),
    html.Button('Enviar', id='send-button', n_clicks=0, style={'margin-top': '10px'}),
    html.Div(id='chat-output', style={'border': '1px solid #ccc', 'padding': '10px', 'margin-top': '20px'}),

    html.Hr(),

    html.H3("Codi del chatbot seleccionat:"),
    html.Pre(id='chatbot-code', style={'border': '1px solid #ccc', 'padding': '10px', 'whiteSpace': 'pre-wrap'}),
])

def carregar_chatbot(nom_chatbot):
    """
    Carrega un chatbot des de la carpeta 'chatbots/' i retorna el seu mòdul.
    """
    try:
        module_path = f"{CHATBOTS_DIR}.{nom_chatbot}"
        chatbot_module = importlib.import_module(module_path)
        return chatbot_module
    except ModuleNotFoundError:
        return None

@app.callback(
    Output('chat-output', 'children'),
    [Input('send-button', 'n_clicks')],
    [State('chatbot-dropdown', 'value'), State('chat-input', 'value')]
)
def interactuar_amb_chatbot(n_clicks, nom_chatbot, missatge_usuari):
    if n_clicks == 0 or not missatge_usuari:
        return ""

    chatbot = carregar_chatbot(nom_chatbot)
    if chatbot and hasattr(chatbot, 'main'):
        resposta = chatbot.main(missatge_usuari)
        return resposta
    return "Error: No s'ha pogut carregar el chatbot."

@app.callback(
    Output('chatbot-code', 'children'),
    [Input('chatbot-dropdown', 'value')]
)
def mostrar_codi_chatbot(nom_chatbot):
    try:
        with open(f"{CHATBOTS_DIR}/{nom_chatbot}.py", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: No s'ha trobat el fitxer del chatbot."

if __name__ == "__main__":
    app.run_server(debug=True)
