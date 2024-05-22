from waifuc.action import ThreeStageSplitAction, FilterSimilarAction, PersonSplitAction
from waifuc.export import SaveExporter
from waifuc.source import LocalSource

if __name__ == '__main__':
    source = LocalSource('G:\F_IMG_INPUT')
    source = source.attach(
        ThreeStageSplitAction(),
        PersonSplitAction(),
        FilterSimilarAction()
  )
    source.export(
        SaveExporter('G:\F_IMG_OUTPUT', no_meta=True)
    )