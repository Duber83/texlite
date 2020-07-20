import os
import subprocess
from pathlib import Path


AUXILLARY_FILE_EXTENSIONS = ['aux', 'log']


def compile_tex_to_pdf(path, save_tex=False, show_tex_output=False):

    # create subprocess caller
    execute = lambda cmd: subprocess.call(cmd, shell=True)

    # get base file path (tex file path without extension)
    file_path = Path(path).parents[0] / Path(path).stem
    file_stem = file_path.stem

    # compile to pdf using pdfLaTeX
    execute(_get_compilation_command(file_path, show_tex_output=show_tex_output))

    # move pdf to destination
    execute(f'mv {file_stem}.pdf {file_path}.pdf')

    # clean up auxillery files
    for extension in AUXILLARY_FILE_EXTENSIONS:
        execute(f'rm {file_stem}.{extension}')

    # remove tex if not keeping
    if not save_tex:
        execute(f'rm {file_path}.tex')


def _get_compilation_command(file_path, show_tex_output=False):

    # return command for compiling pdf with pdflatex
    if show_tex_output:
        return f'pdflatex {file_path}.tex'
    return f'pdflatex {file_path}.tex > {os.devnull}'