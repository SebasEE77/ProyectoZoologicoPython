import view.zoologicoView as ZoologicoView
import streamlit as st

if __name__ == '__main__':
    st.set_page_config(
        page_title="Zoologico de Cali",
        layout="wide"
    )
    zoologico = ZoologicoView.zoologicoView()
    zoologico.mostrarMenu()
