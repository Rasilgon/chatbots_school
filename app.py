from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# Simulació de "chatbots" i els seus codis
chatbot_list = {f"Chatbot {i+1}": f"def chatbot_{i+1}():\n    return 'Aquest és el codi del chatbot {i+1}'"
                for i in range(20)}

# Crear l'aplicació
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Necessari per Gunicorn

app.title = "Els chatbots de Vinyes Velles"

# Disseny de la interfície d'usuari
app.layout = html.Div([
    html.H1("Els chatbots de Vinyes Velles", style={'textAlign': 'center'}),
    
    # Menú desplegable per seleccionar un chatbot
    html.Div([
        html.Label("Selecciona un chatbot:"),
        dcc.Dropdown(
            id='chatbot-dropdown',
            options=[{'label': bot, 'value': bot} for bot in chatbot_list.keys()],
            value='Chatbot 1',
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
        html.H3("Codi del chatbot:"),
        html.Pre(id='chatbot-code', style={'border': '1px solid #ccc', 'padding': '10px'}),
    ], style={'width': '80%', 'margin': '0 auto'}),
])

# Lògica del servidor
@app.callback(
    [Output('chat-output', 'children'), Output('chatbot-code', 'children')],
    [Input('send-button', 'n_clicks'), Input('chatbot-dropdown', 'value')],
    [State('chat-input', 'value')]
)
def interact_with_chatbot(n_clicks, selected_bot, user_message):
    # Simula una resposta del chatbot
    if user_message:
        chatbot_response = f"{selected_bot} respon: Hola! Has dit: '{user_message}'"
    else:
        chatbot_response = f"{selected_bot} està esperant el teu missatge."
    
    # Mostra el codi del chatbot seleccionat
    chatbot_code = chatbot_list[selected_bot]
    
    return chatbot_response, chatbot_code

# Executar l'aplicació en mode local
if __name__ == "__main__":
    app.run_server(debug=True)
