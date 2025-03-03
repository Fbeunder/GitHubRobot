"""
Styles Module
------------
Deze module bevat de CSS-stijlen en opmaak voor de applicatie.
"""

def get_css():
    """
    Retourneert de CSS-stijlen voor de applicatie.
    
    Returns:
        str: Een string met CSS-code
    """
    return """
    <style>
        /* Algemene stijlen */
        .stApp {
            font-family: 'Roboto', sans-serif;
        }
        
        h1 {
            color: #2F80ED;
            text-align: center;
        }
        
        .stButton > button {
            font-size: 72px;
            height: 150px;
            width: 150px;
            border-radius: 50%;
            background-color: #f0f2f6;
            border: none;
            transition: transform 0.3s;
        }
        
        .stButton > button:hover {
            transform: scale(1.1);
            background-color: #e0e2e6;
        }
        
        /* Quote stijlen */
        h3 {
            margin-top: 20px;
            padding: 10px;
            background-color: #f1f8ff;
            border-left: 5px solid #2F80ED;
            text-align: center;
        }
        
        /* Footer stijlen */
        footer {
            margin-top: 50px;
            text-align: center;
            color: #888;
        }
    </style>
    """
