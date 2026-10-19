import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Identidad de Marca - Yamileth Ospino",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main-title {
        color: #2E4A3D;
        font-size: 2.3rem;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #557A68;
        font-size: 1.2rem;
        font-weight: 400;
        margin-bottom: 20px;
    }
    .highlight-box {
        background-color: #F0F4F1;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E4A3D;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Menú lateral
st.sidebar.title("Navegación")
opcion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "0. Vista General",
        "01. Hallazgo Estratégico",
        "02. Visión y Misión",
        "03. Valores de Marca",
        "04. Personalidad de Marca",
        "05. Territorio Conceptual",
        "06. Manifiesto",
        "07. Posicionamiento",
        "08. Tono y Lenguaje",
        "09. Síntesis"
    ]
)

# Encabezado Principal
st.markdown("<h1 class='main-title'>IDENTIDAD DE MARCA</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Yamileth Ospino · Psicología y acompañamiento a lo largo de la vida</h3>", unsafe_allow_html=True)
st.divider()

# --- 0. VISTA GENERAL ---
if opcion == "0. Vista General":
    st.markdown("<div class='highlight-box'><b>Idea estratégica central:</b><br><i>El bienestar se construye a lo largo de la vida.</i></div>", unsafe_allow_html=True)
    st.write("Documento de trabajo que sintetiza la propuesta de identidad estratégica. Su propósito es servir como base para validar la esencia, el posicionamiento y la futura expresión visual y verbal de la marca.")
    
    st.subheader("Contenido")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * **01.** Hallazgo estratégico
        * **02.** Visión y misión
        * **03.** Valores de marca
        * **04.** Personalidad de marca
        * **05.** Territorio conceptual
        """)
    with col2:
        st.markdown("""
        * **06.** Manifiesto
        * **07.** Posicionamiento
        * **08.** Tono y lenguaje
        * **09.** Síntesis
        """)

# --- 01. HALLAZGO ESTRATÉGICO ---
elif opcion == "01. Hallazgo Estratégico":
    st.header("01. Hallazgo estratégico")
    st.write("Yamileth entiende la psicología no únicamente como una intervención cuando aparece un problema, sino como un acompañamiento que puede aportar en distintas etapas y circunstancias de la vida. La propuesta combina escucha sin juicio, preparación profesional, orientación y herramientas para que cada persona pueda comprender mejor lo que vive y tomar sus propias decisiones.")
    
    st.subheader("Los cuatro pilares")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Escucha sin juicio:** crear un espacio en el que la persona pueda expresarse con confianza y respeto.")
        st.info("**Conocimiento profesional:** sostener el acompañamiento en preparación, actualización y responsabilidad ética.")
    with col2:
        st.info("**Autonomía y orientación:** facilitar comprensión y herramientas, sin imponer respuestas ni decidir por la persona.")
        st.info("**Prevención y continuidad:** reconocer que el cuidado psicológico puede ser relevante antes de una crisis y a lo largo de la vida.")

# --- 02. VISIÓN Y MISIÓN ---
elif opcion == "02. Visión y Misión":
    st.header("02. Visión y misión")
    
    st.subheader("Visión propuesta")
    st.caption("Hacia dónde quiere contribuir la marca")
    st.markdown("<div class='highlight-box'>Contribuir a una sociedad que reconozca la salud mental como parte esencial del bienestar durante toda la vida, donde las personas puedan acceder a acompañamiento psicológico oportuno y desarrollar herramientas para afrontar sus desafíos y vivir con mayor bienestar.</div>", unsafe_allow_html=True)
    
    st.subheader("Misión propuesta")
    st.caption("Qué ofrece y cómo lo hace")
    st.markdown("<div class='highlight-box'>Brindar acompañamiento psicológico profesional, empático y basado en evidencia, que permita a las personas comprender sus pensamientos y emociones, afrontar los desafíos de las distintas etapas de la vida y desarrollar herramientas para tomar sus propias decisiones y mejorar su bienestar.</div>", unsafe_allow_html=True)

# --- 03. VALORES DE MARCA ---
elif opcion == "03. Valores de Marca":
    st.header("03. Valores de marca")
    valores = {
        "Empatía y respeto": "Escuchar con atención, reconocer la historia de cada persona y evitar juicios o etiquetas.",
        "Ética y autonomía": "Cuidar la confidencialidad y los límites profesionales, respetando la capacidad de cada persona para decidir.",
        "Rigor y aprendizaje continuo": "Mantener una práctica responsable, fundamentada en el conocimiento y abierta a la actualización.",
        "Autonomía y empoderamiento": "Ofrecer orientación y herramientas para que las personas comprendan su situación y puedan tomar decisiones propias.",
        "Prevención y continuidad": "Promover una mirada del bienestar psicológico que no se limite a responder a una crisis puntual."
    }
    for val, desc in valores.items():
        with st.expander(f"📌 {val}", expanded=True):
            st.write(desc)

# --- 04. PERSONALIDAD DE MARCA ---
elif opcion == "04. Personalidad de Marca":
    st.header("04. Personalidad de marca")
    st.write("La marca puede expresarse como una profesional cercana y confiable, con calidez humana y una base científica clara. La cercanía debe transmitir seguridad sin borrar los límites del vínculo profesional.")
    
    st.markdown("""
    * **Cercana, no excesivamente informal:** humana y accesible, sin confundirse con una relación de amistad.
    * **Científica, no fría:** demuestra preparación y criterio, explicando con claridad y sensibilidad.
    * **Reflexiva, no impositiva:** invita a comprender y explorar, sin decirle a la persona cómo debe vivir.
    * **Profesional, no rígida:** transmite confianza y estructura sin recurrir a un lenguaje institucional distante.
    * **Metódica y contemporánea:** proyecta orden, actualización y apertura a distintas realidades.
    """)

# --- 05. TERRITORIO CONCEPTUAL ---
elif opcion == "05. Territorio Conceptual":
    st.header("05. Territorio conceptual")
    
    st.subheader("Territorio principal recomendado")
    st.markdown("<div class='highlight-box'><b>El bienestar se construye a lo largo de la vida</b><br>Este territorio permite hablar de desarrollo, cambios, prevención, aprendizaje y continuidad. Amplía la percepción de la psicología más allá de la crisis y puede dar coherencia a una práctica que acompaña distintas etapas.</div>", unsafe_allow_html=True)
    
    st.subheader("Territorios complementarios")
    st.markdown("""
    * **Un espacio para comprender y avanzar:** Expresa la experiencia que la persona puede encontrar: escucha, confianza, claridad, herramientas y autonomía.
    * **Ciencia que acompaña:** Comunica la unión entre conocimiento profesional, humanidad y confianza.
    """)
    
    st.subheader("Arquitectura conceptual sugerida")
    tabla_arq = [
        {"Nivel": "Centro", "Función": "Define la visión amplia", "Idea": "El bienestar se construye a lo largo de la vida"},
        {"Nivel": "Experiencia", "Función": "Describe cómo se siente el acompañamiento", "Idea": "Un espacio para comprender y avanzar"},
        {"Nivel": "Fundamento", "Función": "Explica por qué confiar", "Idea": "Ciencia que acompaña"}
    ]
    st.table(tabla_arq)

# --- 06. MANIFIESTO ---
elif opcion == "06. Manifiesto":
    st.header("06. Manifiesto de marca")
    st.markdown("""
    > **La salud mental importa en cada etapa de la vida.**
    > 
    > Creemos que cuidar la salud mental no debería ser el último recurso cuando sentimos que ya no podemos más. Todas las personas atraviesan cambios, decisiones y momentos que pueden transformar su manera de pensar, sentir y vivir. No tenemos que recorrerlos sin apoyo.
    > 
    > Acompañar no significa decirle a alguien cómo vivir. Significa escuchar sin juzgar, comprender su historia, ofrecer herramientas y ayudarle a encontrar claridad para tomar sus propias decisiones.
    > 
    > Creemos en una psicología profesional, fundamentada en el conocimiento y ejercida con empatía, respeto y responsabilidad. Una psicología que reconoce a la persona más allá de sus dificultades y que comprende que su bienestar también está relacionado con su historia, su entorno y sus vínculos.
    > 
    > Queremos contribuir a que pedir ayuda sea una posibilidad y no un motivo de vergüenza; a que el cuidado psicológico pueda comenzar antes de una crisis y continuar a lo largo de la vida.
    > 
    > Porque cada persona merece ser escuchada, comprendida y acompañada con respeto.
    > 
    > **El bienestar también se construye. Y no tenemos que hacerlo a solas.**
    """)

# --- 07. POSICIONAMIENTO ---
elif opcion == "07. Posicionamiento":
    st.header("07. Posicionamiento")
    
    st.subheader("Declaración de posicionamiento propuesta")
    st.markdown("<div class='highlight-box'>Para las personas que buscan comprender lo que están viviendo y desarrollar herramientas para afrontar los desafíos de la vida, Yamileth Ospino ofrece acompañamiento psicológico cercano, profesional y fundamentado en el conocimiento, que combina escucha sin juicio, orientación y una visión integral de la persona.</div>", unsafe_allow_html=True)
    
    st.write("La promesa no es resolver la vida de la persona ni garantizar resultados rápidos; es ofrecer un espacio profesional para comprender, explorar opciones y desarrollar recursos propios.")

# --- 08. TONO Y LENGUAJE ---
elif opcion == "08. Tono y Lenguaje":
    st.header("08. Tono y lenguaje")
    
    tabla_tono = [
        {"Dimensión": "Cercanía", "Cómo se expresa": "Cálida, respetuosa y accesible", "Evitar": "Exceso de confianza o familiaridad"},
        {"Dimensión": "Claridad", "Cómo se expresa": "Palabras sencillas, ideas concretas", "Evitar": "Tecnicismos innecesarios o frases ambiguas"},
        {"Dimensión": "Profesionalismo", "Cómo se expresa": "Conocimiento explicado con claridad", "Evitar": "Tono frío, rígido o excesivamente institucional"},
        {"Dimensión": "Reflexión", "Cómo se expresa": "Preguntas que invitan a comprender", "Evitar": "Imponer conclusiones o dar lecciones"},
        {"Dimensión": "Esperanza realista", "Cómo se expresa": "Hablar de posibilidades, herramientas y procesos", "Evitar": "Promesas de cambio inmediato o frases motivacionales vacías"}
    ]
    st.table(tabla_tono)
    
    st.subheader("Ejemplos de lenguaje")
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Preferible:**\n- “Podemos explorar lo que estás viviendo y las herramientas que podrían ayudarte”.\n- “Pedir apoyo también puede ser una forma de cuidarte”.")
    with col2:
        st.error("**Evitar:**\n- “Te voy a decir qué tienes que hacer”.\n- “Vas a cambiar tu vida en pocas sesiones”.")

# --- 09. SÍNTESIS ---
elif opcion == "09. Síntesis":
    st.header("09. Síntesis y decisiones por validar")
    
    st.subheader("Propuesta de síntesis")
    tabla_sintesis = [
        {"Elemento": "Visión", "Propuesta": "Una sociedad que reconozca la salud mental en todas las etapas de la vida."},
        {"Elemento": "Misión", "Propuesta": "Acompañamiento profesional, empático y fundamentado en conocimiento."},
        {"Elemento": "Valores", "Propuesta": "Empatía, ética, rigor, autonomía, prevención y continuidad."},
        {"Elemento": "Personalidad", "Propuesta": "Cercana, reflexiva, científica, metódica y confiable."},
        {"Elemento": "Concepto", "Propuesta": "El bienestar se construye a lo largo de la vida."},
        {"Elemento": "Manifiesto", "Propuesta": "La salud mental importa en cada etapa de la vida."},
        {"Elemento": "Posicionamiento", "Propuesta": "Acompañamiento cercano y profesional, con escucha, orientación y herramientas."},
        {"Elemento": "Tono", "Propuesta": "Cercano sin exceso de informalidad; científico sin frialdad; claro sin simplificar en exceso."}
    ]
    st.table(tabla_sintesis)