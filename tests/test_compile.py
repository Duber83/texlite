import argparse
from pathlib import Path

from texlite.main import main


def test_simple_source():
    '''Tests feeding in a simple source file'''

    # set arguments
    args = {
        'source': Path('tests/assets/test_compile/simple.md'),
        'save_tex': False,
        'show_tex_output': False,
        'dry': False,
    }

    # execute main
    main(args=argparse.Namespace(**args))

    # assert
    assert Path('tests/assets/test_compile/simple.pdf').exists()

    # tear down
    Path('tests/assets/test_compile/simple.pdf').unlink()


def test_saving_tex():
    '''Tests feeding in a simple source file and saving the TeX file'''

    # set arguments
    args = {
        'source': Path('tests/assets/test_compile/simple.md'),
        'save_tex': True,
        'show_tex_output': False,
        'dry': False,
    }

    # execute main
    main(args=argparse.Namespace(**args))

    # assert
    assert Path('tests/assets/test_compile/simple.tex').exists()

    # tear down
    Path('tests/assets/test_compile/simple.pdf').unlink()
    Path('tests/assets/test_compile/simple.tex').unlink()


def test_empty_source():
    '''Tests feeding in an empty source file'''

    # set arguments
    args = {
        'source': Path('tests/assets/test_compile/empty.md'),
        'save_tex': False,
        'show_tex_output': False,
        'dry': False,
    }

    # execute main
    main(args=argparse.Namespace(**args))

    # assert
    assert Path('tests/assets/test_compile/empty.pdf').exists()

    # tear down
    Path('tests/assets/test_compile/empty.pdf').unlink()


def test_nonexistent_source():
    '''Tests feeding in a non-existent file'''

    # set arguments
    args = {
        'source': Path('tests/assets/test_compile/doesnotexist.md'),
        'save_tex': False,
        'show_tex_output': False,
        'dry': False,
    }

    # execute main
    success = main(args=argparse.Namespace(**args))

    # assert
    assert success is False


def test_incorrect_source():
    '''Tests feeding in a file of the wrong type (not .md)'''

    # set arguments
    args = {
        'source': Path('tests/assets/test_compile/incorrect.txt'),
        'save_tex': False,
        'show_tex_output': False,
        'dry': False,
    }

    # execute main
    success = main(args=argparse.Namespace(**args))

    # assert
    assert success is False
