
import os
import requests
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm

URL = "https://lambda.gsfc.nasa.gov/data/suborbital/ACT/ACT_dr6/dr6_lensing_release.tar.gz"
OUTPUT_FILE = "assets/act_data_v2.tar.gz" # Unique name to avoid locks
CHUNKS = 8  # Reduced to avoid server dropping connections
MAX_RETRIES = 10

def get_session():
    session = requests.Session()
    retry = Retry(
        total=5,
        read=5,
        connect=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    return session

def download_segment(session, url, start, end, filename, chunk_id, pbar):
    headers = {'Range': f'bytes={start}-{end}'}
    
    for attempt in range(MAX_RETRIES):
        try:
            # Open file in r+b mode (must exist)
            with open(filename, "r+b") as f:
                f.seek(start)
                
                # Stream the request
                with session.get(url, headers=headers, stream=True, timeout=30) as r:
                    r.raise_for_status()
                    
                    for chunk in r.iter_content(chunk_size=32768):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))
            return True # Success
            
        except Exception as e:
            time.sleep(2 * attempt) # Exponential backoff attempt
            
            if attempt == MAX_RETRIES - 1:
                # print(f"\n❌ Chunk {chunk_id} FAILED after {MAX_RETRIES} attempts: {e}")
                raise e
    return False

def fast_download():
    if not os.path.exists("assets"):
        os.makedirs("assets")

    print(f"🚀 Initializing Robust Download V2: {URL}")
    print(f"   Target: {OUTPUT_FILE}")
    print(f"   Threads: {CHUNKS}")

    session = get_session()

    # Get file size
    try:
        head = session.head(URL, timeout=10)
        file_size = int(head.headers.get('content-length', 0))
    except:
        # Fallback to get if head fails
        r = session.get(URL, stream=True)
        file_size = int(r.headers.get('content-length', 0))
        r.close()

    print(f"   Size: {file_size / (1024*1024):.2f} MB")

    if file_size == 0:
        print("❌ Error: Could not determine file size.")
        return

    # Create empty file
    with open(OUTPUT_FILE, "wb") as f:
        f.seek(file_size - 1)
        f.write(b"\0")

    chunk_size = file_size // CHUNKS
    ranges = []
    for i in range(CHUNKS):
        start = i * chunk_size
        end = start + chunk_size - 1
        if i == CHUNKS - 1:
            end = file_size - 1
        ranges.append((start, end, i))

    print("\n   [Downloading Chunks...]")
    
    with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
        with ThreadPoolExecutor(max_workers=CHUNKS) as executor:
            futures = []
            for start, end, i in ranges:
                futures.append(
                    executor.submit(download_segment, session, URL, start, end, OUTPUT_FILE, i, pbar)
                )
            
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"\n❌ Critical Failure in thread: {e}")
                    sys.exit(1)

    print("\n✅ Download Complete!")
    
    # Final Size Check
    size_on_disk = os.path.getsize(OUTPUT_FILE)
    if size_on_disk == file_size:
        print("✅ Integrity Check Passed (Size Matches).")
    else:
        print(f"⚠️ Warning: Size Mismatch! (Disk: {size_on_disk} vs Network: {file_size})")

if __name__ == "__main__":
    try:
        fast_download()
    except KeyboardInterrupt:
        print("\n\n⚠️  Download Cancelled.")
