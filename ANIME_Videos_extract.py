from waifuc.action import PersonSplitAction, FilterSimilarAction, FileOrderAction, MinSizeFilterAction, FaceCountAction, ThreeStageSplitAction
from waifuc.export import SaveExporter
from waifuc.source import VideoSource

if __name__ == '__main__':
    source = VideoSource.from_directory('G:\F_ANIME_INPUT\High School DxD Hero')
    source = source.attach(
        # filter similar on full frames (e.g. OPs, EDs)
        FilterSimilarAction(),

        # split for each person
        PersonSplitAction(),

        # must contain only 1 face
        FaceCountAction(1),

        # filter images with min(width, height) < 320
        MinSizeFilterAction(320),

        # filter similar person images
        FilterSimilarAction(),

        # split person images
        ThreeStageSplitAction(),
        

        # rename the files in order with png format
        FileOrderAction(ext='.png'),
    )
    source.export(
        SaveExporter('G:\F_ANIME_OUTPUT\High School DxD Hero', no_meta=True)
    )

# install waifuc with video extension
# dont run `pip install onnxruntime` any more, that will break this environment
# also `pip install pyav` is unnecessary
# pip install git+https://github.com/deepghs/waifuc.git@main#egg=waifuc[video]

# install onnxruntime-gpu cuda12 version for colab
# local cuda12 env dont need this, just `pip install onnxruntime-gpu>=1.17`
# pip install ort-nightly-gpu --index-url=https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ort-cuda-12-nightly/pypi/simple/