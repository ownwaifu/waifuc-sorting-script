# Anime Video Extractor

This repository contains a script to extract and process frames from anime videos. The script uses the `waifuc` library to filter and export images based on various criteria such as person detection, face count, and image size.

## Features

- Filters similar frames (e.g., opening and ending sequences)
- Splits frames by detected persons
- Filters images based on face count
- Filters images based on minimum size
- Renames and orders the extracted images
- Exports the processed images to a specified directory

## Requirements

- Python 3.x
- `waifuc` library with video extension

## Installation

To set up the environment, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/anime-video-extractor.git
    cd anime-video-extractor
    ```

2. Install the required libraries:
    ```bash
    pip install git+https://github.com/deepghs/waifuc.git@main#egg=waifuc[video]
    ```

3. For GPU support with CUDA 12, install `onnxruntime-gpu`:
    ```bash
    pip install onnxruntime-gpu>=1.17
    ```

    **Note:** If you are using Google Colab, install the CUDA 12 version for Colab:
    ```bash
    pip install ort-nightly-gpu --index-url=https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ort-cuda-12-nightly/pypi/simple/
    ```

## Usage

1. Place your input videos in a directory. For example: `G:\\F_ANIME_INPUT\\High School DxD Hero`.

2. Modify the script to set your input and output directories.

3. Run the script:
    ```bash
    python ANIME_Videos_extract.py
    ```

## Script Overview

The script performs the following actions:

1. Loads video files from the specified input directory.
2. Attaches several actions to process the frames:
    - Filters similar frames.
    - Splits frames by detected persons.
    - Ensures frames contain only one face.
    - Filters out small images.
    - Further filters similar images.
    - Splits person images into three stages.
    - Renames and orders the files in PNG format.
3. Exports the processed images to the specified output directory.

## Notes

- Do not run `pip install onnxruntime` as it may break the environment.
- `pyav` installation is unnecessary.

## License

This project is licensed under the MIT License.
