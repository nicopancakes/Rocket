# Rocket
[![Python Version](https://img.shields.io/badge/python-3.8+-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](https://www.apache.org/licenses/LICENSE-2.0)
[![Release](https://img.shields.io/github/v/release/nicopancakes/Rocket?style=flat-square)](https://github.com/nicopancakes/Rocket/releases)
[![Last Commit](https://img.shields.io/github/last-commit/nicopancakes/Rocket?style=flat-square)](https://github.com/nicopancakes/Rocket/commits/main)

Rocket is a web path enumerator written in Python. It uses `asyncio` and `aiohttp` to perform fast directories, and endpoints during security testing.

The tool includes a default wordlist of over 4,000 paths, 

### Important Notice

This tool is intended **for authorized use**.  
Scanning or probing any system without explicit permission is illegal in most jurisdictions and may violate laws such as the Computer Fraud and Abuse Act (CFAA) in the United States.  
Always obtain written authorization before testing any target you do not own. The maintainer accepts no liability for misuse.

### Features

- High performance scanning  (as of v1.8)
- Configurable concurrency (as of v1.8)
- Custom wordlist support  (as of v1.7)
- Status code filtering  (as of v1.7)
- Request timeout control  (as of v1.8)
- Clean terminal output with status, response time, and content length (as of v1.8)  
- Cross-platform compatibility (Windows, Linux, macOS)

### Requirements

- Python 3.8 or newer  
- aiohttp  
- tqdm
### Installation

Clone the repository and set up a virtual environment (recommended):

```bash
git clone https://github.com/nicopancakes/Rocket.git
cd Rocket

python -m venv venv
source venv/bin/activate      # Linux/macOS
# or on Windows:
venv\Scripts\activate
