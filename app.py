"""
GitHubRobot - Hoofdapplicatie
----------------------------
Dit is de hoofdmodule voor de GitHubRobot applicatie.
Het initialiseert de Streamlit interface en verbindt alle componenten.

Stan de GitHub Robot toont grappige GitHub-gerelateerde uitspraken
wanneer erop geklikt wordt.
"""

import streamlit as st
from robot_display import display_robot
from quotes_generator import get_random_quote
import styles

def main():
    """
    Hoofdfunctie die de applicatie initialiseert en uitvoert.
    """
    # Pagina configuratie
    st.set_page_config(
        page_title="Stan de GitHub Robot",
        page_icon=":robot_face:",
        layout="centered"
    )
    
    # Toepassen van custom CSS stijlen
    st.markdown(styles.get_css(), unsafe_allow_html=True)
    
    # Header
    st.title("Stan de GitHub Robot")
    st.markdown("Klik op Stan voor een grappige GitHub uitspraak!")
    
    # Robot weergeven
    clicked = display_robot()
    
    # Als op de robot is geklikt, toon een grappige quote
    if clicked:
        quote = get_random_quote()
        st.markdown(f"### '{quote}'")
        
    # Footer
    st.markdown("---")
    st.markdown("*Gemaakt met Streamlit en Python*")

if __name__ == "__main__":
    main()
