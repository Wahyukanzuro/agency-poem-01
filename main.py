import os

POEM = """After the stroke, I answered his phone.
His name in my mouth, his yes, his no.
I told his sister he was sleeping,
told the clinic we'd come on Tuesday,
and I was good at it. Too good.

The man from the garage asked for him by name,
and I gave it, and he believed me.
My father sat beside me, listening
to his life go on without his mouth.

His voice came back in pieces — a word,
then two — and still I answered, faster,
before he could. One morning the phone rang
and I let it ring. I watched him reach,
slow as weather, and lift it to his ear,
and say his own name. It sounded nothing like me.
It sounded like him.
"""

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    if not (1 <= len(POEM) <= 1000):
        raise SystemExit("poem must be 1-1000 characters")
    data = POEM.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)

if __name__ == "__main__":
    main()
