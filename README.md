# Fasta-project

Библиотека для работы с FASTA файлами на Python.

## Описание

Проект реализует два основных класса для работы с биологическими последовательностями в формате FASTA:

- **`Seq`** - представляет отдельную последовательность
- **`FastaReader`** - читает FASTA файлы с поддержкой больших файлов через генераторы

## Установка

```bash

# Клонирование репозитория
git clone https://github.com/Lubov-Kost/fasta-project.git
cd fasta-project
```

## Быстрый старт
```python
from fasta import Seq, FastaReader

# Создание последовательности
seq = Seq("test_sequence", "ATCGATCG")
print(seq)  # Seq('test_sequence', 8, nucleotide)

# Чтение FASTA файла
reader = FastaReader("example.fasta")
for sequence in reader:
    print(f"{sequence.title}: {len(sequence)}")
```

## Использование

### Класс Seq
```python
from fasta import Seq

seq = Seq("my_sequence", "ATCGATCG")
print(len(seq))      # Длина: 8
print(seq.alphabet()) # Тип: nucleotide
print(seq.to_fasta()) # FASTA формат
```

### Класс FastaReader
```python
from fasta import FastaReader

reader = FastaReader("sequences.fasta")
for seq in reader:
    print(f"Заголовок: {seq.title}")
    print(f"Длина: {len(seq)}")
    print(f"Тип: {seq.alphabet()}")
```

## Документация
HTML документация находится в `docs/build/html/index.html`

Чтобы пересобрать документацию:
```bash
cd docs
sphinx-build -b html source build
```

## Демонстрация
Запустите демонстрационную программу:

```bash
python demo.py
```

## Структура проекта
```text
fasta-project/
├── fasta/              # Исходный код
│   ├── __init__.py
│   ├── seq.py
│   └── fasta_reader.py
├── docs/               # Документация
│   ├── source/
│   └── build/html/
├── examples/           # Примеры FASTA файлов
├── demo.py            # Демонстрация
└── README.md          # Этот файл
```

## Лицензия
Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для подробностей.
