from ytb_downloader.file_name_collector import FileNameCollectorPP


def test__init_():
    fnc = FileNameCollectorPP()
    assert fnc.file_names == []

def test_run():
    fnc = FileNameCollectorPP()
    information = {"filepath": "dummy/path/file.name"}
    first, second = fnc.run(information)
    assert first == []
    assert second == information
    assert fnc.file_names == ["dummy/path/file.name"]
