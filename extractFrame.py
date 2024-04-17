def extract_frame_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    frames = []
    current_frame = {}
    for line in lines:
        if line.startswith("Frame"):
            if current_frame:
                frames.append(current_frame)
                current_frame = {}
            current_frame["Frame Number"] = line.split()[1]
        elif "Source:" in line:
            current_frame["Source Address"] = line.split()[1]
        elif "Destination:" in line:
            current_frame["Destination Address"] = line.split()[1]
        elif "Type:" in line:
            current_frame["Frame Type"] = line.split()[1]

    if current_frame:
        frames.append(current_frame)

    return frames


def display_frames(frames):
    for frame in frames:
        print("Frame Number:", frame["Frame Number"])
        print("Source Address:", frame["Source Address"])
        print("Destination Address:", frame["Destination Address"])
        print("Frame Type:", frame["Frame Type"])
        print()


if __name__ == "__main__":
    filename = "wireShark.txt"
    frames = extract_frame_data(filename)
    display_frames(frames)