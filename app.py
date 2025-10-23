import streamlit as st
from textblob import TextBlob
from googletrans import Translator


translator = Translator()


st.title("🪶 Análisis de Sentimientos con TextBlob")


st.subheader("Escribe una frase para analizar su polaridad y subjetividad:")


with st.sidebar:
    st.header("📊 Guía de interpretación")
    st.markdown("""
    **Polaridad:**  
    Indica si el sentimiento del texto es positivo, negativo o neutral.  
    -1 → Muy negativo 😔  
     0 → Neutral 😐  
     1 → Muy positivo 😊  

    **Subjetividad:**  
    Mide cuánto del texto expresa **opiniones o emociones** (subjetivo)  
    frente a **hechos o datos** (objetivo).  
    0 → Totalmente objetivo  
    1 → Totalmente subjetivo
    """)


with st.expander("🔍 Analizar Polaridad y Subjetividad"):
    text1 = st.text_area("✏️ Escribe aquí tu texto en español:")
    
    if text1:
      
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        
   
        blob = TextBlob(trans_text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        

        st.write("### 📈 Resultados del análisis:")
        st.write(f"**Polaridad:** {polarity}")
        st.write(f"**Subjetividad:** {subjectivity}")
        
       
        if polarity >= 0.5:
            st.success("El texto expresa un **sentimiento positivo** 😊")
        elif polarity <= -0.5:
            st.error("El texto expresa un **sentimiento negativo** 😔")
        else:
            st.info("El texto expresa un **sentimiento neutral** 😐")


with st.expander("📝 Corrección ortográfica (en inglés)"):
    text2 = st.text_area("✏️ Escribe tu texto en inglés:", key="4")
    
    if text2:
        blob2 = TextBlob(text2)
        corrected = blob2.correct()
        st.write("###  Texto corregido:")
        st.write(corrected)


st.caption("Desarrollado con ❤️ usando Streamlit, Google Translate y TextBlob.")
