## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Tech Stack](#tech-stack)
* [Tests](#tests)
* [Contributing](#contributing)
* [License](#license)
* [Credits](#credits)

---

## Features

Key functionalities of the project:

* Convert normal text into Morse code instantly 
* Convert Morse code back into readable English text 
* Accepts user-friendly Morse input:

  * `0` for dot
  * `1` for dash
  * space for letter separation
  * `/` for word separation 
* Desktop GUI built using Tkinter with a clean layout 
* Copy output directly to clipboard
* Clear input/output with one click
* Adjustable font sizes for better readability
* Built-in Help window with usage instructions
* Status bar feedback for user actions

---

## Installation

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/morsepy.git
cd morsepy
```

### 2. Ensure Python is installed

Python 3.8+ is recommended.

Check your version:

```bash
python --version
```

### 3. Run the application

```bash
python main.py
```

No external dependencies are required since Tkinter is included with standard Python installations.

---

## Usage

Launch the program and follow these steps:

### 1. Choose conversion mode

* **Text → Morse**
* **Morse → Text**

### 2. Enter input

For Morse input, use:

```
0 = dot
1 = dash
space = letter separator
/ = word separator
```

Example Morse input:

```
0000 0 0100 0100 111 / 011 111 010 0100 100
```

### 3. Click Convert

The result will appear in the output box and can be copied using the **Copy Output** button.

---

## Tech Stack

Technologies used in this project:

* Python 3
* Tkinter – GUI framework for desktop applications
* Modular architecture:

  * Conversion logic module 
  * Morse dictionary module 
  * GUI controller module 

---

## Tests

No automated tests are included yet.

You can manually test by running:

```bash
python main.py
```

Then verify:

* Text converts correctly to Morse
* Morse converts correctly to text
* Clipboard copy works
* Font size dropdown updates text display
* Help window opens successfully

---

## Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

For major improvements, please open an issue first to discuss the proposal.

---

## License

MIT License

Copyright (c) 2026 SiddharthShah30

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Credits

* Built with Python and Tkinter GUI framework
* Morse mappings based on standard international Morse code 
* Designed and developed by SiddharthShah30

---
