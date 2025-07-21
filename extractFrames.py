import cv2
from pathlib import Path

def extract_frames_from_videos(video_folder, output_folder, interval=30):
    video_folder = Path(video_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    if not video_folder.exists():
        print(f"[❌] Folder not found: {video_folder}")
        return

    print("✅ Files in folder:")
    for item in video_folder.iterdir():
        print(" -", item.name)

    # Find all video files
    video_files = []
    for ext in ["*.mp4", "*.MP4", "*.mov", "*.MOV", "*.avi", "*.AVI", "*.mkv", "*.MKV"]:
        video_files += list(video_folder.glob(ext))

    if not video_files:
        print(f"[⚠️] No video files found in: {video_folder}")
        return

    for video_file in video_files:
        print(f"\n🎞️ Processing: {video_file.name}")
        cap = cv2.VideoCapture(str(video_file))
        frame_count = 0
        saved_count = 0

        video_name = video_file.stem
        save_path = output_folder / video_name
        save_path.mkdir(parents=True, exist_ok=True)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % interval == 0:
                frame_filename = save_path / f"frame_{frame_count:05d}.jpg"
                cv2.imwrite(str(frame_filename), frame)
                saved_count += 1
            frame_count += 1
        cap.release()
        print(f"✅ Extracted {saved_count} frames from {video_file.name}")

# ✅ Use your actual path here
extract_frames_from_videos(
    video_folder=r"C:\Users\Veer\OneDrive\Desktop\Bottle Quality Inspection\dataset_videos\close_shots",
    output_folder=r"C:\Users\Veer\OneDrive\Desktop\Bottle Quality Inspection\extracted_frames",
    interval=30
)
