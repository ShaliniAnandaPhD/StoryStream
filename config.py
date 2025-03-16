"""
StoryStream - Configuration Module
Handles loading and managing configuration settings for the StoryStream system.
"""

import os
import json
import yaml

DEFAULT_CONFIG = {
    "name": "StoryStream",
    "version": "0.1.0",
    "demo_mode": True,
    "agents": {
        "causal": {
            "enabled": True,
            "model_path": "models/causal_agent.pkl",
            "threshold": 0.75
        },
        "character": {
            "enabled": True,
            "model_path": "models/character_agent.pkl",
            "max_characters": 10
        },
        "setting": {
            "enabled": True,
            "model_path": "models/setting_agent.pkl",
            "default_timeline": "linear"
        },
        "theme": {
            "enabled": True,
            "model_path": "models/theme_agent.pkl",
            "theme_corpus": "data/themes.json"
        },
        "emotional": {
            "enabled": True,
            "model_path": "models/emotional_agent.pkl",
            "emotion_lexicon": "data/emotion_lexicon.json"
        }
    },
    "knowledge_integration": {
        "enabled": True,
        "knowledge_base": "data/knowledge_base.json",
        "embedding_dim": 256
    },
    "interface": {
        "api_enabled": True,
        "port": 8080,
        "visualization": True
    },
    "generation": {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 1000
    }
}

def load_config(config_path=None):
    """
    Load configuration from a file or use defaults.
    
    Args:
        config_path (str, optional): Path to configuration file. Defaults to None.
        
    Returns:
        dict: Configuration dictionary
    """
    if config_path is None:
        config_path = os.environ.get('STORYSTREAM_CONFIG', 'config.yaml')
    
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            if config_path.endswith('.json'):
                file_config = json.load(f)
            elif config_path.endswith(('.yaml', '.yml')):
                file_config = yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported config format: {config_path}")
        
        # Update default config with file values
        _update_dict(config, file_config)
    
    return config

def _update_dict(d, u):
    """
    Recursively update a dictionary.
    
    Args:
        d (dict): Dictionary to update
        u (dict): Dictionary with updates
    """
    for k, v in u.items():
        if isinstance(v, dict) and k in d and isinstance(d[k], dict):
            _update_dict(d[k], v)
        else:
            d[k] = v

def save_config(config, config_path='config.yaml'):
    """
    Save configuration to a file.
    
    Args:
        config (dict): Configuration dictionary
        config_path (str, optional): Path to save configuration. Defaults to 'config.yaml'.
    """
    with open(config_path, 'w') as f:
        if config_path.endswith('.json'):
            json.dump(config, f, indent=2)
        elif config_path.endswith(('.yaml', '.yml')):
            yaml.dump(config, f, default_flow_style=False)
        else:
            raise ValueError(f"Unsupported config format: {config_path}")
