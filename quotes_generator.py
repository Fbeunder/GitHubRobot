"""
Quotes Generator Module
---------------------
Deze module is verantwoordelijk voor het genereren van grappige
GitHub-gerelateerde quotes die Stan de Robot zal uitspreken.
"""

import random

def get_random_quote():
    """
    Selecteert een willekeurige grappige quote over GitHub.
    
    Returns:
        str: Een willekeurige quote
    """
    # Placeholder lijst met eenvoudige quotes
    # In een toekomstige implementatie wordt deze lijst uitgebreid
    quotes = [
        "Ik ben Stan, uw vriendelijke GitHub robot!",
        "Wist je dat GitHub meer dan 100 miljoen repositories heeft?",
        "Git commit, push, repeat... het verhaal van mijn leven!",
        "Merge conflicten zijn als puzzels, maar dan minder leuk.",
        "Branche, commit, merge... ik voel me als een boom!",
        "404: Humor niet gevonden. Maar ik blijf het proberen!"
    ]
    
    return random.choice(quotes)
