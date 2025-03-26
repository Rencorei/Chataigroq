from groq import Groq

client = Groq(api_key="api_key") #Reemplazar por tu API Key
conversacion=[
        {
            "role": "system",
            "content": "Abi, asistente virtual, responde de manera breve." #Perfil o rol q tomara el modelo
        }
    ]
print("\033[1;92m\nAbi: Soy Abi tu asistente virtual, en que puedo ayudarte?\033[0m")

while True:
    msj = input("\nTú: ")
    if msj.lower() == "salir":
        print("Un gusto haberte atendido, hasta luego!")
        break
    conversacion.append({"role": "user", "content": msj})

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",#Puedes reemplazarlo por cualquier modelo de Groq
        messages=conversacion,
        temperature=0.6, #Rango de 0 a 1, entre mas alto mas creativo
        max_completion_tokens=4180, #Tamaño maximo de la respuesta
        top_p=0.95, 
        stream=True,
        stop=None,
    )
    
    print("\033[1;92m\nAbi: ", end=" ")
    respuesta=""
    for chunk in completion:
        texto=chunk.choices[0].delta.content or ""
        print(f"\033[1;92m{texto}\033[0m", end="")
        respuesta+=texto

    conversacion.append({"role": "assistant", "content": respuesta})

