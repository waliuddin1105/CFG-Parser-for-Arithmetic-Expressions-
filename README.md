<h1>CFG Parser — Arithmetic Expressions</h1>
<p>A compact recursive-descent CFG parser with a Tkinter GUI that builds and displays ASTs for arithmetic expressions.</p>

<ul>
  <li>Operators: + - * /</li>
  <li>Parentheses</li>
  <li>Multi-digit numbers & variables</li>
  <li>Unary +/-</li>
</ul>

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
