import os

ROOT = r'd:\WorkSpace\物理\CQMFormal'

MD_LITERALS = [
    # 公式箭头：重组实现（带标签）
    (r'\xleftrightarrow{\text{重组实现}}', r'\xRightarrow{\text{重组实现}}'),
    (r'\xleftrightarrow{\text{规范重组}}', r'\xRightarrow{\text{规范重组}}'),
    # 公式箭头：子群重组（Z_n/Z_2/Z_N/{e} 标签）
    (r'\xleftrightarrow{Z_n}', r'\xRightarrow{Z_n}'),
    (r'\xleftrightarrow{Z_2}', r'\xRightarrow{Z_2}'),
    (r'\xleftrightarrow{Z_N}', r'\xRightarrow{Z_N}'),
    (r'\xleftrightarrow{\{e\}}', r'\xRightarrow{\{e\}}'),
    # 公式箭头：空标签（FG_纤维丛主丛结构 / Lean README）
    (r'\xleftrightarrow{}', r'\xRightarrow{}'),
    # 商约束箭头（重组商映射）
    (r'\xrightarrow{\;\mathbb{Z}_n\text{ 商}\;}', r'\xRightarrow{\;\mathbb{Z}_n\text{ 商}\;}'),
    (r'\xrightarrow{\mathbb{Z}_n \text{商}}', r'\xRightarrow{\mathbb{Z}_n \text{商}}'),
    # README 图例 / 前沿研究公式（非可伸长 \leftrightarrow，重组语义）
    (r'F=G\leftrightarrow R=G\leftrightarrow\hat{H}', r'F=G\Rightarrow R=G\Rightarrow\hat{H}'),
    (r'（$\leftrightarrow$表示重组实现', r'（$\Rightarrow$表示重组实现'),
    (r'U(1)\leftrightarrow U(1)/\mathbb{Z}_n', r'U(1)\Rightarrow U(1)//\mathbb{Z}_n'),
    (r'SU(5)\leftrightarrow U(1)\times SU(2)\times SU(3)', r'SU(5)\Rightarrow U(1)\times SU(2)\times SU(3)'),
    (r'GL(5)\leftrightarrow SU(5)', r'GL(5)\Rightarrow SU(5)'),
    # 重组商群：单斜杠 -> 双斜杠
    (r'U(1)/\mathbb{Z}', r'U(1)//\mathbb{Z}'),
    (r'U(1)/ℤ', r'U(1)//ℤ'),
    # 文本级重组箭头
    (r'重组实现↔', r'重组实现⇒'),
    (r'重组实现 ↔', r'重组实现 ⇒'),
    (r'↔重组实现', r'⇒重组实现'),
    (r'↔ 重组实现', r'⇒ 重组实现'),
    (r'GL(5) ↔ SU(5)', r'GL(5) ⇒ SU(5)'),
]

LEAN_LITERALS = [
    (r'F=G↔R=G↔Ĥ', r'F=G⇒R=G⇒Ĥ'),
    (r'F = G ↔ R = G ↔ Ĥ', r'F = G ⇒ R = G ⇒ Ĥ'),
    (r'涨落 ↔ 重组实现 ↔', r'涨落 ⇒ 重组实现 ⇒'),
    (r'U(1)/\mathbb{Z}', r'U(1)//\mathbb{Z}'),
    (r'U(1)/Z_', r'U(1)//Z_'),
]


def iter_files(root, ext):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith('归档') and d not in ('.git', '.arts')]
        for fn in filenames:
            if fn.endswith(ext):
                yield os.path.join(dirpath, fn)


def apply(path, literals):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        s = f.read()
    total = 0
    for old, new in literals:
        if old in s:
            total += s.count(old)
            s = s.replace(old, new)
    if total:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(s)
    return total


grand = 0
for p in iter_files(ROOT, '.md'):
    n = apply(p, MD_LITERALS)
    if n:
        print(f'{n:4d}  {os.path.relpath(p, ROOT)}')
        grand += n
for p in iter_files(ROOT, '.lean'):
    n = apply(p, LEAN_LITERALS)
    if n:
        print(f'{n:4d}  {os.path.relpath(p, ROOT)}')
        grand += n
print('TOTAL replacements:', grand)
