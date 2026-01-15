
import tarfile
import os

TAR_FILE = "assets/act_data_v2.tar.gz"
EXTRACT_PATH = "assets/"

def extract_data():
    if not os.path.exists(TAR_FILE):
        print(f"❌ Error: {TAR_FILE} not found.")
        return

    print(f"📦 Extracting {TAR_FILE}...")
    try:
        with tarfile.open(TAR_FILE, "r:gz") as tar:
            
            # List members to see what we are extracting
            members = tar.getmembers()
            count = len(members)
            print(f"   Found {count} files in archive.")
            
            # Filter for the baseline kappa map only to save time/space?
            # Or just extract all. 
            # The user wants "the data", usually implies all relevant. 
            # But the baseline map is what we need. 
            # Let's extract all for completeness as per user intent "download the data".
            
            tar.extractall(path=EXTRACT_PATH)
            print("✅ Extraction Complete.")
            
            # Rename the main file to what our script expects
            # We need to find `act_dr6_lens_kappa_baseline_v1.fits` inside the subdirs
            # and move/copy it to `assets/act_dr6_lens.fits`
            
            found_baseline = False
            for m in members:
                if "kappa_baseline" in m.name and m.name.endswith(".fits"):
                    src = os.path.join(EXTRACT_PATH, m.name)
                    dst = os.path.join(EXTRACT_PATH, "act_dr6_lens.fits")
                    print(f"   Renaming {src} -> {dst}")
                    if os.path.exists(dst):
                        os.remove(dst)
                    os.rename(src, dst)
                    found_baseline = True
                    break
            
            if found_baseline:
                print("✅ Baseline Map Ready: assets/act_dr6_lens.fits")
            else:
                print("⚠️ Warning: Could not auto-locate 'kappa_baseline' FITS file.")
                
    except Exception as e:
        print(f"❌ Extraction Failed: {e}")

if __name__ == "__main__":
    extract_data()
