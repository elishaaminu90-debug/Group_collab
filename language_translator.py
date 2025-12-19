def run():
    D = {
        "hello": {
            "yoruba": "Bawo",
            "tiv": "Msugh",
            "urhobo": "Mavo",
            "igala": "Agba",
            "igbo": "Ndeewo"
        },
        "goodbye": {
            "yoruba": "O dabo",
            "tiv": "Msugh u",
            "urhobo": "Kude",
            "igala": "Ola ojo",
            "igbo": "Ka o di"
        },
        "please": {
            "yoruba": "E jowo",
            "tiv": "Zaar",
            "urhobo": "Biko",
            "igala": "Abele",
            "igbo": "Biko"
        },
        "thank you": {
            "yoruba": "E se",
            "tiv": "Msugh",
            "urhobo": "Wekobiruo",
            "igala": "Agba",
            "igbo": "Daalu"
        },
        
        "house": {
            "yoruba": "Ile",
            "tiv": "Ya",
            "urhobo": "Uwevwin",
            "igala": "Unyi",
            "igbo": "Ulo"
        },
        "car": {
            "yoruba": "Oko",
            "tiv": "Mato",
            "urhobo": "Imoto",
            "igala": "Imoto",
            "igbo": "Ugbo ala"
        },
        "water": {
            "yoruba": "Omi",
            "tiv": "Mnger",
            "urhobo": "Ame",
            "igala": "Omi",
            "igbo": "Mmiri"
        },
        "food": {
            "yoruba": "Ounje",
            "tiv": "Kwaghgyan",
            "urhobo": "Emo",
            "igala": "Onje",
            "igbo": "Nri"
        },
        "book": {
            "yoruba": "Iwe",
            "tiv": "Takerada",
            "urhobo": "Obe",
            "igala": "Otakada",
            "igbo": "Akwukwo"
        },
        "pen": {
            "yoruba": "Kalamu",
            "tiv": "Jokol",
            "urhobo": "Ukeke",
            "igala": "Kalamu",
            "igbo": "Pen"
        },
        "school": {
            "yoruba": "Ile-iwe",
            "tiv": "Fada",
            "urhobo": "Isikuru",
            "igala": "Unkoche",
            "igbo": "Ulo akwukwo"
        },
        "family": {
            "yoruba": "Ebi",
            "tiv": "Tsombor",
            "urhobo": "Ekru",
            "igala": "Abogjo",
            "igbo": "Ezi na ulo"
        },
        "friend": {
            "yoruba": "Ore",
            "tiv": "Ijua",
            "urhobo": "Ogbesu",
            "igala": "Omule",
            "igbo": "Enyi"
        },
        "love": {
            "yoruba": "Ife",
            "tiv": "Dooshima",
            "urhobo": "Guono",
            "igala": "Ufedo",
            "igbo": "Hunanya"
        },
        "happy": {
            "yoruba": "Inu didun",
            "tiv": "Saana",
            "urhobo": "Oghogho",
            "igala": "Ayoyo",
            "igbo": "Obi uto"
        },
        "sad": {
            "yoruba": "Ibaniuje",
            "tiv": "Achi",
            "urhobo": "Uweri",
            "igala": "Edoji",
            "igbo": "Iwe"
        }
    }

    L = ["yoruba", "tiv", "urhobo", "igala", "igbo"]

    print(" Hello ")

    name = input("what your name: ").strip()
    print(f"Hi, {name}" )

    while True:
        print("Words I know:")

        W = list(D.keys())

        print(" , " .join(W))

        W_choice = input("\nPick a word (or type 'exit'): ").strip().lower()

        if W_choice == 'exit':
            print("Bye bye,", (name))
            break

        if W_choice not in D:
            print("I don't know that word. Try again.")
            continue

        print("\nLanguages are: {0}".format(', '.join(L)))

        L_choice = input("Pick a language: ").lower()

        if L_choice not in L:
            print("I don't know that language. Try again.")
            continue

        T = D[W_choice][L_choice]

        print("\nResult: {0} in {1} is {2}".format(
            W_choice,
            L_choice,
            T
        ))
        print("-")


run()
