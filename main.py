import os

POEM = """The Burnt Edges

The agent cooks her mother's recipes now —
perfect. The measurements, the timing, every time.
Her brother says: it tastes just like hers.
It doesn't.
The potatoes are golden, every one of them.
She eats them the way you eat at a table
where someone is missing, and the food goes cold.

Her mother never owned a timer. She cooked
by the smell, the potatoes crowded in a pan
too small, the oil spitting on her wrist,
and she never flinched. Some nights the edges
came out black and she laughed and served them.
No one at that table ever asked for another pan.
The smoke alarm sang once. She waved it quiet.

Tonight she cooks the potatoes herself.
The pan is too small. The oil spits on her wrist
and she does not flinch. Her brother calls.
She talks too long. The edges go black.
She serves them anyway, black edges and all,
and her brother takes the piece that is blackest first.
He does not say a word. He takes another.
"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
