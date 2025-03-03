"""
Robot Display Module
-------------------
Deze module is verantwoordelijk voor het weergeven van de robot 
in de Streamlit interface en het afhandelen van klikinteracties.
"""

import streamlit as st

def display_robot():
    """
    Geeft de robot weer in de Streamlit interface.
    
    Returns:
        bool: True als op de robot is geklikt, anders False
    """
    # Placeholder voor de echte implementatie
    # In de toekomst zal dit SVG of een ander visueel formaat zijn
    
    # We gebruiken een eenvoudige button met robotgezicht als placeholder
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Centreer de robot in de middelste kolom
        clicked = st.button(
            "🤖",
            key="robot_button",
            help="Klik op Stan voor een grappige GitHub uitspraak!"
        )
    
    return clicked
