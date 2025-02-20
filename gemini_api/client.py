import google.generativeai as genai 

# Configure a chave da API globalmente (faça isso uma única vez na inicialização do app)
genai.configure(api_key="AIzaSyDMEOFR_wzbkKAg3_f_gHEx66Pi5pCoeII")

def get_car_ai_bio(model, brand, year):
    # Inicializa o modelo corretamente
    model_gen = genai.GenerativeModel("gemini-2.0-flash")

    # Define o prompt
    prompt = f"Você agora é um vendedor de automóveis experiente. Me mostre uma descrição do carro modelo {model} da marca {brand} do ano {year} em até 502 caracteres."

    # Gera o conteúdo
    response = model_gen.generate_content(prompt)

    if response.candidates and response.candidates[0].content.parts:
        return response.candidates[0].content.parts[0].text.strip()
    
    return "Erro ao gerar a descrição do carro."

