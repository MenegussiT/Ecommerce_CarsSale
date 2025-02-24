import google.generativeai as genai 

genai.configure(api_key="AIzaSyDMEOFR_wzbkKAg3_f_gHEx66Pi5pCoeII")

def get_car_ai_bio(model, brand, year):
    model_gen = genai.GenerativeModel("gemini-2.0-flash")

    
    prompt = f" Me mostre uma descrição do carro modelo {model} da marca {brand} do ano {year} em até 502 caracteres de forma técnica e objetiva, sem o uso de ásteristico para negrito ou coisas parecidas."

    response = model_gen.generate_content(prompt)

    if response.candidates and response.candidates[0].content.parts:
        return response.candidates[0].content.parts[0].text.strip()
    
    return "Erro ao gerar a descrição do carro."

