"""Rebuild the two cuddle rows from prepared frames without editing source assets."""
import json
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [6, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8]
ROWS = {
    0: ('idle', [0, 1, 2, 2, 3, 4], [1680, 660, 660, 840, 840, 1920]),
    4: ('hover-hug', [0, 1, 2, 3, 4], [140, 140, 140, 140, 280]),
}


def visible_equal(a, b):
    return a.size == b.size and a.getchannel('A').tobytes() == b.getchannel('A').tobytes() and all(
        x == y for x, y in zip(a.get_flattened_data(), b.get_flattened_data()) if x[3]
    )


def validate(atlas):
    if atlas.size != (1536, 2288) or atlas.mode != 'RGBA':
        raise ValueError('Expected 1536x2288 RGBA v2 atlas')
    for row, count in enumerate(COUNTS):
        for col in range(8):
            cell = atlas.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))
            alpha = cell.getchannel('A')
            if (alpha.getbbox() is not None) != (col < count):
                raise ValueError(f'Invalid occupied/empty cell r{row}c{col}')
            if col < count and alpha.getextrema()[0] != 0:
                raise ValueError(f'Opaque cell background r{row}c{col}')


def main():
    original = Image.open(ROOT / 'pet/spritesheet.webp').convert('RGBA')
    validate(original)
    frames = [Image.open(ROOT / f'source/frames/{i}.png').convert('RGBA') for i in range(5)]
    for frame in frames:
        if frame.size != (192, 208) or frame.getchannel('A').getbbox() is None:
            raise ValueError('Expected five nonempty 192x208 transparent frames')
    atlas = original.copy()
    for row, (_, order, _) in ROWS.items():
        for col, index in enumerate(order):
            atlas.paste(frames[index], (col * 192, row * 208))
    validate(atlas)
    out = ROOT / 'dist'
    (out / 'pet').mkdir(parents=True, exist_ok=True)
    (out / 'previews').mkdir(exist_ok=True)
    atlas.save(out / 'pet/spritesheet.webp', lossless=True, quality=100, method=4, exact=True)
    shutil.copy2(ROOT / 'pet/pet.json', out / 'pet/pet.json')
    decoded = Image.open(out / 'pet/spritesheet.webp').convert('RGBA')
    if not visible_equal(atlas, decoded):
        raise ValueError('Encoded atlas pixels changed')
    for row in range(11):
        if row not in ROWS:
            box = (0, row * 208, 1536, (row + 1) * 208)
            if not visible_equal(original.crop(box), decoded.crop(box)):
                raise ValueError(f'Unrelated row changed: {row}')
    for _, (name, order, durations) in ROWS.items():
        seq = [frames[i] for i in order]
        seq[0].save(out / f'previews/{name}.webp', save_all=True, append_images=seq[1:],
                    duration=durations, loop=0, lossless=True, exact=True)
        flattened = []
        for frame in seq:
            bg = Image.new('RGB', frame.size, '#f9f2e8')
            bg.paste(frame, mask=frame.getchannel('A'))
            flattened.append(bg)
        flattened[0].save(out / f'previews/{name}.gif', save_all=True,
                          append_images=flattened[1:], duration=durations, loop=0, disposal=2)
    print(json.dumps({'valid': True, 'output': 'dist/', 'unused_cells_transparent': True,
                      'unrelated_rows_unchanged': True}, ensure_ascii=False))


if __name__ == '__main__':
    main()
