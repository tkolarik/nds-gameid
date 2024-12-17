
# Nintendo DS GameID Generator

## Table of Contents

-   Introduction
    
-   Features
    
-   Prerequisites
    
-   Installation
    
-   Usage
    
    -   Basic Usage
        
    -   Processing Multiple Files
        
-   Example
    
-   Troubleshooting
    
-   Contributing
    
-   License
    
-   Acknowledgements
    

## Introduction

Welcome to the **Nintendo DS GameID Generator**! This utility simplifies the process of generating unique GameIDs for Nintendo DS ROMs by combining the Game Code extracted from the ROM header with the JAMCRC (bitwise NOT of CRC-32) of the ROM's first 512 bytes. Whether you're organizing your ROM collection or developing tools that require unique identifiers, this script provides a straightforward solution.

## Features

-   **Automated GameID Generation:** Combines Game Code and JAMCRC to produce standardized GameIDs.
    
-   **Batch Processing:** Handle multiple ROM files in a single command.
    
-   **Easy Integration:** Can be integrated into larger workflows or scripts.
    
-   **Cross-Platform:** Designed to work seamlessly on macOS, Linux, and Windows (with minor adjustments).
    

## Prerequisites

Before using the Nintendo DS GameID Generator, ensure you have the following dependencies installed on your system:

1.  **Python 3.6 or Higher:**
    
    -   [Download Python](https://www.python.org/downloads/) or install via a package manager.
        
    -   Verify installation:
        
        ```
        python3 --version
        ```
        
2.  **ndstools:**
    
    -   A set of tools for manipulating Nintendo DS ROMs.
        
    -   **Installation via Homebrew (macOS/Linux):**
        
        ```
        brew install ndstools
        ```
        
    -   **Installation via Source:**
        
        -   Visit the [ndstools GitHub repository](https://github.com/smealum/ndstools) for detailed installation instructions.
            
    -   Verify installation:
        
        ```
        ndstool -h
        ```
        

## Installation

1.  **Clone the Repository:**
    
    ```
    git clone https://github.com/yourusername/nds-gameid.git
    ```
    
2.  **Navigate to the Directory:**
    
    ```
    cd nds-gameid
    ```
    
3.  **(Optional) Create a Virtual Environment:**
    
    It's good practice to use a virtual environment to manage dependencies.
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    
4.  **Install Python Dependencies:**
    
    This script relies on Python's standard libraries, so no additional packages are required. However, if you plan to extend the script, you might need to install other packages.
    

## Usage

The main script `generate_gameid.py` processes one or more Nintendo DS ROM files and outputs their corresponding GameIDs.

### Basic Usage

```
python generate_gameid.py /path/to/rom.nds
```

**Example:**

```
python generate_gameid.py "./roms/POKEMON_HG.nds"
```

**Output:**

```
IPKE 4DFFBF91
```

### Processing Multiple Files

You can process multiple ROM files simultaneously by listing them as arguments.

```
python generate_gameid.py /path/to/rom1.nds /path/to/rom2.nds /path/to/rom3.nds
```

**Example:**

```
python generate_gameid.py "./roms/rom1.nds" "./roms/rom2.nds" "./roms/rom3.nds"
```

**Output:**

```
IPKE 4DFFBF91
ABCD 12345678
WXYZ 9ABCDEF0
```

### Making the Script Executable (Optional)

For convenience, you can make the script executable and place it in your PATH.

1.  **Make Executable:**
    
    ```
    chmod +x generate_gameid.py
    ```
    
2.  **Move to a Directory in PATH:**
    
    ```
    sudo mv generate_gameid.py /usr/local/bin/gameid-generator
    ```
    
3.  **Usage:**
    
    ```
    gameid-generator /path/to/rom.nds
    ```
    

## Example

Given the following `ndstools` output for a ROM file:

```
$ ndstool -i ./roms/POKEMON_HG.nds 
Nintendo DS rom tool (commit 5cb7620)
...
0x0C	Game code                	IPKE (NTR-IPKE-USA)
...
```

And running the script:

```
python generate_gameid.py ./roms/POKEMON_HG.nds
```

**Output:**

```
IPKE 4DFFBF91
```

This output follows the required format:

```
IPKE 4DFFBF91
```

Where `IPKE` is the Game Code and `4DFFBF91` is the JAMCRC of the ROM header.

## Troubleshooting

-   `**ndstool**` **Command Not Found:**
    
    -   Ensure `ndstools` is installed and added to your system's PATH.
        
    -   Verify installation by running `ndstool -h`.
        
-   **Permission Issues:**
    
    -   Ensure you have read permissions for the ROM files you're processing.
        
    -   If you encounter permission denied errors, adjust the file permissions or run the script with appropriate privileges.
        
-   **Empty or Corrupted ROM Files:**
    
    -   Ensure the ROM files are not corrupted and contain at least the first 512 bytes required for JAMCRC calculation.
        
-   **Python Errors:**
    
    -   Ensure you're using Python 3.6 or higher.
        
    -   Check for any syntax errors or missing dependencies if you modified the script.
        

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

### How to Contribute

1.  **Fork the Repository**
    
2.  **Create a New Branch:**
    
    ```
    git checkout -b feature/YourFeature
    ```
    
3.  **Commit Your Changes:**
    
    ```
    git commit -m "Add your message here"
    ```
    
4.  **Push to the Branch:**
    
    ```
    git push origin feature/YourFeature
    ```
    
5.  **Open a Pull Request**
    

### Code of Conduct

Please adhere to the Code of Conduct in all interactions.

## License

This project is licensed under the MIT License.

## Acknowledgements

-   **ndstools:** Essential for extracting Game Codes from Nintendo DS ROMs. [ndstools GitHub](https://github.com/smealum/ndstools)
    
-   **Python's binascii Module:** Used for CRC-32 calculations.
    
-   **OpenAI's ChatGPT:** Assisted in developing the initial script and documentation.
    

----------

_Happy Gaming!_