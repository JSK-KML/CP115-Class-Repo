#!/usr/bin/env python3
import subprocess, sys, re, argparse

TOL = 1e-6
def extract_numbers(text):
    return [float(n) for n in re.findall(r"-?\d+\.?\d*(?:[eE][+-]?\d+)?", text)]

def run_test(script, input_data, expected):
    proc = subprocess.run(
        [sys.executable, script],
        input=input_data,
        text=True,
        capture_output=True
    )
    actual = extract_numbers(proc.stdout)
    ok = len(actual) == len(expected) and all(abs(a - e) < TOL for a,e in zip(actual, expected))
    if ok:
        print(f"PASS {script} | in={input_data.strip()} → out={actual}")
    else:
        print(f"\nFAIL {script}")
        print(f"  Input:    {input_data!r}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}")
    return ok

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--script", help="e.g. lab-03-2.py")
    return p.parse_args()

def main():
    args = parse_args()
    tests = [
        ("lab-03-2.py", "0\n", [0.0]),
        ("lab-03-2.py", "1\n", [287.50]),
        ("lab-03-2.py", "5\n", [1437.50]),

        ("lab-03-3.py", "0\n",    [0.0, 0.0, 0.0, 0.0]),
        ("lab-03-3.py", "1024\n", [1.0, 0.0009765625, 9.5367e-07, 9.3132e-10]),
        ("lab-03-3.py", "1536\n", [1.5, 0.00146484375,1.4305e-06,1.4015e-09]),

        ("lab-03-4.py", "0\n",  [3.00]),
        ("lab-03-4.py", "5\n",  [4.00]),
        ("lab-03-4.py", "10\n", [5.00]),

        ("lab-03-5.py", "0\n", [0.0]),
        ("lab-03-5.py", "1\n", [3000.0]),
        ("lab-03-5.py", "4\n", [12000.0]),

        ("lab-03-6.py", "10 10 4 4\n", [168.00]),
        ("lab-03-6.py", "5 5 2 2\n",   [42.00]),
        ("lab-03-6.py", "20 15 5 5\n", [550.00]),

        ("lab-03-7.py", "0\n",       [32.0, 273.15]),
        ("lab-03-7.py", "100\n",     [212.0, 373.15]),
        ("lab-03-7.py", "-273.15\n", [-459.67, 0.0]),

        ("lab-03-8.py", "1000\n5\n2\n", [100.0,1100.0,100.0/24]),
        ("lab-03-8.py", "500\n3\n1\n",   [15.0,515.0,15.0/12]),
        ("lab-03-8.py", "200\n0\n5\n",   [0.0,200.0,0.0]),
    ]

    if args.script:
        tests = [t for t in tests if t[0] == args.script]

    fail = False
    for script, inp, exp in tests:
        if not run_test(script, inp, exp):
            fail = True

    sys.exit(1 if fail else 0)

if __name__=="__main__":
    main()
