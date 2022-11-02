from pathlib import Path

file = Path('myfile.txt')
folder = Path('myFolder')

folder.mkdir()

pythonFile = folder / 'myfile.txt'
pythonFile.write_text('text')