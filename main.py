"""
StoryStream - Main Entry Point
Main orchestrator for the StoryStream narrative intelligence system.
"""

import logging
from core.narrative_engine import NarrativeEngine
from config import load_config

def setup_logging():
    """Configure the logging system."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("storystream.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('storystream')

def main():
    """Main entry point for StoryStream."""
    logger = setup_logging()
    logger.info("Starting StoryStream Narrative Intelligence System")
    
    # Load configuration
    config = load_config()
    logger.info(f"Loaded configuration: {config['name']}")
    
    # Initialize the narrative engine
    engine = NarrativeEngine(config)
    
    # Example usage
    if config['demo_mode']:
        logger.info("Running in demo mode")
        sample_story = """
        Once upon a time, there was a young woman named Elara who lived in a small village by the sea. 
        She dreamed of exploring the world beyond the horizon. One day, a mysterious ship arrived at the harbor.
        The captain offered her a chance to join the crew. Despite her family's concerns, Elara decided to embark on the journey.
        At sea, she discovered she had a natural talent for navigation using the stars.
        """
        
        # Analyze the sample story
        analysis = engine.analyze_narrative(sample_story)
        print("\nStory Analysis:")
        print(analysis)
        
        # Generate a continuation
        continuation = engine.generate_continuation(sample_story, length=150)
        print("\nStory Continuation:")
        print(continuation)
    
    logger.info("StoryStream execution complete")

if __name__ == "__main__":
    main()
