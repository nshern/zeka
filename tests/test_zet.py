from zet import zet


def test_create_front_matter():
    class Args:
        def __init__(self, title, lang, tags):
            self.title = title
            self.lang = lang
            self.tags = tags

    args = Args("Test Title", "en-US", "tag1,tag2")
    filename, front_matter = zet.create_front_matter(args)
    assert filename == "Test Title"
    assert "title: Test Title" in front_matter
    assert "lang: en-US" in front_matter
    assert "tags: tag1,tag2" in front_matter
