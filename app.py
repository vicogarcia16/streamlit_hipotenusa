import streamlit as st
import numpy as np

def calcular_hipotenusa(cateto1, cateto2):
    return np.sqrt(cateto1**2 + cateto2**2)

def calcular_cateto_faltante(hipotenusa, cateto_conocido):
    if hipotenusa**2 < cateto_conocido**2:
        raise ValueError("No se puede calcular el cateto faltante. La hipotenusa es menor que el cateto conocido.")
    return np.sqrt(hipotenusa**2 - cateto_conocido**2)

def main():
    
    st.set_page_config(
    page_title="Calculadora de Triángulo Rectángulo",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': 'https://github.com/vicogarcia16/',
        'About': "#### Disfruta esta aplicación *extremadamente* divertida!"
    }
    )
    
    st.title(":blue[Calculadora de Triángulo Rectángulo] :computer:")
    
    st.header("Catetos")
    cateto1 = st.number_input("Cateto 1:", value=0.0, format="%.2f", key="cateto1",
                              help="Ingrese el valor del cateto 1.")
    cateto2 = st.number_input("Cateto 2:", value=0.0, format="%.2f", key="cateto2",
                              help="Ingrese el valor del cateto 2.")

    st.header("Hipotenusa")
    hipotenusa = st.number_input("Hipotenusa:", value=0.0, format="%.2f", key="hipotenusa",
                                 help="Ingrese el valor de la hipotenusa.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.empty() 
        
    with col2:
        calcular_hip = st.button("Calcular Hipotenusa", key="calcular_hip")

    with col3:
        calcular_cateto = st.button("Calcular Cateto", "calcular_cateto")
        
    with col4:
        st.empty()
    
    
    if calcular_hip:
        if cateto1 != 0.0 and cateto2 != 0.0 and hipotenusa == 0.0:
            try:
                resultado = calcular_hipotenusa(cateto1, cateto2)
                st.success(f"Hipotenusa: {resultado:.2f}")
            except ValueError as e:
                st.error(str(e))
        elif cateto1 == 0.0 and cateto2 == 0.0:
            st.warning("Por favor, ingrese los valores de ambos catetos.")
        else:
            st.error("Debe ingresar dos catetos o uno de los catetos y la hipotenusa.")

    if calcular_cateto:
        if hipotenusa != 0.0 and (cateto1 != 0.0 or cateto2 != 0.0):
            try:
                if cateto1 != 0.0 and cateto2 == 0.0:
                    resultado = calcular_cateto_faltante(hipotenusa, cateto1)
                    st.success(f"Cateto 2: {resultado:.2f}")
                elif cateto1 == 0.0 and cateto2 != 0.0:
                    resultado = calcular_cateto_faltante(hipotenusa, cateto2)
                    st.success(f"Cateto 1: {resultado:.2f}")
                else:
                    st.error("Solo debe ingresar un cateto y la hipotenusa.")
            except ValueError as e:
                st.error(str(e))
        else:
            st.error("Debe ingresar la hipotenusa y uno de los catetos.")

if __name__ == "__main__":
    main()
