<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>CFG Parser — Arithmetic Expressions</title>
  <style>
    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;max-width:760px;margin:40px auto;padding:0 16px;color:#111}
    h1{font-size:1.4rem;margin-bottom:4px}
    p.lead{margin-top:0;color:#334}
    pre{background:#f6f8fa;padding:12px;border-radius:6px;overflow:auto}
    ul{margin:8px 0 12px 20px}
    footer{margin-top:18px;font-size:0.9rem;color:#555}
    .row{display:flex;gap:12px;flex-wrap:wrap}
    .chip{background:#eef;padding:6px 8px;border-radius:999px;font-size:0.85rem}
  </style>
</head>
<body>
  <h1>CFG Parser — Arithmetic Expressions</h1>
  <p class="lead">A compact recursive-descent CFG parser with a Tkinter GUI that builds and displays ASTs for arithmetic expressions.</p>

  <div class="row">
    <div class="chip">Operators: + - * /</div>
    <div class="chip">Parentheses</div>
    <div class="chip">Multi-digit numbers &amp; variables</div>
    <div class="chip">Unary +/-</div>
  </div>

  <h2>Quick Start</h2>
  <pre>
git clone &lt;repo&gt;
cd &lt;repo&gt;
python main.py
  </pre>

  <h2>Grammar (informal)</h2>
  <pre>
E → T ((+ | -) T)*
T → F ((* | /) F)*
F → (+|-) F | NUMBER | IDENT | ( E )
  </pre>

  <h2>Example</h2>
  <pre>
Input:  -(3 + x) * 4
AST (pretty): 
* 
  u-
    +
      num(3)
      var(x)
  num(4)
  </pre>

  <footer>
</body>
</html>
