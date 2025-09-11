# Snake Game 🐍

A classic Snake game implementation built as part of the **Zero To Mastery Prompt Engineering Bootcamp** with a focus on Python development and LLM prompt engineering techniques.

## 📖 About This Project

This project demonstrates the development of a classic Snake game using Python and Pygame, created as a learning exercise to explore:
- Python game development fundamentals
- LLM-assisted coding workflows
- Prompt engineering strategies for code generation and refinement
- Iterative development with AI assistance

## 🎮 Game Features

### Version 1 (`snake.py`)
- Classic Snake gameplay mechanics
- Simple rectangular snake segments
- Basic collision detection (walls and self)
- Score tracking and speed progression
- Pause/resume functionality (Press 'P')
- Game over screen with restart option
- Clean purple background with green snake

### Version 2 (`snake_v2.py`) - Enhanced Edition
- **Improved visual design:**
  - Circular snake body segments for smoother appearance
  - Triangular snake head pointing in movement direction
  - Circular food items instead of rectangles
  - Enhanced typography with larger game over text
- **Better game feel:**
  - Slightly adjusted speed progression
  - More polished visual feedback
  - Improved color scheme

## 🚀 How to Run

### Prerequisites
```bash
pip install pygame
```

### Running Version 1 (Basic)
```bash
python snake.py
```

### Running Version 2 (Enhanced)
```bash
python snake_v2.py
```

### Controls
- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **P**: Pause/Resume the game
- **Q**: Quit game (on game over screen)
- **C**: Continue/Restart game (on game over screen)

## 🤖 AI & LLM Integration

### Current Implementation
While the current versions are standalone Python games, this project serves as a foundation for exploring:
- AI-assisted code generation and debugging
- Prompt engineering for game feature enhancement
- LLM-guided code refactoring and optimization

### Future AI Integration Plans
- **Smart Snake AI**: Implement an AI agent that can play the game autonomously
- **Procedural Content**: Use LLMs to generate game variations and challenges
- **Code Documentation**: Automated code explanation and documentation generation
- **Feature Suggestions**: AI-powered gameplay enhancement recommendations

## 📚 Learning & Reflection: Prompt Engineering Strategies

### Effective Strategies Explored

1. **Incremental Feature Development**
   - Started with basic game mechanics
   - Used prompts like: "Add pause functionality to this snake game"
   - Built complexity gradually with targeted feature requests

2. **Code Refinement Through Iteration**
   - Prompt pattern: "Improve the visual appearance of [specific element]"
   - Asked for specific enhancements: "Make the snake head triangular and point in movement direction"

3. **Bug Fixing and Optimization**
   - Descriptive problem statements: "The snake moves too fast when score increases"
   - Requested specific solutions: "Adjust speed progression to be more gradual"

4. **Code Explanation and Documentation**
   - Used prompts like: "Explain how the collision detection works in this code"
   - Requested code comments: "Add detailed comments to the draw_snake function"

### Key Learnings

- **Specificity matters**: Detailed prompts yield better results than vague requests
- **Context is crucial**: Providing existing code context improves AI suggestions
- **Iterative refinement**: Building features step-by-step leads to better outcomes
- **Testing integration**: Always verify AI-suggested code changes work correctly

## 🛠 Technical Details

- **Language**: Python 3.x
- **Framework**: Pygame
- **Game Loop**: 60 FPS with dynamic speed progression
- **Grid System**: 20x20 pixel cells for movement
- **Window Size**: 600x400 pixels

## 📁 File Structure

```
snake_game/
├── snake.py      # Basic version with core functionality
├── snake_v2.py   # Enhanced version with improved visuals
└── README.md     # This documentation file
```

## 🤝 Contributing & Feedback

### We Welcome:
- **Bug reports** and feature suggestions
- **Code improvements** and optimizations
- **New game variations** or modes
- **AI integration** ideas and implementations
- **Prompt engineering** technique sharing

### How to Contribute
1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Share Your Experience
If you use this project to explore prompt engineering or AI-assisted development:
- Share your successful prompts and strategies
- Document interesting AI interactions
- Contribute examples of effective LLM conversations

## 📞 Connect & Collaborate

This project is part of a larger exploration into LLM-assisted development. Connect with us to:
- Share prompt engineering discoveries
- Collaborate on AI integration features
- Discuss best practices for human-AI coding workflows

---

**Happy Coding! 🚀**

*Built with curiosity, enhanced with AI, powered by learning.*
