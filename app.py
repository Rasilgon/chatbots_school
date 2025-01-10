from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# Llista de chatbots amb noms i descripcions
chatbots = {
    "ChatBotPy": "parla sobre qualsevol cosa",
    "FutBot": "parla de futbol",
    "Cabechat": "parla sobre el bàsquet i és dels Warriors",
    "Walter": "parla sobre el Barça",
    "Hades": "sobre música del gènere urbà 2024",
    "Thebot": "pot ampliar el teu coneixement sobre qualsevol religió",
    "SantiBot": "t'ajuda amb teoria musical i composició",
    "RossoX": "parla sobre F1 i li agrada Ferrari",
    "LuisMarioBot": "parla sobre futbol",
    "Turkobot": "t’ajuda a triar sèries turques",
    "DeciBot": "t’ajuda a prendre decisions",
    "Eco": "parla de futbol",
    "Neobot": "parla sobre tennis",
    "ArtBot": "parla sobre obres d’art",
    "RumaBot": "parla sobre bàsquet",
    "MisterMarlet": "parla sobre atletisme",
}

# Crear l'aplicació
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.title = "Els chatbots de Vinyes Velles"

# Disseny de la interfície d'usuari
app.layout = html.Div([
    html.H1("Els chatbots de Vinyes Velles", style={'textAlign': 'center'}),

    # Menú desplegable per seleccionar un chatbot
    html.Div([
        html.Label("Selecciona un chatbot:"),
        dcc.Dropdown(
            id='chatbot-dropdown',
            options=[{'label': name, 'value': name} for name in chatbots.keys()],
            value='ChatBotPy',
            clearable=False
        ),
    ], style={'width': '50%', 'margin': '0 auto'}),

    html.Hr(),

    # Zona d'interacció amb el chatbot
    html.Div([
        html.H3("Interacció amb el chatbot:"),
        dcc.Textarea(
            id='chat-input',
            placeholder='Escriu el teu missatge aquí...',
            style={'width': '100%', 'height': '100px'}
        ),
        html.Button('Enviar', id='send-button', n_clicks=0, style={'margin-top': '10px'}),
        html.Div(id='chat-output', style={'border': '1px solid #ccc', 'padding': '10px', 'margin-top': '20px'}),
    ], style={'width': '80%', 'margin': '0 auto'}),

    html.Hr(),

    # Mostra el codi del chatbot seleccionat
    html.Div([
        html.H3("Descripció del chatbot seleccionat:"),
        html.Pre(id='chatbot-description', style={'border': '1px solid #ccc', 'padding': '10px'}),
    ], style={'width': '80%', 'margin': '0 auto'}),
])

# Lògica del servidor
@app.callback(
    [Output('chat-output', 'children'), Output('chatbot-description', 'children')],
    [Input('send-button', 'n_clicks'), Input('chatbot-dropdown', 'value')],
    [State('chat-input', 'value')]
)
def interact_with_chatbot(n_clicks, selected_bot, user_message):
    # Missatge de benvinguda i interacció
    chatbot_response = f"{selected_bot} diu: Hola! {chatbots[selected_bot]}"
    if user_message:
        chatbot_response += f"\nHas dit: '{user_message}'"

    # Descripció del chatbot seleccionat
    chatbot_description = f"Nom: {selected_bot}\nDescripció: {chatbots[selected_bot]}"

    return chatbot_response, chatbot_description

# Executar l'aplicació en mode local
if __name__ == "__main__":
    app.run_server(debug=True)
