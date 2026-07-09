import markdown

class TextUtility:
    """
    Class: TextUtility
    Description:
        A utility class for text processing and formatting.
    """
    @staticmethod
    def markdown_to_html(markdown_text):
        """將 Markdown 文字轉換為具備語法高亮擴充的 HTML"""
        return markdown.markdown(markdown_text, extensions=['extra', 'codehilite'])