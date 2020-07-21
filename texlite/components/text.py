import re

from texlite.components.common import BACKSLASH, NON_ENCAPSULATION_CHARS


class Text:

    def __init__(self, content):
        self.content = content

    def tex(self):

        # flow through formatting pipes
        formatted_content = self._format_encapsulations(self.content)
        formatted_content = self._format_replacements(formatted_content)
        formatted_content = self._format_figures(formatted_content)
        formatted_content = self._format_hyperlinks(formatted_content)

        return formatted_content

    def _is_encapsulatable(self, text, bad_chars=NON_ENCAPSULATION_CHARS):

        # return if head and tail chars are acceptable for encapsulation
        return not text[0] in bad_chars and not text[-1] in bad_chars

    def _format_encapsulations(self, text):

        # format bold (**)
        for match in re.findall(r'\*\*(.*)\*\*', text):
            if self._is_encapsulatable(match):
                text = text.replace(f'**{match}**',
                                    f'{BACKSLASH}textbf{{{match}}}')

        # format italics (*)
        for match in re.findall(r'\*(.*)\*', text):
            if self._is_encapsulatable(match):
                text = text.replace(f'*{match}*',
                                    f'{BACKSLASH}textit{{{match}}}')

        # format code (`)
        for match in re.findall(r'`(.*)`', text):
            if self._is_encapsulatable(match):
                text = text.replace(f'`{match}`',
                                    f'{BACKSLASH}texttt{{{match}}}')

        # format double quotes (")
        for match in re.findall(r'"(.*)"', text):
            if self._is_encapsulatable(text):
                text = text.replace(f'"{match}"', f'``{match}"')

        return text

    def _format_replacements(self, text):

        # replace horizontal bars with medskips
        text = text.replace('---', r'\medskip')

        return text

    def _format_figures(self, text):

        # format figures/graphics
        for m in re.finditer(r'(!\[.*\]\(.*\))', text):

            # get matched
            match = m.group(1)

            # get href info
            caption_text = re.findall(r'\[(.*)\]', match)[0]
            image_path = re.findall(r'\((.*)\)', match)[0]

            # form figure
            graphics_width = f'{BACKSLASH}textwidth' # f'{BACKSLASH}textwidth'
            if caption_text:
                figure = '\n'.join([
                    f'{BACKSLASH}begin{{figure}}[h!]',
                    f'{BACKSLASH}centering',
                    f'{BACKSLASH}includegraphics[width={graphics_width}]'
                    f'{{{image_path}}}',
                    f'{BACKSLASH}caption{{{Text(caption_text).tex()}}}'
                    f'{BACKSLASH}end{{figure}}',
                ])
            else:
                figure = '\n'.join([
                    f'{BACKSLASH}begin{{figure}}[h!]',
                    f'{BACKSLASH}centering',
                    f'{BACKSLASH}includegraphics[width={graphics_width}]'
                    f'{{{image_path}}}',
                    f'{BACKSLASH}end{{figure}}',
                ])

            # replace text
            text = text.replace(match, figure)

        return text

    def _format_hyperlinks(self, text):

        # format hyperlinks
        for m in re.finditer(r'(\[.*\]\(.*\))', text):

            # get matched
            match = m.group(1)

            # get href info
            link_text = re.findall(r'\[(.*)\]', match)[0]
            link_url = re.findall(r'\((.*)\)', match)[0]

            # form href and replace in text
            href = f'{BACKSLASH}href{{{link_url}}}{{{Text(link_text).tex()}}}'
            text = text.replace(match, href)

        return text
