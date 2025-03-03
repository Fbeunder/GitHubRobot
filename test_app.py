"""
Test Module
----------
Deze module bevat tests voor de GitHubRobot applicatie.
"""

import pytest
import importlib

def test_modules_importable():
    """Test of alle modules correct geïmporteerd kunnen worden."""
    modules = ['app', 'robot_display', 'quotes_generator', 'styles']
    
    for module_name in modules:
        try:
            importlib.import_module(module_name)
        except ImportError as e:
            pytest.fail(f"Module {module_name} kon niet worden geïmporteerd: {e}")

def test_get_random_quote():
    """Test of de functie get_random_quote een string retourneert."""
    from quotes_generator import get_random_quote
    
    quote = get_random_quote()
    assert isinstance(quote, str)
    assert len(quote) > 0

def test_get_css():
    """Test of de functie get_css een string retourneert met CSS code."""
    from styles import get_css
    
    css = get_css()
    assert isinstance(css, str)
    assert '<style>' in css
    assert '</style>' in css
