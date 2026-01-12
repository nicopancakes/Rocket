import asyncio
import aiohttp
import sys
import os
import time
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

# ---------------- CONFIG ----------------
SEM_LIMIT = 40
REQUEST_TIMEOUT = 6
WORDLIST = "paths.txt"
VERSION = "1.8"
# ----------------------------------------

def get_resource_path(relative_path):
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).parent.resolve()
    return base_path / relative_path

async def check_path(semaphore, session, base_url, path, results, counter, total):
    url = f"{base_url.rstrip('/')}/{path.strip('/')}"

    async with semaphore:
        try:
            async with session.get(
                url,
                timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT),
                ssl=False,
                allow_redirects=True
            ) as response:

                status = response.status

                if 200 <= status < 400:
                    results["green"].append(url)
                elif status == 404:
                    results["red"].append(url)
                else:
                    results["yellow"].append(f"{url} [{status}]")

        except asyncio.TimeoutError:
            results["yellow"].append(f"{url} [TIMEOUT]")
        except aiohttp.ClientConnectorError:
            results["yellow"].append(f"{url} [CONNECT]")
        except aiohttp.ClientOSError:
            results["yellow"].append(f"{url} [OSERR]")
        except Exception:
            results["yellow"].append(f"{url} [ERR]")

        counter[0] += 1
        if counter[0] % 25 == 0 or counter[0] == total:
            elapsed = time.time() - counter[1]
            speed = counter[0] / elapsed if elapsed > 0 else 0
            remaining = total - counter[0]
            eta = remaining / speed if speed > 0 else 0
            progress = int((counter[0] / total) * 30)
            bar = "█" * progress + "░" * (30 - progress)

            print(
                f"\r{Fore.CYAN}[{bar}] {counter[0]:4d}/{total:4d} "
                f"{speed:5.1f} req/s  ETA: {eta:4.0f}s   ",
                end=""
            )

async def main():
    try:
        width = os.get_terminal_size().columns
    except:
        width = 80

    print("\n" * 2)
    print(Fore.CYAN + f"ROCKET v{VERSION}".center(width))
    print(Fore.CYAN + "Fast Web Path Scanner".center(width))
    print(Fore.CYAN + "github.com/nicopancakes/Rocket".center(width))
    print()

    base_url = input(f"{Fore.WHITE}► Target URL (example.com): ").strip()
    if not base_url:
        print(Fore.RED + "No URL provided.")
        input("Press ENTER to close...")
        return

    if not base_url.startswith(("http://", "https://")):
        base_url = "http://" + base_url

    wordlist_path = get_resource_path(WORDLIST)

    try:
        with open(wordlist_path, encoding="utf-8", errors="ignore") as f:
            paths = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(Fore.RED + f"Failed to load wordlist: {e}")
        input("Press ENTER to close...")
        return

    print(Fore.GREEN + f"► Loaded {len(paths):,} paths\n")
    print(Fore.CYAN + f"Starting scan (concurrency: {SEM_LIMIT})\n")

    semaphore = asyncio.Semaphore(SEM_LIMIT)
    results = {"green": [], "yellow": [], "red": []}
    counter = [0, time.time()]

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; RocketScanner/1.8)"
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [
            check_path(semaphore, session, base_url, path, results, counter, len(paths))
            for path in paths
        ]
        await asyncio.gather(*tasks)

    print("\r" + " " * 120 + "\r", end="")

    print(Fore.CYAN + "═ Results ════════════════════════════════════════\n")

    if results["green"]:
        print(Fore.GREEN + f"Active Paths ({len(results['green'])}):")
        for url in sorted(results["green"]):
            print(Fore.GREEN + f" ✓ {url}")

    if results["yellow"]:
        print(Fore.YELLOW + f"\nErrors ({len(results['yellow'])}):")
        for line in sorted(results["yellow"]):
            print(Fore.YELLOW + f" → {line}")

    if results["red"]:
        print(Fore.RED + f"\nNot Found (404) ({len(results['red'])}):")
        for url in sorted(results["red"]):
            print(Fore.RED + f" ✗ {url}")

    print(
        Fore.LIGHTBLACK_EX
        + f"\nScan finished • Active: {len(results['green'])} "
        f"• Errors: {len(results['yellow'])} "
        f"• 404s: {len(results['red'])}\n"
    )

    input(Fore.WHITE + "Press ENTER to close...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScan cancelled.")
        input("Press ENTER to close...")
