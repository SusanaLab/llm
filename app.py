from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def asistente_escritura(texto_usuario):
    respuesta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente que mejora redacción y genera texto claro."},
            {"role": "user", "content": texto_usuario}
        ]
    )
    return respuesta.choices[0].message.content


if __name__ == "__main__":
    print("=== Asistente de escritura ===")
    
    texto = input("Escribe tu idea: ")
    resultado = asistente_escritura(texto)
    
    print("\nResultado:\n")
    print(resultado)