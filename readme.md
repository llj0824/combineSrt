# SRT File Merger Script

This script is designed to merge two SRT (SubRip Text) files into a single file. SRT is a file format that is often used to provide subtitles or captions for video content.

## Functions

The script contains three main functions:

1. `read_srt(file_name)`: This function reads an SRT file and returns its content as a list of blocks, where each block represents a subtitle entry.

2. `write_srt(file_name, content)`: This function writes the provided content into an SRT file.

3. `merge_srt(file1, file2, output_file)`: This function merges two SRT files into a single file. It reads the content of both files, checks if they have the same number of blocks, and then merges them block by block. If the timecodes in the blocks do not match, it raises an error.

## Usage

The script prompts the user to enter the names of the two SRT files to be merged. The merged content is then written into a new file named 'merged.srt'.

Please note that this script assumes that the two SRT files have the same number of blocks and that the timecodes in corresponding blocks match. If these conditions are not met, the script will raise an error.

Example:
```
python combineSrt.py
Enter the first srt file: [chinese]北京遇上西雅图.srt
Enter the second srt file: [eng]北京遇上西雅图.srt
```

## Error Handling

The script includes error handling to ensure that the two SRT files can be correctly merged. If the number of blocks in the two files does not match, or if the timecodes in corresponding blocks do not match, the script will raise a ValueError with a message indicating the nature of the mismatch.