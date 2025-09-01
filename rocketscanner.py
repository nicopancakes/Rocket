import asyncio
import aiohttp
from colorama import init, Fore, Style

init(autoreset=True)

SEM_LIMIT = 100

async def check_path(session, sem, base_url, path, results):
    url = base_url.rstrip('/') + '/' + path.strip()
    async with sem:
        try:
            async with session.get(url, timeout=5) as response:
                status = response.status
                if status == 200:
                    results['green'].append((status, url))
                elif status == 404:
                    results['red'].append((status, url))
                else:
                    results['yellow'].append((status, url))
        except:
            results['yellow'].append((None, url)) 

async def main():
    base_url = input("[ ROCKET - ver 1.4 - https://github.com/typescriptlang/Rocket ] Enter the base website URL (e.g. example.com): ").strip()

    if not base_url.startswith(('http://', 'https://')):
        base_url = 'https://' + base_url

    try:
        with open('paths.txt', 'r') as f:
            paths = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}Error: 'paths.txt' file not found.{Style.RESET_ALL}")
        return

    sem = asyncio.Semaphore(SEM_LIMIT)
    results = {'green': [], 'yellow': [], 'red': []}

    async with aiohttp.ClientSession() as session:
        tasks = [check_path(session, sem, base_url, path, results) for path in paths]
        await asyncio.gather(*tasks)

    # Green
    for status, url in sorted(results['green'], key=lambda x: x[1]):
        print(f"{Fore.GREEN}[FOUND] {url} (Status: {status}){Style.RESET_ALL}")

    # Yellow
    for status, url in sorted(results['yellow'], key=lambda x: x[1]):
        status_str = status if status is not None else "ERROR"
        print(f"{Fore.YELLOW}[{status_str}] {url}{Style.RESET_ALL}")

    # Red
    for status, url in sorted(results['red'], key=lambda x: x[1]):
        print(f"{Fore.RED}[NOT FOUND] {url} (Status: {status}){Style.RESET_ALL}")

if __name__ == "__main__":
    asyncio.run(main())
