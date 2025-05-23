# Lorye Go! 香港版

Welcome to **Lorye Go! 香港版**, a fun and engaging train-themed board game set in the vibrant city of Hong Kong! Navigate the MTR (Mass Transit Railway) network, buy properties, compete with friends, and reach destinations to earn rewards. This project combines the classic board game experience with a unique Hong Kong twist, brought to life using Pygame.

- **Website**: [LoryeGo Homepage](https://entzyeung.github.io/LoryeGo)
- **GitHub Repository**: [https://github.com/entzyeung/LoryeGo](https://github.com/entzyeung/LoryeGo)
- **Developed by**: Entz Yeung
- **License**: [MIT License](#license)

---

## Overview

Lorye Go! 香港版 is a digital adaptation of a board game where players roll dice to move across a map of Hong Kong's MTR stations. The game features:
- **Interactive Gameplay**: Move through the MTR network, buy properties, and manage your assets.
- **Seasonal Events**: Random events based on seasons (Spring, Summer, Autumn, Winter) add excitement.
- **Multiplayer Support**: Up to 4 players can compete in a single game.
- **Custom Graphics and Sound**: Handcrafted assets and sound effects enhance the experience.

The game has been packaged into a standalone Windows executable (`.exe`) using PyInstaller, making it easy to distribute and play without requiring Python or Pygame installations.

---

## Features
- Roll dice to determine movement steps.
- Purchase properties at city stations to build your empire.
- Reach destinations to earn cash rewards.
- Experience random events that can teleport you or affect your finances.
- Beautifully designed map with animated backgrounds.
- HUD (Heads-Up Display) for player status and game information.
- Save screenshots during gameplay with the 'S' key.
- Zoom in/out with 'I' and 'O' keys for better map navigation.

---

## Installation

### Prerequisites
- **Operating System**: Windows (tested on Windows 11) or macOS
- **Hardware**: Any modern PC or Mac (remarks: no graphic cards needed. Lightweight executable file.)

### Downloading the Game
1. Visit the [project website](https://entzyeung.github.io/LoryeGo/)
2. Click the "Download .exe" button for Windows or "Download for Mac" for macOS to get the latest version of the game (`Lorye_Go_v994.exe` for Windows, `Lorye_Go_v994.zip` for macOS).
3. The files are hosted on GitHub Releases.

### Running the Game on Windows
1. After downloading, locate the `.exe` file (e.g., `Lorye_Go_v994.exe`).
2. Double-click the file to launch the game.
3. Follow the on-screen instructions to set up the number of players, player names, and game duration.

**Note**: Since this is an `.exe` file, your antivirus might flag it as untrusted. This is common for self-signed executables. Our file is 100% safe.

### Running the Game on macOS
1. After downloading, locate the `.zip` file (e.g., `Lorye_Go_v994.zip`).
2. Double-click the `.zip` file to extract the `Lorye_Go_v994.app` application.
3. Move the `Lorye_Go_v994.app` to your Applications folder (optional but recommended).
4. Double-click the `Lorye_Go_v994.app` to launch the game. You may see a security warning like the one below because I am not a registered Apple developer:

   ![macOS Security Warning](macos_security_warning.png)

   **Security Note**: This warning is normal for apps not signed by a registered Apple developer. I assure you that this app is 100% safe and virus-free. I stand by the integrity of this project.

5. To bypass the warning, go to `System Settings > Privacy & Security`. You’ll see a message saying “Lorye_Go_v994.app” was blocked. Click **Open Anyway** to allow the app to run.
6. Follow the on-screen instructions to set up the number of players, player names, and game duration.

---

## Usage

### Game Setup
- **Number of Players**: Enter 2-4 players during setup.
- **Player Names**: Input names (max 12 characters) for each player.
- **Game Years**: Choose 1-5 years to determine game length.
- **First Destination**: The first player selects the initial destination.

### Gameplay
- **Roll Dice**: Click "擲骰" (Roll Dice) on the HUD to move.
- **Navigate Map**: Use "瀏覽地圖" (Browse Map) to explore or click stations to move.
- **Buy Properties**: Visit city stations to purchase assets.
- **Reach Destinations**: Arrive at the destination to earn HK$1000.
- **Events**: Encounter seasonal or station-specific events that may teleport you or affect your cash.
- **Screenshots**: Press 'S' to save the current screen.
- **Zoom**: Use 'I' to zoom in and 'O' to zoom out.

### Controls
- **Mouse**: Click to roll dice, navigate, or buy properties.
- **Keyboard**:
  - 'S': Save screenshot.
  - 'I': Zoom in.
  - 'O': Zoom out.
  - Arrow keys: Move to adjacent stations.

---

## Development

### Technologies Used
- **Python**: Core programming language.
- **Pygame**: Game development library for graphics, sound, and input.
- **PyInstaller**: Tool to package the game into a Windows executable.
- **Assets**: Custom images, sounds, and fonts stored in the `assets` folder.

---

## Screenshots
![Game Cover](win/screenshots/Lorye_G0_Hong_Kong.png)
![Gameplay Screenshot](win/screenshots/window_screenshot_20250315_071518.jpg)

---

### Issues
This is my side project for fun only, and still under development. This version is just a MVP for demo purpose only. 

- Report bugs or suggest features by opening an [issue](https://github.com/entzyeung/LoryeGo/issues).

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, play, and distribute the game, but please include the original license.

---

## Acknowledgments
- Thanks to the Pygame community for the robust library.
- Inspiration from classic board games like Momotaro Densetsu.
- Special thanks to friends and testers who provided feedback.

---

## Contact
- **GitHub**: [https://github.com/entzyeung](https://github.com/entzyeung)
- **Email**: [entzyeung@gmail.com]

---