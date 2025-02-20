import openai

def get_car_ai_bio(model, brand, year):
    client = openai.OpenAI(api_key="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")

    prompt = f"Me mostre uma descrição do carro modelo {model} da marca {brand} do ano {year} em apenas 250 caracteres."

    response = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=250
    )

    return response.choices[0].text

