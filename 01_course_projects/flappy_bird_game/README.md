# Flappy Bird Game 🐦

A modern implementation of the classic Flappy Bird game built with Python and Pygame, featuring enhanced graphics, progressive difficulty, and dynamic sound effects.

## 📖 Overview

This project is part of the Zero To Mastery Prompt Engineering Bootcamp, demonstrating how to build engaging games through iterative development and LLM-assisted programming. The game includes three versions showcasing progressive enhancements and feature additions.

## ✨ Features

### Core Gameplay
- **Classic Flappy Bird mechanics** with smooth bird physics
- **Collision detection** with pipes and screen boundaries
- **Progressive difficulty** - pipe speed increases every 10 points
- **Score tracking** with persistent high score display
- **Multiple game states** - Start screen, Playing, and Game Over

### Visual Enhancements
- **Custom bird design** with polygon-based graphics
- **Colorful pipe system** with cyan-colored obstacles
- **Purple gradient background** for improved aesthetics
- **Dynamic score display** positioned at the top center
- **Smooth animations** and visual feedback

### Audio System
- **Procedurally generated sound effects** using NumPy
- **Jump sound** - 660Hz tone with 0.05s duration
- **Score sound** - 880Hz celebratory tone
- **Game over sound** - 220Hz low-pitched feedback
- **Stereo audio support** with 44.1kHz quality

### Game Mechanics
- **Adaptive physics** with slower gravity (0.1) for better control
- **Softer jump mechanics** (-3 velocity) for precise movement
- **Smart pipe generation** with 200px gaps and random positioning
- **Pipe speed progression** from 2 to maximum 5 pixels per frame
- **Off-screen pipe cleanup** for optimal performance

## 🎮 Game Versions

### flappy_birdv1.py
- Basic implementation with core mechanics
- Simple graphics and essential features
- Foundation for subsequent versions

### flappy_birdv2.py
- Enhanced graphics and visual improvements
- Improved collision detection
- Better game state management

### flappy_birdv3.py (Latest)
- Complete feature set with all enhancements
- Procedural audio generation
- Progressive difficulty system
- Optimized performance and cleanup

## 🛠️ Requirements

### System Requirements
- Python 3.7 or higher
- Windows, macOS, or Linux operating system
- Audio output device for sound effects

### Python Dependencies
```bash
pygame>=2.0.0
numpy>=1.19.0
```

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/neural-arun/working_with_LLMs.git
cd working_with_LLMs/flappy_bird_game
```

### 2. Install Dependencies
```bash
# Using pip
pip install pygame numpy

# Using conda
conda install pygame numpy

# Using requirements file (if available)
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "import pygame, numpy; print('Dependencies installed successfully!')"
```

## 🎯 How to Run

### Quick Start
```bash
# Run the latest version
python flappy_birdv3.py

# Or try different versions
python flappy_birdv1.py
python flappy_birdv2.py
```

### Game Controls
- **SPACE BAR** - Make the bird jump/flap
- **SPACE BAR** - Start the game from the start screen
- **SPACE BAR** - Restart after game over
- **ESC or Close Window** - Exit the game

### Gameplay Tips
- 🎯 **Timing is everything** - Master the rhythm of jumping
- 📈 **Progressive challenge** - Game speed increases every 10 points
- 🏆 **Score milestones** - Try to beat your personal best
- 🎵 **Audio cues** - Listen for jump and score sounds

## 🏗️ Project Structure

```
flappy_bird_game/
├── flappy_birdv1.py     # Basic version
├── flappy_birdv2.py     # Enhanced version
├── flappy_birdv3.py     # Complete version
└── README.md            # This documentation
```

## 🔧 Technical Implementation

### Game Architecture
- **Modular function design** for maintainability
- **Separate concerns** - rendering, physics, collision detection
- **Event-driven programming** with Pygame event system
- **State management** for different game phases

### Key Functions
- `create_pipe()` - Generates pipe pairs with random gaps
- `move_pipes()` - Handles pipe movement and cleanup
- `draw_pipes()` - Renders pipes to the screen
- `check_collision()` - Detects bird-pipe and boundary collisions
- `generate_sound()` - Creates procedural audio effects
- `draw_score()` - Displays current score
- `draw_message()` - Shows game state messages

### Performance Optimizations
- **Efficient collision detection** using Pygame Rect objects
- **Memory management** with off-screen object cleanup
- **Optimized rendering** with minimal draw calls
- **Frame rate control** at 60 FPS for smooth gameplay

## 🎨 Customization Options

### Visual Customization
```python
# In the main() function, modify these constants:
PURPLE = (138, 43, 226)      # Background color
CYAN = (0, 255, 255)         # Pipe color
BIRD_COLOR = (255, 165, 0)   # Bird color
SCREEN_WIDTH = 800           # Window width
SCREEN_HEIGHT = 600          # Window height
```

### Gameplay Tuning
```python
# Adjust these variables for different difficulty:
gravity = 0.1                    # Bird fall speed
INITIAL_PIPE_SPEED = 2          # Starting pipe speed
MAX_PIPE_SPEED = 5              # Maximum pipe speed
PIPE_GAP = 200                  # Gap between pipe pairs
```

### Audio Customization
```python
# Modify sound parameters in generate_sound() calls:
jump_sound = generate_sound(frequency=660, duration=0.05, volume=0.3)
score_sound = generate_sound(frequency=880, duration=0.1, volume=0.4)
game_over_sound = generate_sound(frequency=220, duration=0.2, volume=0.5)
```

## 🐛 Troubleshooting

### Common Issues

**ImportError: No module named 'pygame'**
```bash
pip install pygame
```

**ImportError: No module named 'numpy'**
```bash
pip install numpy
```

**No sound output**
- Check system audio settings
- Verify audio device is working
- Try running with `pygame.mixer.pre_init()` parameters adjusted

**Game running too fast/slow**
- Modify the `clock.tick(60)` value in the main game loop
- Adjust `gravity` and `pipe_speed` values

**Window not responding**
- Ensure proper event handling in the game loop
- Check for infinite loops in game logic

## 🚧 Future Enhancements

### Planned Features
- [ ] High score persistence to file
- [ ] Multiple difficulty levels
- [ ] Power-ups and special abilities
- [ ] Animated sprite graphics
- [ ] Background music and improved sound effects
- [ ] Multiplayer support
- [ ] Mobile touch controls
- [ ] Particle effects for collisions

### Technical Improvements
- [ ] Configuration file for easy customization
- [ ] Unit tests for game logic
- [ ] Performance profiling and optimization
- [ ] Cross-platform packaging
- [ ] Save/load game state functionality

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes** with clear, commented code
4. **Test thoroughly** on different systems
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to the branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request** with detailed description

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test on multiple platforms when possible
- Update documentation for new features

## 📄 License

This project is part of educational content and is available for learning purposes. Please respect the original Flappy Bird concept and use this implementation responsibly.

## 🙏 Acknowledgments

- **Zero To Mastery** - For the excellent Prompt Engineering Bootcamp
- **Pygame Community** - For the fantastic game development framework
- **NumPy Team** - For powerful numerical computing capabilities
- **Original Flappy Bird** - By Dong Nguyen for the inspiring game concept

## 📞 Support

If you encounter issues or have questions:

1. Check the troubleshooting section above
2. Review the [Pygame documentation](https://www.pygame.org/docs/)
3. Open an issue in the repository
4. Join the discussion in project issues

---

**Happy Gaming! 🎮** Enjoy playing and learning from this Flappy Bird implementation!
