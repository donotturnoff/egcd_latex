valid = False
while not valid:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        valid = True
    except (NameError, ValueError) as e:
        print("Invalid value")

iterations = []

iterations.append({"i": 0, "q": " ", "r": a, "s": 1, "t": 0})
iterations.append({"i": 1, "q": " ", "r": b, "s": 0, "t": 1})

print("Solving: $a\\cdot{}s+b\\cdot{}t=\\textrm{gcd}(a,b)$; that is, $" + str(a) + "\\cdot{}s+" + str(b) + "\\cdot{}t=\\textrm{gcd}(" + str(a) + "," + str(b) + ")$")

while iterations[-1]["r"] != 0:
    prev = iterations[-1]
    pprev = iterations[-2]
    i = prev["i"] + 1
    q = pprev["r"] // prev["r"]
    r = pprev["r"] % prev["r"]
    s = pprev["s"] - q*prev["s"]
    t = pprev["t"] - q*prev["t"]
    iterations.append({"i": i, "q": q, "r": r, "s": s, "t": t})

print("\\begin{table}")
print(" \\centering")
print(" \\begin{tabular}{|c|c|c|c|c|}")
print("  \\hline")
print("  index $i$ & quotient $q_{i-1}$ & remainder $r_i$ & $s_i$ & $t_i$ \\\\")
print("  \\hline")
for it in iterations:
    print("  " + str(it["i"]) + " & " + str(it["q"]) + " & " + str(it["r"]) + " & " + str(it["s"]) + " & " + str(it["t"]) + " \\\\")
print("  \\hline")
print(" \\end{tabular}")
print("\\end{table}")
